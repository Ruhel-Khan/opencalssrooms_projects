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

#create a list of all the headers
headers = ["Product Page URL", "UPC", "Title", "Price Including Tax", "Price Excluding Tax", "Numbers Available", "Product Description", "Category", "Review Rating", "Image URL" ]
#create a list of all the extracted data
data = []

#get product page url
product_page_url = url
data.append(product_page_url)
#print("Product Page URL: ", product_page_url)

#get all the info in the html table
info_table = soup.find("table", class_="table table-striped")

#print(info_table.text)

#loop through table data
for i in info_table.find_all('tbody'):
    rows = i.find_all('tr')
    data = row.find('td')
    for row in rows:
        print(row)

#get book book_title#
book_title = soup.find("h1")
print("Book Title: ", book_title.text.strip())

#get book description
product_desc = soup.find_all("p")
print("Product Description: ", product_desc[3].text)

#get the image url
image_url = soup.find_all("img")
image = image_url[0]
print("Image URL: ", image.attrs['src'])

#get the book category
category = soup.find_all("a")
print("Category: ", category[3].text)
