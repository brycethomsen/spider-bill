# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class BillsItem(scrapy.Item):
    bill = scrapy.Field()
    date = scrapy.Field()
    size = scrapy.Field()
    link = scrapy.Field()
