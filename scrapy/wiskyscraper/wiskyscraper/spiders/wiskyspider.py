import scrapy 
# Import the item class for fetching data
from wiskyscraper.items import WiskyscraperItem
from scrapy.loader import ItemLoader

class wiskySpider(scrapy.Spider):
    name = 'whisky'
    start_urls = ['https://www.whiskyshop.com/scotch-whisky?item_availability=In+Stock']


    def parse(self, response):



        # get all the return item 
        for product in response.css('div.product-item-info'):

            # 1. selector ('product') select the item from the html and send it to itemloader
            # 2. the item loader use wiskyscrapperItem() and send the data to item clean
            # ==> means we create a item loader, this is my item and this is my selector, go and grab the data for me
            l = ItemLoader(item = WiskyscraperItem(), selector = product)
            
            l.add_css('name', 'a.product-item-link')
            l.add_css('price', 'span.price')
            l.add_css('link', 'a.product-item-link::attr(href)' )

            yield l.load_item()

        # find the next page button(element where link to next page), or a way to link to next page
        next_page = response.css('a.action.next').attrib['href']
        if next_page is not None:
            # we are setting if next page is not none, them we move to next page
            # follow the link, then callback and run the self.parse
            yield response.follow(next_page, callback = self.parse)
            

