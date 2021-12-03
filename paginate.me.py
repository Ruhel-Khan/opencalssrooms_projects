#imort required modules
import requests
from bs4 import BeautifulSoup
import csv
from urllib.parse import urljoin

#set url to scrape
url = 'https://books.toscrape.com/catalogue/category/books/sequential-art_5/index.html'
#get all the urls on a page
def product_urls(soup):
    list_items = soup.find_all('article', 'product_pod')
    for item in list_items:
        link = item.find('a').get('href')
        books.append(link)
#create lists to store the page items
books = []
#write to csv file
def write_to_csv():
    with open('paginate.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile, delimiter=',')
        row = books
        writer.writerow(row)

while True:
    #parse html into a beautifulSoup object
    page = requests.get(url)
    #parse page content into a soup object
    soup = BeautifulSoup(page.content, 'html.parser')
    product_urls(soup)
    #pagination
    next_page_element = soup.select_one('li.next > a')
    if next_page_element:
        next_page_url = next_page_element.get('href')
        url = urljoin(url, next_page_url)
    else:
        break
write_to_csv()
