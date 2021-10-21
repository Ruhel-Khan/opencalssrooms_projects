import requests
from bs4 import BeautifulSoup
import csv

#set url to scrape
url = 'http://books.toscrape.com/catalogue/category/books/travel_2/index.html'

#get page content
page = requests.get(url)

#parse page content into a soup object
soup = BeautifulSoup(page.content, 'html.parser')

#create a list to store the page items
books = []

#target outer tag
list_items = soup.find_all('article', class_='product_pod')

#loop through to find inner tag and append to list
for item in list_items:
    link = soup.find('a').get('href')
    books.append(link)
