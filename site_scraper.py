''' this program scrapes data from every product page on bookstoscrape website.
It will not work on any other site unless the html markup is exactly the same.'''
import requests
from bs4 import BeautifulSoup
import csv
from urllib.parse import urljoin
import re

categories = []

title = []
cat = []
upc = []
priceExVat = []
priceIncVat = []
nums_available = []
rating = []
image_url = []
desc = []
book_urls = []
headers = ["Title","UPC", "Price Excluding Tax", "Price Including Tax", "Numbers Available", "Category", "Review Rating","product_page_url", "Image URL", "Product Description" ]

def remove_non_ascii(string):
    encoded_string = string.encode("ascii", "ignore")
    decode_string = encoded_string.decode()
    return decode_string
def format_title(book_title):
    #format book titles for use as filename for image files
    title_formated = [character for character in book_title if character.isalnum()]
    title_formated = "".join(title_formated)
    return title_formated

#set base url and return the page html content into a soup object
url = "https://books.toscrape.com/"
page = requests.get(url)
soup = BeautifulSoup(page.text, 'lxml')
#get all the categories from the side bar section(linit=53 for max categories)
all_categories = soup.find_all('li', limit = 5)
del all_categories[:3]
#append category urls to list
for i in all_categories:
    links = i.find('a', href=True)
    categories.append(links['href'])

#loop through the category list to join base url to category url and return soup object
for category in categories:
    cat_page = urljoin(url, category)
    page = requests.get(cat_page)
    soup = BeautifulSoup(page.text, 'lxml')
    header = soup.find('h1').text
    #loop through pages in each category
    for page in category:
        #open csv files with current category as the filename and write file headers
            csvfile = open(f'{header}.csv', 'w', encoding='utf8', newline='')
            writer = csv.writer(csvfile, delimiter=',')
            writer.writerow(headers)
            #get all the book urls on page
            products_urls = [x.div.a.get('href') for x in soup.find_all("article", class_ = "product_pod")]
            #find the element for the next page button
            next_page_element = soup.select_one('li.next > a')
            #go to each book page in category page
            for book in products_urls:
                prod_page = urljoin(cat_page, book)
                page = requests.get(prod_page)
                soup = BeautifulSoup(page.text, 'lxml')
                #get all the required book info and append to lis
                cat.append(remove_non_ascii(soup.find_all("a")[3].text))
                upc.append(remove_non_ascii(soup.find_all("td")[0].text))
                priceExVat.append(remove_non_ascii(soup.find_all("td")[2].text))
                priceIncVat.append(remove_non_ascii(soup.find_all("td")[3].text))
                nums_available.append(soup.find_all("td")[5].text)
                rating.append(soup.find("p", class_ = re.compile("star-rating")).get("class")[1])
                cover_url = soup.find("img").get("src")
                image_url.append(cover_url)
                desc.append(remove_non_ascii(soup.find_all("p")[3].text))
                book_urls.append(page.url)
                book_title = remove_non_ascii(soup.find("h1").text)
                title.append(book_title)
                #download the image
                img_url  = urljoin(url, cover_url)
                image_page = requests.get(img_url, stream=True)
                #open image files and write byte data to files
                imagefile = open(f'{header}_{format_title(book_title)}.jpg', 'wb')
                imagefile.write(image_page.content)
                imagefile.close()
                #check for page pagination and set next page
            if next_page_element:
                next_page_url = next_page_element.get('href')
                page_url = urljoin(cat_page, next_page_url)
                page = requests.get(page_url)
                soup = BeautifulSoup(page.text, 'lxml')
            else:
                for i in range(len(title)):
                    row = [title[i], upc[i], priceExVat[i], priceIncVat[i], nums_available[i], cat[i], rating[i], book_urls[i], image_url[i], desc[i]]
                    writer.writerow(row)
                #empty all the lists for next category
                csvfile.close()
                title.clear()
                upc.clear()
                priceExVat.clear()
                priceIncVat.clear()
                nums_available.clear()
                cat.clear()
                rating.clear()
                book_urls.clear()
                image_url.clear()
                desc.clear()
                break
