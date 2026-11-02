#!/usr/bin/env python
"""Refresh _data/repo_stats.yml from the GitHub API.

Reads the repo list from _data/repositories.yml (github_repos) and stores the
description, primary language, stars and forks for each, so the repositories
page can render its cards without relying on an external image service.
Set GITHUB_TOKEN to avoid the unauthenticated rate limit.
"""

import json
import os
import sys
import urllib.request

import yaml

REPOS_FILE = "_data/repositories.yml"
OUT_FILE = "_data/repo_stats.yml"


def fetch(repo):
    req = urllib.request.Request(
        f"https://api.github.com/repos/{repo}",
        headers={"Accept": "application/vnd.github+json"},
    )
    token = os.environ.get("GITHUB_TOKEN")
    if token:
        req.add_header("Authorization", f"Bearer {token}")
    with urllib.request.urlopen(req, timeout=30) as resp:
        return json.load(resp)


def main():
    with open(REPOS_FILE) as f:
        repos = yaml.safe_load(f).get("github_repos") or []

    try:
        with open(OUT_FILE) as f:
            existing = yaml.safe_load(f) or {}
    except FileNotFoundError:
        existing = {}

    stats = {}
    failed = False
    for repo in repos:
        try:
            d = fetch(repo)
            stats[repo] = {
                "description": d.get("description") or "",
                "language": d.get("language") or "",
                "stars": d.get("stargazers_count", 0),
                "forks": d.get("forks_count", 0),
            }
            print(f"{repo}: {stats[repo]['stars']} stars, {stats[repo]['forks']} forks")
        except Exception as e:  # keep previous data for this repo on failure
            print(f"Failed to fetch {repo}: {e}", file=sys.stderr)
            failed = True
            if repo in existing:
                stats[repo] = existing[repo]

    with open(OUT_FILE, "w") as f:
        yaml.safe_dump(stats, f, sort_keys=False, allow_unicode=True, width=1000)

    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
