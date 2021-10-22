import requests
from bs4 import BeautifulSoup
import csv
import time

#create empty lists for all the site information
category = []
product_url = []
title = []
upc =
price_inc_tax = []
price_ex_tax = []
numbers_available = []
review_rating = []
image_url = []
description = []

#loop for pagination range
for x in range(1, 100):
    print("scraping page.."+str(x))

    #set url to scrape
    url = 'https://books.toscrape.com/catalogue/page-'

    #get page content
    page = requests.get(url+str(x)+".html")

    #parse page content into a soup object
    soup = BeautifulSoup(page.content, 'html.parser')

    #get the product page urls
    products_urls = [x.div.a.get('href') for x in soup.findAll("article", class_ = "product_pod")]

    #append urls to list
    for url in products_urls:
        product_url.append(url)

    #open csv file and write data to file
    with open('site.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile, delimiter=',')
        row = books
        writer.writerow(row)

    #get the next next page button tag
    pager = soup.findAll('ul', class_= "pager")
    next_btn = soup.find('li', class_= "next")

    #set page exception
    if next_btn == None:
        print(str(x-1)+" " + "Pages scraped")
        break

    #set a small time delay
    time.sleep(1)
