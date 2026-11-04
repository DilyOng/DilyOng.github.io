require "active_support/all"
require 'net/http'
require 'json'
require 'uri'

module Helpers
  extend ActiveSupport::NumberHelper
end

module Jekyll
  class ADSCitationsTag < Liquid::Tag
    Citations = { }

    def initialize(tag_name, params, tokens)
      super
      @arxiv_id = params.strip
    end

    # Raw integer citation count (or nil on failure), cached per build so the
    # badge and the first-author total always agree.
    def self.fetch_count(arxiv_id)
      arxiv_id = arxiv_id.to_s
      return Citations[arxiv_id] if Citations.key?(arxiv_id)

      api_token = ENV['ADS_API_TOKEN']
      unless api_token
        puts "Warning: ADS_API_TOKEN environment variable not set. Skipping ADS citation fetch for #{arxiv_id}."
        return Citations[arxiv_id] = nil
      end

      begin
        uri = URI("https://api.adsabs.harvard.edu/v1/search/query?q=arXiv:#{arxiv_id}&fl=citation_count,bibcode")
        http = Net::HTTP.new(uri.host, uri.port)
        http.use_ssl = true
        request = Net::HTTP::Get.new(uri)
        request['Authorization'] = "Bearer #{api_token}"
        response = http.request(request)
        data = JSON.parse(response.body)

        # Surface the real reason when ADS does not return a result set, so a
        # bad token / rate limit / empty match is distinguishable in build logs.
        docs = data.dig("response", "docs")
        if docs.nil?
          puts "Warning: ADS returned no result set for #{arxiv_id} (HTTP #{response.code}): #{response.body.to_s[0, 300]}"
          count = nil
        elsif docs.empty?
          puts "Warning: ADS has no record matching arXiv:#{arxiv_id} (HTTP #{response.code})."
          count = nil
        else
          count = docs[0]["citation_count"].to_i
        end
      rescue Exception => e
        count = nil
        puts "Error fetching ADS citation count for #{arxiv_id}: #{e.class} - #{e.message}"
      end
      Citations[arxiv_id] = count
    end

    def render(context)
      count = ADSCitationsTag.fetch_count(context[@arxiv_id.strip])
      return "N/A" if count.nil?
      Helpers.number_to_human(count, format: '%n%u', precision: 2, units: { thousand: 'K', million: 'M', billion: 'B' }).to_s
    end
  end
end

Liquid::Template.register_tag('ads_citations', Jekyll::ADSCitationsTag)
