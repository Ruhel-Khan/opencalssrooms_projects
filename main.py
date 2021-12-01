#import required modules

import requests
from bs4 import BeautifulSoup
import csv
import re

headers = ["Title","UPC", "Price Excluding Tax", "Price Including Tax", "Numbers Available", "Category", "Review Rating","product_page_url", "Image URL", "Product Description" ]
title = []
cat = []
upc = []
priceExVat = []
priceIncVat = []
nums_available = []
rating = []
image_url = []
desc = []
book_url = []
data = [title, upc, priceExVat, priceExVat, nums_available, cat, rating,book_url, image_url, desc]
#url to scrape
url = 'http://books.toscrape.com/catalogue/vagabonding-an-uncommon-guide-to-the-art-of-long-term-world-travel_552/index.html'

#get page content
def get_page_content(url):
    page = requests.get(url)
    return page
#print(get_page_content(url).text)

#return a BeautifulSoup get_bs_object
def get_soup(page):
    soup = BeautifulSoup(page.content, 'lxml')
    return soup
soup = get_soup(get_page_content(url))

#get all the table table_data
def get_table(soup):
    upc.append(soup.find_all("td")[0].text)
    priceExVat.append(soup.find_all("td")[2].text)
    priceIncVat.append(soup.find_all("td")[3].text)
    nums_available.append(soup.find_all("td")[5].text)

#get all the rest of the book data
def get_data(soup):
    cat.append(soup.find_all("a")[3].text)
    rating.append(soup.find("p", class_ = re.compile("star-rating")).get("class")[1])
    image_url.append(soup.find("img").get("src"))
    book_url.append(get_page_content(url).url)
    title.append(soup.find("h1").text)
    desc.append(soup.find_all("p")[3].text)

get_table(soup)
get_data(soup)

#write data to csv file
def write_to_csv(headers):
    with open('data.csv', 'w',encoding = 'utf8', newline='') as csvfile:
        writer = csv.writer(csvfile, delimiter=',')
        writer.writerow(headers)
        for i in range(len(title)):
            row = [title[i], upc[i], priceExVat[i], priceIncVat[i], nums_available[i], cat[i], rating[i], book_url[i], image_url[i], desc[i]]
            writer.writerow(row)
write_to_csv(headers)
