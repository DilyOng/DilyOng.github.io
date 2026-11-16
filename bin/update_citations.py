#!/usr/bin/env python
"""Fetch citation counts for every arXiv paper in the bibliography from several
platforms, remove duplicate citing records, and keep the highest count.

For each paper (any entry in _bibliography/papers.bib with an `arxiv` field) it
downloads the full list of citing works from:

  * InspireHEP        (needs `inspirehep_id` in the bib entry)
  * NASA ADS / SciX   (needs ADS_API_TOKEN)
  * OpenAlex          (no key; set OPENALEX_EMAIL to join the polite pool)
  * Semantic Scholar  (no key needed, S2_API_KEY raises the rate limit)

Within each platform, citing records that are the same paper are merged: they
share an arXiv ID or DOI, or have the same first author and a near-identical
title (e.g. an arXiv preprint and its retitled journal version that the
platform failed to link). The platform with the most unique citing papers
wins; ties go to the earlier platform in SOURCES.

Results go to _data/citation_counts.yml, which _layouts/bib.liquid and
_plugins/first-author-citations.rb read at build time. The file is only
rewritten when a count or link changes. If a platform cannot be reached, its
previous result is kept, so a temporary outage never lowers a badge.
"""

import json
import os
import re
import sys
import time
import unicodedata
import urllib.error
import urllib.parse
import urllib.request
from datetime import date
from difflib import SequenceMatcher

import yaml

BIB_FILE = "_bibliography/papers.bib"
OUTPUT_FILE = "_data/citation_counts.yml"
SOURCES = ["inspirehep", "ads", "openalex", "semanticscholar"]
TITLE_SIMILARITY = 0.75  # same first author + titles at least this similar => same paper
USER_AGENT = "personal-website-citation-updater/1.0"


# --------------------------------------------------------------------------- HTTP


def get_json(url, headers=None, retries=4):
    """GET a JSON document, backing off on rate limits and server errors."""
    req_headers = {"User-Agent": USER_AGENT, "Accept": "application/json"}
    req_headers.update(headers or {})
    delay = 5
    for attempt in range(retries):
        try:
            req = urllib.request.Request(url, headers=req_headers)
            with urllib.request.urlopen(req, timeout=30) as resp:
                return json.load(resp)
        except urllib.error.HTTPError as e:
            if e.code == 404:
                return None
            if e.code in (429, 500, 502, 503, 504) and attempt < retries - 1:
                time.sleep(delay)
                delay *= 2
                continue
            raise
        except urllib.error.URLError:
            if attempt < retries - 1:
                time.sleep(delay)
                delay *= 2
                continue
            raise


# ---------------------------------------------------------------- normalisation


def strip_accents(text):
    return "".join(c for c in unicodedata.normalize("NFKD", text) if not unicodedata.combining(c))


def norm_title(title):
    title = re.sub(r"<[^>]+>", " ", title or "")  # drop HTML/MathML tags
    title = strip_accents(title).lower()
    return re.sub(r"\s+", " ", re.sub(r"[^a-z0-9 ]", "", title)).strip()


def norm_surname(name):
    """'Lee, Seokcheon' / 'Seokcheon Lee' -> 'lee'."""
    name = strip_accents(name or "").strip()
    surname = name.split(",")[0] if "," in name else (name.split() or [""])[-1]
    return re.sub(r"[^a-z]", "", surname.lower())


def norm_arxiv(value):
    value = (value or "").lower().strip()
    value = re.sub(r"^(https?://)?(doi\.org/)?10\.48550/arxiv\.", "", value)
    value = re.sub(r"^arxiv:", "", value)
    return re.sub(r"v\d+$", "", value)


def norm_doi(value):
    value = (value or "").lower().strip()
    value = re.sub(r"^(https?://)?(dx\.)?doi\.org/", "", value)
    if value.startswith("10.48550/arxiv."):
        return None  # arXiv DOIs are handled as arXiv IDs
    return value or None


def record(title, first_author, arxiv_ids=(), dois=()):
    ids = {"arxiv:" + norm_arxiv(a) for a in arxiv_ids if a}
    for d in dois:
        if d and d.lower().replace("https://doi.org/", "").startswith("10.48550/arxiv."):
            ids.add("arxiv:" + norm_arxiv(d))
        elif norm_doi(d):
            ids.add("doi:" + norm_doi(d))
    return {"title": norm_title(title), "author": norm_surname(first_author), "ids": ids}


def unique_count(records):
    """Number of distinct papers after merging duplicate records (union-find)."""
    parent = list(range(len(records)))

    def find(i):
        while parent[i] != i:
            parent[i] = parent[parent[i]]
            i = parent[i]
        return i

    def same_paper(a, b):
        if a["ids"] & b["ids"]:
            return True
        if a["author"] and a["author"] == b["author"] and a["title"] and b["title"]:
            return SequenceMatcher(None, a["title"], b["title"]).ratio() >= TITLE_SIMILARITY
        return False

    for i in range(len(records)):
        for j in range(i + 1, len(records)):
            if same_paper(records[i], records[j]):
                parent[find(i)] = find(j)
    return len({find(i) for i in range(len(records))})


# ---------------------------------------------------------------------- sources


def fetch_inspirehep(paper):
    recid = paper.get("inspirehep_id")
    if not recid:
        return None
    query = urllib.parse.quote(f"refersto:recid:{recid}")
    url = (
        f"https://inspirehep.net/api/literature?q={query}&size=250"
        "&fields=titles.title,authors.full_name,arxiv_eprints.value,dois.value"
    )
    records, raw = [], None
    while url:
        data = get_json(url)
        raw = data["hits"]["total"]
        for hit in data["hits"]["hits"]:
            m = hit["metadata"]
            records.append(
                record(
                    (m.get("titles") or [{}])[0].get("title"),
                    (m.get("authors") or [{}])[0].get("full_name"),
                    [e["value"] for e in m.get("arxiv_eprints", [])],
                    [d["value"] for d in m.get("dois", [])],
                )
            )
        url = data.get("links", {}).get("next")
    return {
        "raw": raw,
        "unique": unique_count(records),
        "url": f"https://inspirehep.net/literature?q=refersto%3Arecid%3A{recid}",
    }


def fetch_ads(paper):
    token = os.environ.get("ADS_API_TOKEN")
    if not token:
        print("  ads: ADS_API_TOKEN not set, skipping")
        return None
    arxiv = paper["arxiv"]
    query = urllib.parse.quote(f"citations(arXiv:{arxiv})")
    url = (
        f"https://api.adsabs.harvard.edu/v1/search/query?q={query}"
        "&fl=title,first_author,identifier,doi&rows=2000"
    )
    data = get_json(url, headers={"Authorization": f"Bearer {token}"})
    docs = data["response"]["docs"]
    records = []
    for d in docs:
        identifiers = d.get("identifier", [])
        arxiv_ids = [i for i in identifiers if i.lower().startswith("arxiv:")]
        records.append(record((d.get("title") or [""])[0], d.get("first_author"), arxiv_ids, d.get("doi", [])))
    return {
        "raw": len(docs),
        "unique": unique_count(records),
        "url": f"https://scixplorer.org/search?q=citations(arXiv%3A{arxiv})",
    }


def openalex_params():
    email = os.environ.get("OPENALEX_EMAIL")
    return f"&mailto={urllib.parse.quote(email)}" if email else ""


def fetch_openalex(paper):
    work = get_json(f"https://api.openalex.org/works/doi:10.48550/arXiv.{paper['arxiv']}?select=id{openalex_params()}")
    if work is None and paper.get("doi"):
        work = get_json(f"https://api.openalex.org/works/doi:{paper['doi']}?select=id{openalex_params()}")
    if work is None:
        return None
    work_id = work["id"].rsplit("/", 1)[-1]
    records, raw, cursor = [], 0, "*"
    while cursor:
        data = get_json(
            f"https://api.openalex.org/works?filter=cites:{work_id}&per_page=200&cursor={cursor}"
            f"&select=display_name,authorships,doi,ids,locations{openalex_params()}"
        )
        for w in data["results"]:
            first = (w.get("authorships") or [{}])[0].get("author", {}).get("display_name")
            dois = [w.get("doi")] + [
                (loc.get("landing_page_url") or "") for loc in w.get("locations", []) if "doi.org" in (loc.get("landing_page_url") or "")
            ]
            records.append(record(w.get("display_name"), first, [], dois))
        raw += len(data["results"])
        cursor = data["meta"].get("next_cursor") if data["results"] else None
    return {
        "raw": raw,
        "unique": unique_count(records),
        "url": f"https://openalex.org/works?filter=cites:{work_id}",
    }


def fetch_semanticscholar(paper):
    key = os.environ.get("S2_API_KEY")
    headers = {"x-api-key": key} if key else {}
    arxiv = paper["arxiv"]
    meta = get_json(f"https://api.semanticscholar.org/graph/v1/paper/ARXIV:{arxiv}?fields=paperId", headers)
    if meta is None:
        return None
    records, offset = [], 0
    while offset is not None:
        time.sleep(1 if key else 3)
        data = get_json(
            f"https://api.semanticscholar.org/graph/v1/paper/ARXIV:{arxiv}/citations"
            f"?fields=title,authors,externalIds&limit=1000&offset={offset}",
            headers,
        )
        for c in data.get("data", []):
            p = c["citingPaper"]
            ext = p.get("externalIds") or {}
            records.append(
                record(p.get("title"), ((p.get("authors") or [{}])[0]).get("name"), [ext.get("ArXiv")], [ext.get("DOI")])
            )
        offset = data.get("next")
    return {
        "raw": len(records),
        "unique": unique_count(records),
        "url": f"https://www.semanticscholar.org/paper/{meta['paperId']}#citing-papers",
    }


FETCHERS = {
    "inspirehep": fetch_inspirehep,
    "ads": fetch_ads,
    "openalex": fetch_openalex,
    "semanticscholar": fetch_semanticscholar,
}


# ------------------------------------------------------------------------- main


def read_bib(path):
    """Minimal BibTeX reader: the fields this script needs, per entry."""
    with open(path, encoding="utf-8") as f:
        text = f.read()
    papers = []
    for block in re.split(r"\n(?=@\w+\{)", text):
        fields = dict(re.findall(r"^\s*(\w+)\s*=\s*\{(.*)\},?\s*$", block, re.M))
        if fields.get("arxiv"):
            papers.append(
                {
                    "arxiv": fields["arxiv"].strip(),
                    "title": fields.get("title", "").strip(),
                    "inspirehep_id": fields.get("inspirehep_id", "").strip() or None,
                    "doi": fields.get("doi", "").strip() or None,
                }
            )
    return papers


def main():
    previous = {}
    if os.path.exists(OUTPUT_FILE):
        with open(OUTPUT_FILE, encoding="utf-8") as f:
            previous = (yaml.safe_load(f) or {}).get("papers", {}) or {}

    papers_out = {}
    for paper in read_bib(BIB_FILE):
        arxiv = paper["arxiv"]
        print(f"{arxiv}  {paper['title'][:70]}")
        old_sources = (previous.get(arxiv) or {}).get("sources", {}) or {}
        sources = {}
        for name in SOURCES:
            try:
                result = FETCHERS[name](paper)
            except Exception as e:  # keep yesterday's value if a platform is down
                print(f"  {name}: failed ({type(e).__name__}: {e}); keeping previous value")
                result = old_sources.get(name)
            if result:
                sources[name] = result
                print(f"  {name}: {result['raw']} listed, {result['unique']} unique")
        if not sources:
            if arxiv in previous:
                papers_out[arxiv] = previous[arxiv]
            continue
        best = max(SOURCES, key=lambda s: (sources[s]["unique"] if s in sources else -1, -SOURCES.index(s)))
        papers_out[arxiv] = {
            "title": paper["title"],
            "count": sources[best]["unique"],
            "source": best,
            "url": sources[best]["url"],
            "sources": sources,
        }
        print(f"  -> {sources[best]['unique']} from {best}")

    if papers_out == previous:
        print("No change in citation counts.")
        return
    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        f.write("# Generated daily by bin/update_citations.py -- do not edit by hand.\n")
        yaml.safe_dump(
            {"last_updated": date.today().isoformat(), "papers": papers_out},
            f,
            sort_keys=False,
            allow_unicode=True,
            width=1000,
        )
    print(f"Wrote {OUTPUT_FILE}")


if __name__ == "__main__":
    sys.exit(main())
