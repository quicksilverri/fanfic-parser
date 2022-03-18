# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class FanficsItem(scrapy.Item):
    title = scrapy.Field()
    author = scrapy.Field()
    date = scrapy.Field()
    fandoms = scrapy.Field()
    characters = scrapy.Field()
    parings = scrapy.Field()
    warnings = scrapy.Field()
    freeforms = scrapy.Field()
    description = scrapy.Field()
    language = scrapy.Field()
    number_of_words = scrapy.Field()
    hits = scrapy.Field()

# title author date fandoms characters parings warnings freeforms description language number_of_words hits
