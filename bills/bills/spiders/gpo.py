# -*- coding: utf-8 -*-
import scrapy


class GpoSpider(scrapy.Spider):
    name = "gpo"
    allowed_domains = ["https://www.gpo.gov/fdsys/bulkdata"]
    #start_urls = ['http://https://www.gpo.gov/fdsys/bulkdata/']
    start_urls = [
        'https://www.gpo.gov/fdsys/bulkdata/BILLSTATUS/115/sres',
    ]


    def parse(self, response):
        #response.xpath('//a[contains(@href, "xml")]/@href').extract()
        for page in response.xpath('//div[@id="bulkdata"]/table/tr'):
            if page.xpath('.//a[contains(@href, "xml")]/@href').extract_first():
                yield {
                    'bill': page.xpath('.//td[1]/a/@href').extract_first()
                    'date': page.xpath('.//td[2]/text()').extract_first()
                    'size': page.xpath('.//td[3]/text()').extract_first()
                }

        next_page = response.css('li.next a::attr(href)').extract_first()
        if next_page is not None:
            next_page = response.urljoin(next_page)
            yield scrapy.Request(next_page, callback=self.parse)
