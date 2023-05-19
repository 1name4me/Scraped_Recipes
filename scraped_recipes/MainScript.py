from scrapy.utils.log import configure_logging
from twisted.internet import reactor, defer

## LUNCH
# from scrapingRecipes.spiders.recipes import RecipesSpider
# from scrapingRecipes.spiders.recipes_Tasty import TastyRecipesSpider
# from scrapingRecipes.spiders.recipes_foodnetwork import FoodNetworkRecipesSpider

## BREAKFAST
# from scrapingRecipes.spiders.recipes import BreakfastRecipesSpider
# from scrapingRecipes.spiders.recipes_Tasty import BreakfastTastyRecipesSpider


## DINNER
# from scrapingRecipes.spiders.recipes import DinnerRecipesSpider
# from scrapingRecipes.spiders.recipes_Tasty import DinnerTastyRecipesSpider
# from scrapingRecipes.spiders.recipes_foodnetwork import DinnerFoodNetworkRecipesSpider

## DESSERTS
from scrapingRecipes.spiders.recipes import DessertsRecipesSpider
from scrapingRecipes.spiders.recipes_Tasty import DessertsTastyRecipesSpider
from scrapingRecipes.spiders.recipes_foodnetwork import DessertsFoodNetworkRecipesSpider

from scrapy.crawler import CrawlerRunner


def main():
    # process = CrawlerProcess()
    # process.crawl(RecipesSpider)
    # process.crawl(TastyRecipesSpider)
    # process.crawl(FoodNetworkRecipesSpider)
    # process.start()

    configure_logging()
    runner = CrawlerRunner()

    # Run one spider at a time
    #LUNCH

    # @defer.inlineCallbacks
    # def crawl():
    #     yield runner.crawl(RecipesSpider)
    #     yield runner.crawl(TastyRecipesSpider)
    #     yield runner.crawl(FoodNetworkRecipesSpider)
    #     reactor.stop()
    #
    # crawl()
    # reactor.run()


    # BREAKFAST
    # @defer.inlineCallbacks
    # def crawl():
    #     yield runner.crawl(BreakfastRecipesSpider)
    #     yield runner.crawl(BreakfastTastyRecipesSpider)
    #     reactor.stop()


    #DINNER
    # @defer.inlineCallbacks
    # def crawl():
    #     yield runner.crawl(DinnerRecipesSpider)
    #     yield runner.crawl(DinnerTastyRecipesSpider)
    #     yield runner.crawl(DinnerFoodNetworkRecipesSpider)
    #     reactor.stop()


    #DESSERTS
    @defer.inlineCallbacks
    def crawl():
        yield runner.crawl(DessertsRecipesSpider)
        yield runner.crawl(DessertsTastyRecipesSpider)
        yield runner.crawl(DessertsFoodNetworkRecipesSpider)
        reactor.stop()

    crawl()
    reactor.run()

#
if __name__ == '__main__':
    main()