import json
import scrapy
from ..items import ScrapingrecipesItem


# AllRecipes LUNCH
class RecipesSpider(scrapy.Spider):
    name = 'recipes'
    allowed_domains = [
        'allrecipes.com'
    ]

    custom_settings = {
        'FEEDS' : {
            'Lunch_recipes.csv': {
                'format': 'csv'
            }
        }
    }
    # start_urls = ['https://tasty.co/api/proxy/tasty/feed-page?from=0&size=901&slug=lunch&type=topic']

    def start_requests(self):
        url = 'https://www.allrecipes.com/recipes/17561/lunch/?page={}'

        for i in range(2,154):
            yield scrapy.Request(url.format(i))

    def parse(self, response):
        item = ScrapingrecipesItem()

        allrecipes = response.css('div.component.tout')
        for recipe in allrecipes:
            title = recipe.css('div.tout__imageContainer a::attr(title)').get()
            image = recipe.css('a.tout__imageLink img::attr(src)').get()
            link = 'https://www.allrecipes.com' + recipe.css('div.tout__imageContainer a::attr(href)').get()



            item['title'] = title
            item['image'] = image
            item['link'] = link



            yield item

#BREAKFAST
class BreakfastRecipesSpider(scrapy.Spider):
    name = 'breakfast_recipes'
    allowed_domains = [
        'allrecipes.com'
    ]

    custom_settings = {
        'FEEDS' : {
            'Breakfast_recipes.csv': {
                'format': 'csv'
            }
        }
    }
    # start_urls = ['https://tasty.co/api/proxy/tasty/feed-page?from=0&size=901&slug=lunch&type=topic']

    def start_requests(self):
        url = 'https://www.allrecipes.com/recipes/78/breakfast-and-brunch/?page={}'

        for i in range(2,143):
            yield scrapy.Request(url.format(i))

    def parse(self, response):
        item = ScrapingrecipesItem()

        allrecipes = response.css('div.component.tout')
        for recipe in allrecipes:
            title = recipe.css('div.tout__imageContainer a::attr(title)').get()
            image = recipe.css('a.tout__imageLink img::attr(src)').get()
            link = 'https://www.allrecipes.com' + recipe.css('div.tout__imageContainer a::attr(href)').get()



            item['title'] = title
            item['image'] = image
            item['link'] = link



            yield item


## DINNER
class DinnerRecipesSpider(scrapy.Spider):
    name = 'Dinner_recipes'
    allowed_domains = [
        'allrecipes.com'
    ]

    custom_settings = {
        'FEEDS' : {
            'Dinner_recipes.csv': {
                'format': 'csv'
            }
        }
    }
    # start_urls = ['https://tasty.co/api/proxy/tasty/feed-page?from=0&size=901&slug=lunch&type=topic']

    def start_requests(self):
        url = 'https://www.allrecipes.com/recipes/17562/dinner/?page={}'

        for i in range(2,385):
            yield scrapy.Request(url.format(i))

    def parse(self, response):
        item = ScrapingrecipesItem()

        allrecipes = response.css('div.component.tout')
        for recipe in allrecipes:
            title = recipe.css('div.tout__imageContainer a::attr(title)').get()
            image = recipe.css('a.tout__imageLink img::attr(src)').get()
            link = 'https://www.allrecipes.com' + recipe.css('div.tout__imageContainer a::attr(href)').get()



            item['title'] = title
            item['image'] = image
            item['link'] = link



            yield item


## DESSERTS
class DessertsRecipesSpider(scrapy.Spider):
    name = 'Dessert_recipes'
    allowed_domains = [
        'allrecipes.com'
    ]

    custom_settings = {
        'FEEDS' : {
            'Desserts_recipes.csv': {
                'format': 'csv'
            }
        }
    }
    # start_urls = ['https://tasty.co/api/proxy/tasty/feed-page?from=0&size=901&slug=lunch&type=topic']

    def start_requests(self):
        url = 'https://www.allrecipes.com/recipes/79/desserts/?page={}'

        for i in range(2,417):
            yield scrapy.Request(url.format(i))

    def parse(self, response):
        item = ScrapingrecipesItem()

        allrecipes = response.css('div.component.tout')
        for recipe in allrecipes:
            title = recipe.css('div.tout__imageContainer a::attr(title)').get()
            image = recipe.css('a.tout__imageLink img::attr(src)').get()
            link = 'https://www.allrecipes.com' + recipe.css('div.tout__imageContainer a::attr(href)').get()



            item['title'] = title
            item['image'] = image
            item['link'] = link



            yield item