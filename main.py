#import required modules

import requests
from bs4 import BeautifulSoup
import csv
from urllib.parse import urljoin
import re


#url to scrape
url = 'http://books.toscrape.com/catalogue/vagabonding-an-uncommon-guide-to-the-art-of-long-term-world-travel_552/index.html'

#get page content
def get_page_content(url):
    page = requests.get(url)
    return page
#print(get_page_content(url).text)

#parse page content into a soup object
html = get_page_content(url)
def get_bs_object(html):
    soup = BeautifulSoup(page.content, 'html.parser')
    return soup

print(get_bs_object(html).text)

def get_table(soup):
    table_data = soup.find_all("td")
    return table_data
