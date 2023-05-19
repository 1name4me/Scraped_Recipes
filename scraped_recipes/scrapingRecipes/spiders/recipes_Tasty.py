import json
import scrapy
from ..items import ScrapingrecipesItem

# LUNCH
class TastyRecipesSpider(scrapy.Spider):
    name = 'tasty_recipes'
    allowed_domains = [
        'tasty.co'
    ]
    start_urls = ['https://tasty.co/api/proxy/tasty/feed-page?from=0&size=901&slug=lunch&type=topic']

    custom_settings = {
        'FEEDS': {
            'Lunch_recipes.csv': {
                'format': 'csv'
            }
        }
    }

    def parse(self, response):
        item = ScrapingrecipesItem()

        data = json.loads(response.body)
        tasty_recipes = data.get('items')

        for i in tasty_recipes:
            title = i.get('name')
            image = i.get('thumbnail_url')
            link = i.get('id')


            # reviews =

            item['title'] = title
            item['image'] = image
            item['link'] = link


            # item['reviews'] = reviews

            yield item



## BREAKFAST
class BreakfastTastyRecipesSpider(scrapy.Spider):
    name = 'tasty_recipes_breakfast'
    allowed_domains = [
        'tasty.co'
    ]
    start_urls = ['https://tasty.co/api/proxy/tasty/feed-page?from=0&size=901&slug=breakfast&type=topic']

    custom_settings = {
        'FEEDS': {
            'Breakfast_recipes.csv': {
                'format': 'csv'
            }
        }
    }

    def parse(self, response):
        item = ScrapingrecipesItem()

        data = json.loads(response.body)
        tasty_recipes = data.get('items')

        for i in tasty_recipes:
            title = i.get('name')
            image = i.get('thumbnail_url')
            link = i.get('id')


            # reviews =

            item['title'] = title
            item['image'] = image
            item['link'] = link


            # item['reviews'] = reviews

            yield item


## DINNER
class DinnerTastyRecipesSpider(scrapy.Spider):
    name = 'tasty_recipes_Dinner'
    allowed_domains = [
        'tasty.co'
    ]
    start_urls = ['https://tasty.co/api/proxy/tasty/feed-page?from=0&size=1890&slug=dinner&type=topic']

    custom_settings = {
        'FEEDS': {
            'Dinner_recipes.csv': {
                'format': 'csv'
            }
        }
    }

    def parse(self, response):
        item = ScrapingrecipesItem()

        data = json.loads(response.body)
        tasty_recipes = data.get('items')

        for i in tasty_recipes:
            title = i.get('name')
            image = i.get('thumbnail_url')
            link = i.get('id')


            # reviews =

            item['title'] = title
            item['image'] = image
            item['link'] = link


            # item['reviews'] = reviews

            yield item


##DESSERTS
class DessertsTastyRecipesSpider(scrapy.Spider):
    name = 'tasty_recipes_Desserts'
    allowed_domains = [
        'tasty.co'
    ]
    start_urls = ['https://tasty.co/api/proxy/tasty/feed-page?from=0&size=2020&slug=desserts&type=topic']

    custom_settings = {
        'FEEDS': {
            'Desserts_recipes.csv': {
                'format': 'csv'
            }
        }
    }

    def parse(self, response):
        item = ScrapingrecipesItem()

        data = json.loads(response.body)
        tasty_recipes = data.get('items')

        for i in tasty_recipes:
            title = i.get('name')
            image = i.get('thumbnail_url')
            link = i.get('id')


            # reviews =

            item['title'] = title
            item['image'] = image
            item['link'] = link


            # item['reviews'] = reviews

            yield item