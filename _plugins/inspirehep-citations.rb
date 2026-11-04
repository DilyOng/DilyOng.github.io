require "active_support/all"
require 'net/http'
require 'json'
require 'uri'

module Helpers
  extend ActiveSupport::NumberHelper
end

module Jekyll
  class InspireHEPCitationsTag < Liquid::Tag
    Citations = { }

    def initialize(tag_name, params, tokens)
      super
      @recid = params.strip
    end

    # Raw integer citation count (or nil on failure), cached per build so the
    # badge and the first-author total always agree.
    def self.fetch_count(recid)
      recid = recid.to_s
      return Citations[recid] if Citations.key?(recid)

      api_url = "https://inspirehep.net/api/literature/?fields=citation_count&q=recid:#{recid}"
      begin
        data = JSON.parse(Net::HTTP.get(URI(api_url)))
        count = data["hits"]["hits"][0]["metadata"]["citation_count"].to_i
      rescue Exception => e
        count = nil
        puts "Error fetching citation count for #{recid}: #{e.class} - #{e.message}"
      end
      Citations[recid] = count
    end

    def render(context)
      count = InspireHEPCitationsTag.fetch_count(context[@recid.strip])
      return "N/A" if count.nil?
      Helpers.number_to_human(count, format: '%n%u', precision: 2, units: { thousand: 'K', million: 'M', billion: 'B' }).to_s
    end
  end
end

Liquid::Template.register_tag('inspirehep_citations', Jekyll::InspireHEPCitationsTag)
