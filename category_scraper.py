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
header = []
#target outer tag
list_items = soup.find_all('article', class_='product_pod')

#loop through to find inner tag and append to list
for item in list_items:
    link = list_items.find('a').get('href')
    print(link)    #books.append(link)
'''
#open csv file and write data to file
with open('category.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile, delimiter=',')
    writer.writerow(header)
    row = books
    writer.writerow(row)
'''
