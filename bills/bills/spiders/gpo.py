# -*- coding: utf-8 -*-
import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor


class GpoSpider(scrapy.Spider):
    name = "gpo"
    #allowed_domains = ["https://www.gpo.gov/fdsys/bulkdata"]
    start_urls = [
        'https://www.gpo.gov/fdsys/bulkdata',
    ]

    #rules = (
    #    Rule(LinkExtractor(allow=('https://www.gpo.gov/fdsys/bulkdata/*')),callback='parse')
    #)


    def parse(self, response):
        for page in response.xpath('//div[@id="bulkdata"]/table/tr'):
            if page.xpath('.//a[contains(@href, "xml")]/@href').extract_first():
                yield {
                    'bill': page.xpath('.//td[1]/a/@href').extract_first(),
                    'date': page.xpath('.//td[2]/text()').extract_first(),
                    'size': page.xpath('.//td[3]/text()').extract_first(),
                }
            else:
                next_link = page.xpath('.//td[1]/a[not(contains(@href, "zip"))]/@href').extract_first()
                # gotta get rid of html, zip, pdf, xsl, and other junk
                if next_link is not None:
                    yield {
                        'link': next_link
                    }
                    next_link = response.urljoin(next_link)
                    yield scrapy.Request(next_link, callback=self.parse)
