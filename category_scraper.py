''' this program scrapes data from an category page on bookstoscrape website.
It will not work on any other site unless the html markup is exactly the same.'''
#import required modules
import requests
from bs4 import BeautifulSoup
import csv

#create lists to store the page items
books = []

#set url to scrape
url = "http://books.toscrape.com/catalogue/category/books/travel_2/index.html"
#parse html into a beautifulSoup object
def get_soup(url):
    #get page content
    page = requests.get(url)
    #parse page content into a soup object
    soup = BeautifulSoup(page.content, 'html.parser')
    return soup
soup = get_soup(url)

 #get all the product urls
def product_urls(soup):
    list_items = soup.find_all('article', 'product_pod')
    for item in list_items:
        link = item.find('a').get('href')
        books.append(link)
product_urls(soup)

#write to csv file
def write_to_csv():
    with open('category.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile, delimiter=',')
        row = books
        writer.writerow(row)
write_to_csv()
