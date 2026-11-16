require 'bibtex'

# Computes the total citations of first-author papers, using exactly the same
# per-paper count shown in the "Cited by" badge (see _layouts/bib.liquid):
#   _data/citation_counts.yml (highest de-duplicated count across platforms,
#   refreshed daily by bin/update_citations.py) -> manual cited_by fallback ->
#   cited_by_override wins.
#
# Exposed as {{ site.first_author_citations }}, and substituted for the
# placeholder {first_author_citations} in any page's front-matter description.
module Jekyll
  module FirstAuthorCitations
    PLACEHOLDER = '{first_author_citations}'.freeze

    def self.field(entry, name)
      entry.has_field?(name) ? entry[name].to_s.strip : nil
    end

    def self.badge_count(entry, counts)
      count = 0
      arxiv = field(entry, :arxiv)
      record = counts[arxiv] if arxiv && !arxiv.empty?
      count = record['count'].to_i if record
      if count == 0 && field(entry, :cited_by) && field(entry, :cited_by_url)
        count = field(entry, :cited_by).to_i
      end
      override = field(entry, :cited_by_override)
      count = override.to_i if override && !override.empty?
      count
    end

    def self.total(site)
      scholar = site.config['scholar'] || {}
      last_names = Array(scholar['last_name']).map { |n| n.to_s.downcase }
      counts = (site.data['citation_counts'] || {})['papers'] || {}
      source = File.join(site.source, scholar['source'] || '_bibliography')
      path = File.join(source, scholar['bibliography'] || 'papers.bib')

      bib = BibTeX.open(path, filter: nil)
      bib.each_entry.sum do |entry|
        next 0 unless entry.respond_to?(:author) && entry.author
        first = entry.author.first
        next 0 unless first && last_names.include?(first.last.to_s.downcase)
        badge_count(entry, counts)
      end
    rescue StandardError => e
      Jekyll.logger.warn 'FirstAuthorCitations:', "#{e.class} - #{e.message}"
      nil
    end
  end
end

Jekyll::Hooks.register :site, :post_read do |site|
  total = Jekyll::FirstAuthorCitations.total(site)
  next if total.nil?

  site.config['first_author_citations'] = total
  Jekyll.logger.info 'FirstAuthorCitations:', "total = #{total}"
  (site.pages + site.documents).each do |page|
    desc = page.data['description']
    next unless desc.is_a?(String) && desc.include?(Jekyll::FirstAuthorCitations::PLACEHOLDER)

    page.data['description'] = desc.gsub(Jekyll::FirstAuthorCitations::PLACEHOLDER, total.to_s)
  end
end
