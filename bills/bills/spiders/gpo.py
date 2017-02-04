# -*- coding: utf-8 -*-
import scrapy


class GpoSpider(scrapy.Spider):
    name = "gpo"
    allowed_domains = ["https://www.gpo.gov/fdsys/bulkdata"]
    start_urls = ['http://https://www.gpo.gov/fdsys/bulkdata/']

    def parse(self, response):
        pass
