import requests
from bs4 import BeautifulSoup
import csv
from urllib.parse import urljoin
import re

categories = []
sliced_catgories = []
books = []



#set base url and return the page html content into a soup object
url = "https://books.toscrape.com/"
page = requests.get(url)
soup = BeautifulSoup(page.text, 'lxml')
#get all the categories from the side bar section(linit=53 for max categories)
all_categories = soup.find_all('li', limit = 53)
del all_categories[:3]
#append category urls to list
for i in all_categories:
    links = i.find('a', href=True)
    categories.append(links['href'])

#loop through the category list to join base url to category url and return soup object
for category in categories:
    cat_page = urljoin(url , category)
    page = requests.get(cat_page)
    soup = BeautifulSoup(page.text, 'lxml')
    print("Category: "  + soup.find('h1').text)
    #loop through pages in each category
    for page in category:
        products_urls = [x.div.a.get('href') for x in soup.find_all("article", class_ = "product_pod")]
        next_page_element = soup.select_one('li.next > a')
        #go to each product page in category page
        for book in products_urls:
            prod_page = urljoin(cat_page, book)
            page = requests.get(prod_page)
            soup = BeautifulSoup(page.text, 'lxml')
            print(soup.find("h1").text)
            print(soup.find("p", class_ = re.compile("star-rating")).get("class")[1])


        if next_page_element:
            next_page_url = next_page_element.get('href')
            page_url = urljoin(cat_page, next_page_url)
            page = requests.get(page_url)
            soup = BeautifulSoup(page.text, 'lxml')
            #print(soup.find('h1'))
        else:
            break
