import json
import scrapy
from ..items import ScrapingrecipesItem

# LUNCH
class FoodNetworkRecipesSpider(scrapy.Spider):
    name = 'foodnetwork_recipes'
    allowed_domains = [
        'foodnetwork.co.uk'
    ]
    start_urls = ['https://foodnetwork.co.uk/lunch-recipes/']

    custom_settings = {
        'FEEDS': {
            'Lunch_recipes.csv': {
                'format': 'csv'
            }
        }
    }

    def parse(self, response):
        item = ScrapingrecipesItem()

        allrecipes = response.css('div.card.queen.picture.recipepage.collectionItemBlock')

        for recipe in allrecipes:
            title = recipe.css('div.card.queen.picture.recipepage.collectionItemBlock a::attr(title)').get()
            image = recipe.css('div.card.queen.picture.recipepage.collectionItemBlock::attr("data-backgroundimage")').get()
            link = 'https://foodnetwork.co.uk' + recipe.css('div.card.queen.picture.recipepage.collectionItemBlock a::attr(href)').get()



            item['title'] = title
            item['image'] = image
            item['link'] = link


            yield item


## DINNER
class DinnerFoodNetworkRecipesSpider(scrapy.Spider):
    name = 'foodnetwork_recipes_dinner'
    allowed_domains = [
        'foodnetwork.co.uk'
    ]
    start_urls = ['https://foodnetwork.co.uk/dinner-recipes/']

    custom_settings = {
        'FEEDS': {
            'Dinner_recipes.csv': {
                'format': 'csv'
            }
        }
    }

    def parse(self, response):
        item = ScrapingrecipesItem()

        allrecipes = response.css('div.card.queen.picture.recipepage.collectionItemBlock')

        for recipe in allrecipes:
            title = recipe.css('div.card.queen.picture.recipepage.collectionItemBlock a::attr(title)').get()
            image = recipe.css('div.card.queen.picture.recipepage.collectionItemBlock::attr("data-backgroundimage")').get()
            link = 'https://foodnetwork.co.uk' + recipe.css('div.card.queen.picture.recipepage.collectionItemBlock a::attr(href)').get()



            item['title'] = title
            item['image'] = image
            item['link'] = link


            yield item




## DESSERTS
class DessertsFoodNetworkRecipesSpider(scrapy.Spider):
    name = 'foodnetwork_recipes_desserts'
    allowed_domains = [
        'foodnetwork.co.uk'
    ]
    start_urls = ['https://foodnetwork.co.uk/dessert-recipes/']

    custom_settings = {
        'FEEDS': {
            'Desserts_recipes.csv': {
                'format': 'csv'
            }
        }
    }

    def parse(self, response):
        item = ScrapingrecipesItem()

        allrecipes = response.css('div.card.queen.picture.recipepage.collectionItemBlock')

        for recipe in allrecipes:
            title = recipe.css('div.card.queen.picture.recipepage.collectionItemBlock a::attr(title)').get()
            image = recipe.css('div.card.queen.picture.recipepage.collectionItemBlock::attr("data-backgroundimage")').get()
            link = 'https://foodnetwork.co.uk' + recipe.css('div.card.queen.picture.recipepage.collectionItemBlock a::attr(href)').get()



            item['title'] = title
            item['image'] = image
            item['link'] = link


            yield item

