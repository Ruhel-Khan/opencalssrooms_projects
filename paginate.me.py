import requests
from bs4 import BeautifulSoup
import csv
import time


#loop for pagination range
for x in range(1, 20):

    #set url to scrape
    url = 'https://books.toscrape.com/catalogue/category/books/fiction_10/page-'

    #get page content
    page = requests.get(url+str(x)+".html")

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
    with open('paginate.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile, delimiter=',')
        row = books
        writer.writerow(row)

    #get the next next page button tag
    pager = soup.findAll('ul', class_= "pager")
    next_btn = soup.find('li', class_= "next")

    #set page exception
    if next_btn == None:
        break

    #set a small time delay
    time.sleep(1)
