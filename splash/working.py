import requests
from bs4 import BeautifulSoup as bs

# Noraml way we do for the static website
"""
url = 'https://www.amazon.com.au/s?k=macbook+pro&ref=nb_sb_noss'
r = requests.get(url)
print(r.status_code) # should get a 503 
print(r.text) # the return text shows it is error for robot
"""

url = 'https://www.amazon.com.au/s?k=macbook+pro&ref=nb_sb_noss'
r = requests.get("http://localhost:8050/render.html",
                 params={"url": url, "wait": 2})
# print(r.text)

soup = bs(r.text, 'html.parser')
print(soup.title.text)
