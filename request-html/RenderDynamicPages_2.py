from requests_html import HTMLSession
import pandas as pd
import time 

'''
# A code that examinate the attributes inside of an object
for item in dir(products):
    print('{0}'.format(item))
'''

s = HTMLSession()
drinklist=[]

def request(url):
    r = s.get(url)
    r.html.render(sleep=1) 
    return r.html.xpath('//*[@id="product-items-container"]', first=True)
     
def parse(products):
    for link in products.absolute_links:
        r = s.get(link)
        title = r.html.find('div.product-detail-info-title', first=True).text
        subtext = r.html.find('div.product-subtext', first=True).text

        try:
            price = r.html.find('span.price', first=True).text
        except AttributeError:
            price= None
            pass
        
        try:
            rating = r.html.find('span.label-stars', first=True).text
        except AttributeError:
            rating = None
            pass

        if r.html.find('div.add-to-cart-container', first=True):
            stock = "In stock"
        else:
            stock = 'Out of stock'
        
        # Create a dictionary 
        drink = {
            'name': title,
            'subtext': subtext,
            'price': price,
            'rating': rating,
            'stock': stock,
        }
        
        drinklist.append(drink)

def output():
    df = pd.DataFrame(drinklist)
    df.to_csv('drinksdemo.csv', index=False) # index = False is for making the index disapear from the csv file  
    print('Saved to CSV file.')


# define the first page 
pageNumber = 1

while True:
    # Check page numner if page found (return NoneType), break the loop otherwise
    try:
        products = request('https://www.beerwulf.com/en-gb/c/all-beers?page={0}'.format(pageNumber)) 
        print('Getting items from page {0}...'.format(pageNumber))
        parse(products)
        print('Total items: ', len(drinklist))

        pageNumber += 1
        time.sleep(2) # Give 2 seconds break when sending request to the server
    except:
        print('No more items!')
        break

output() 

