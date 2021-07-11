import scrapy 
# Import the item class for fetching data
from wiskyscraper.items import WiskyscraperItem

class wiskySpider(scrapy.Spider):
    name = 'whisky'
    start_urls = ['https://www.whiskyshop.com/scotch-whisky?item_availability=In+Stock']


    def parse(self, response):



        # get all the return item 
        for product in response.css('div.product-item-info'):

            item = WiskyscraperItem()



            # normal funtion in python is return, but scrapy uses 'yield'
            item['name'] = product.css('a.product-item-link::text').get()
            try: 
                item['price'] =  product.css('span.price::text').get().replace('£', ''),
            except :
                item['price']  = None

            item['link'] =  product.css('a.product-item-link').attrib['href']

            yield item

        # find the next page button(element where link to next page), or a way to link to next page
        next_page = response.css('a.action.next').attrib['href']
        if next_page is not None:
            # we are setting if next page is not none, them we move to next page
            # follow the link, then callback and run the self.parse
            yield response.follow(next_page, callback = self.parse)
            

