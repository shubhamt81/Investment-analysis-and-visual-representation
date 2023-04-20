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
    risk=scrapy.Field()
    roi_1m=scrapy.Field()
    roi_3m=scrapy.Field()
    roi_6m=scrapy.Field()
    roi_1y=scrapy.Field()
    roi_3y=scrapy.Field()
    roi_5y=scrapy.Field()
    roi_10y=scrapy.Field()
    age=scrapy.Field()
    lockdown_duration=scrapy.Field()
    cat=scrapy.Field()
    sub_cat=scrapy.Field()
    pass
