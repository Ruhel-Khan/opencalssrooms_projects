import requests
from bs4 import BeautifulSoup
import csv


#url to scrape
url = 'http://books.toscrape.com/catalogue/vagabonding-an-uncommon-guide-to-the-art-of-long-term-world-travel_552/index.html'

#get page content
page = requests.get(url)
# print(page.content)

#parse page content into a soup object
soup = BeautifulSoup(page.content, 'html.parser')
#print(soup)

#get product page url
product_page_url = url
#get all the info in the html table
info_table = soup.find("table", class_="table table-striped")

print(info_table.text.strip())

#loop through the table data

for i in info_table.find_all('tbody'):
    rows = i.find_all('tr')
    for row in rows:
        data = row.find('td')
        print(data)
