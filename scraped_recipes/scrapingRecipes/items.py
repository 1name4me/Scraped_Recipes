# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class ScrapingrecipesItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    # tasty_image = scrapy.Field()
    # tasty_title = scrapy.Field()
    # tasty_link = scrapy.Field()

    title = scrapy.Field()
    image = scrapy.Field()
    link = scrapy.Field()



