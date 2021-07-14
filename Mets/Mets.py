from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd
import time


from requests_html import HTMLSession
s = HTMLSession()

# Get a url from a Youtube channel host
# go to video in the profile and sort by popular
url = "https://www.ozmetshub.com.au/Directory/category"

# Assign driver
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get(url)

counter = 1
total_page = 67


for counter in range(total_page):
    try:
        # click the next button to load all the data
        nextButton = driver.find_element_by_class_name(
            'trigger.edNews_loadMoreTrigger')
        nextButton.click()
        print("left pages: {0}-{1}".format(total_page-counter, counter))
        counter += 1
    except:
        pass

    # wait 2 seconds for webpage to load
    time.sleep(2)


Compnaies = driver.find_elements_by_css_selector(
    "#dnn_ctr11256_ViewEasyDNNNewsMain_ctl00_pnlListArticles > div > article")

# Create an empty list
companies_list = []

# extract informaiton from videos
for company in Compnaies:

    # Get a title from main page
    title = company.find_element_by_class_name(
        'edn_articleTitle').text
    summary = company.find_element_by_class_name(
        'edn_articleSummary').text

    # Extract informtaion from main page link
    link = company.find_element_by_link_text(title).get_attribute('href')
    r = s.get(link)

    # request from each company page
    # Try to get the company link if have any
    try:
        linkInfo = list(r.html.find(
            'div.edn_aditionalBox.edn_articleLinks.MemberLinks', first=True).absolute_links)[0]
    except AttributeError:
        linkInfo = None

    # # Try to get a company address if have one
    try:
        addresses = r.html.find(
            'div.ListingAddress', first=True).text
    except AttributeError:
        addresses = None

    # Try to get a company description if have one
    try:
        description = ""
        descriptions = r.html.find('p')
        for i in descriptions:
            description += i.text

    except:
        description = None

    # Try to get a company catagories if have one
    try:
        catagories = r.html.find(
            'div.edn_articleTags.edn_clearFix', first=True).text
    except:
        catagories = None

    print("Title: {0}".format(title))

    # Make use of information and make it as a dictionary
    company_item = {
        'title': title,
        'summary': summary,
        'description': description.replace('CONTACT USGET SOCIAL', '').replace('Improve productivity, reduce life-cycle cost and drive efficiency in your business!', ''),
        'links': linkInfo,
        'addresses': addresses,
        'catagories': catagories,
    }

    # Add the dictionary of the video item in a list
    companies_list.append(company_item)
    print("Item# {0}\n ".format(len(companies_list)))


# Convert the list into a pandas dataframe
print("Making datafiles")
df = pd.DataFrame(companies_list)

# Do for JSON
df.to_json('CompanyData.json', orient="index")
print('Saved to JSON file.')

# Do for CSV
df.to_csv('CompanyData.csv', index=False)
print('Saved to CSV file.')
print(df)
