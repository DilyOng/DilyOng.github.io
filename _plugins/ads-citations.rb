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

    def render(context)
      arxiv_id = context[@arxiv_id.strip]
      api_token = ENV['ADS_API_TOKEN']

      unless api_token
        puts "Warning: ADS_API_TOKEN environment variable not set. Skipping ADS citation fetch for #{arxiv_id}."
        return "N/A"
      end

      begin
        # If the citation count has already been fetched, return it
        if ADSCitationsTag::Citations[arxiv_id]
          return ADSCitationsTag::Citations[arxiv_id]
        end

        # Fetch the citation count from the ADS API
        uri = URI("https://api.adsabs.harvard.edu/v1/search/query?q=arXiv:#{arxiv_id}&fl=citation_count,bibcode")
        http = Net::HTTP.new(uri.host, uri.port)
        http.use_ssl = true
        request = Net::HTTP::Get.new(uri)
        request['Authorization'] = "Bearer #{api_token}"

        response = http.request(request)
        data = JSON.parse(response.body)

        # Extract citation count from the JSON data
        citation_count = data["response"]["docs"][0]["citation_count"].to_i

        # Format the citation count for readability
        citation_count = Helpers.number_to_human(citation_count, format: '%n%u', precision: 2, units: { thousand: 'K', million: 'M', billion: 'B' })

      rescue Exception => e
        # Handle any errors that may occur during fetching
        citation_count = "N/A"

        # Print the error message including the exception class and message
        puts "Error fetching ADS citation count for #{arxiv_id}: #{e.class} - #{e.message}"
      end

      ADSCitationsTag::Citations[arxiv_id] = citation_count
      return "#{citation_count}"
    end
  end
end

Liquid::Template.register_tag('ads_citations', Jekyll::ADSCitationsTag)
