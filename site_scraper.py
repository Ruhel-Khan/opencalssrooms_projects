import requests
from bs4 import BeautifulSoup
import csv
from urllib.parse import urljoin


categories = []
sliced_catgories = []



#set base url and return the page html content into a soup object
url = "https://books.toscrape.com/"
page = requests.get(url)
soup = BeautifulSoup(page.text, 'lxml')
#get all the categories from the side bar section
all_categories = soup.find_all('li', limit = 10)
del all_categories[:3]
#append category urls to list
for i in all_categories:
    links = i.find('a', href=True)
    categories.append(links['href'])


for category in categories:
    cat_page = urljoin(url , category)
    page = requests.get(cat_page)
    soup = BeautifulSoup(page.text, 'lxml')
    #print(soup.find('h1').text)
    #next_page_element = soup.select_one('li.next > a')

    for page in category:
        print(soup.find('h1'))
        next_page_element = soup.select_one('li.next > a')
        if next_page_element:
            next_page_url = next_page_element.get('href')
            page_url = urljoin(cat_page, next_page_url)
            page = requests.get(page_url)
            soup = BeautifulSoup(page.text, 'lxml')
            #print(soup.find('h1'))
        else:
            break
