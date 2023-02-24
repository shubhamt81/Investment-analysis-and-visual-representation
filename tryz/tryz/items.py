# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class TryzItem(scrapy.Item):
    # define the fields for your item here like:
    company_name=scrapy.Field()
    fund_name = scrapy.Field()
    link=scrapy.Field()
    val=scrapy.Field()
    roi=scrapy.Field()
    type=scrapy.Field()
    pass
