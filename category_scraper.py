import requests
from bs4 import BeautifulSoup
import csv

#set url to scrape
url = 'http://books.toscrape.com/catalogue/category/books/travel_2/index.html'

#get page content
page = requests.get(url)

#parse page content into a soup object
soup = BeautifulSoup(page.content, 'html.parser')

#create lists to store the page items
books = []

#get the product page urls
products_urls = [x.div.a.get('href') for x in soup.findAll("article", class_ = "product_pod")]

#append urls to list
for url in products_urls:
    books.append(url)

#open csv file and write data to file
with open('category.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile, delimiter=',')
    row = books
    writer.writerow(row)
