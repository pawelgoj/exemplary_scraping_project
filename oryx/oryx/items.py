# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class OryxItem(scrapy.Item):
    # define the fields for your item here like:
    data = scrapy.Field()
    country = scrapy.Field()
    staf = scrapy.Field()
    content = scrapy.Field()
    

