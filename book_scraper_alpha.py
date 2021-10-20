import requests
from bs4 import BeautifulSoup
import csv
import re


#url to scrape
url = 'http://books.toscrape.com/catalogue/vagabonding-an-uncommon-guide-to-the-art-of-long-term-world-travel_552/index.html'

#get page content
page = requests.get(url)
# print(page.content)

#parse page content into a soup object
soup = BeautifulSoup(page.content, 'html.parser')
#print(soup)

#create a list of all the headers
headers = ["Title","UPC", "Price Excluding Tax", "Price Including Tax", "Numbers Available", "Category", "Review Rating","product_page_url", "Image URL", "Product Description" ]
#create a list of all the extracted data
data = []

#append title to data list
data.append(soup.find("h1").text)

#get all the table table_data
table_data = soup.find_all("td")

#append all the table data into the data list
for i in table_data:
    if ((i.text == "Books") or (i.text == "£0.00") or (i.text == "0")):
        continue
    data.append(i.text)

#get the book category
category = soup.find_all("a")
data.append(category[3].text)

#get the book ratings
data.append(soup.find("p", class_ = re.compile("star-rating")).get("class")[1])

#append url to data list
data.append(url)

#get the image URL
data.append(soup.find("img").get("src"))

#get the product Description
product_desc = soup.find_all("p")
data.append(product_desc[3].text)


#Save titles and descriptions as lists of strings
'''
titles = []
for title in bs_titles:
	titles.append(title.string)

descriptions = []
for desc in bs_descriptions:
	descriptions.append(desc.string)

# write data to a csv file
headers = ["title", "description"]

with open('data.csv', 'w', newline='') as csvfile:
	writer = csv.writer(csvfile, delimiter=',')
	writer.writerow(headers)
	for i in range(len(titles)):
		row = [titles[i], descriptions[i]]
		writer.writerow(row)
'''


#open csv file and write data to file
with open('data.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile, delimiter=',')
    writer.writerow(headers)
    row = data
    writer.writerow(row)



print(data)
