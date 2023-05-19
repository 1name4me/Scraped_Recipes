import json
import scrapy
from ..items import ScrapingrecipesItem


# class DessertsRecipesSpider(scrapy.Spider):
#     name = 'noOnion_recipes'
#     allowed_domains = [
#         'vegrecipesofindia.com'
#     ]
#
#     custom_settings = {
#         'FEEDS' : {
#             'NoOnions_recipes.csv': {
#                 'format': 'csv'
#             }
#         }
#     }
#     # start_urls = ['https://tasty.co/api/proxy/tasty/feed-page?from=0&size=901&slug=lunch&type=topic']
#
#     def start_requests(self):
#         url = 'https://www.vegrecipesofindia.com/recipes/no-onion-no-garlic-recipes/page/{}'
#
#         for i in range(1,26):
#             yield scrapy.Request(url.format(i))
#
#     def parse(self, response):
#         item = ScrapingrecipesItem()
#
#         allrecipes = response.css('div.component.tout')
#         for recipe in allrecipes:
#             title = recipe.css('div.tout__imageContainer a::attr(title)').get()
#             image = recipe.css('a.tout__imageLink img::attr(src)').get()
#             link = recipe.css('a.post-summary__image::attr(href)').get()
#
#
#
#             item['title'] = title
#             item['image'] = image
#             item['link'] = link
#
#
#
#             yield item

class DessertsRecipesSpider(scrapy.Spider):
    name = 'noOnion_recipes'
    allowed_domains = [
        'pixabay.com'
    ]

    # custom_settings = {
    #     'FEEDS' : {
    #         'NoOnions_recipes.csv': {
    #             'format': 'csv'
    #         }
    #     }
    # }
    # start_urls = ['https://tasty.co/api/proxy/tasty/feed-page?from=0&size=901&slug=lunch&type=topic']

    def start_requests(self):
        url = 'https://pixabay.com/images/search/?order=ec&pagi={}'

        for i in range(1,215):
            yield scrapy.Request(url.format(i))

    def parse(self, response):
        item = ScrapingrecipesItem()

        allrecipes = response.css('div.row-masonry-cell')
        for recipe in allrecipes:
            image = recipe.css('a.tout__imageLink img::attr(src)').get()





            item['image'] = image




            yield item