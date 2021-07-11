from requests_html import HTMLSession

# Load a lightweight brower at the background to fetch the information
# Particular useful for website built by js render

# url = 'https://www.uniqlo.com/au/en/feature/sale/men'
# !! the website for uniqlo => not gonna works but don't know why
url = 'https://www.beerwulf.com/en-gb/c/all-beers?page=1'

# Create a session
s = HTMLSession()

# Create a standard request
r = s.get(url)

# Render the html page
# Setup 1 sec sleeping time so that browser has time to load the whole information
r.html.render(sleep=1)
# print(r.status_code)

# Looking for container for all the single products
# and right clicks on the inspector to get xpath
# Set the first = True, so that if any other xpath returns other object, the results won't be a list
# products = r.html.xpath('//*[@id="root"]/div/div/div[2]/div/div[1]/div[2]/div/div/div/div[7]/div/div[1]/div[3]/div', first = True)
# !! the website for uniqlo => not gonna works but don't know why
products = r.html.xpath('//*[@id="product-items-container"]', first=True)

# for checking purpose, use print(products)
# Use products.absolute_links to get all the links inside of the elements
# These are all the product links
# print(products.absolute_links)

'''
We needed to render() for the main page for the links, not to each product page
'''

# Use each link to get indivusually item
for item in products.absolute_links:
    # get response from each link
    r = s.get(item)
    # Use link to make a request from the js render, then find a classname with .product-detail-info-title in a div ele
    # Then change the result as text
    name = r.html.find('div.product-detail-info-title', first=True).text
    subtext = r.html.find('div.product-subtext', first=True).text
    price = r.html.find('span.price', first=True).text  # Notice here uses span cause it is not div

    try:
        rating = r.html.find('span.label-stars', first=True).text 
    except AttributeError:
        rating = 'none'
        pass

    '''
    A further application, the shopping website has a button called "Add to cart",
    However, if the item is out of stocks, the button is replaced by another class
    In this case, we can use a if statement to check the availiability
    '''
    if r.html.find('div.add-to-cart-container'):
        inStock = True
    else:
        inStock = False

    print(name, subtext, price, "In stock: ", inStock, rating )

