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
image_download = []
headers = ["Title","UPC", "Price Excluding Tax", "Price Including Tax", "Numbers Available", "Category", "Review Rating","product_page_url", "Image URL", "Product Description" ]




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
            csvfile = open(f'{header}.csv', 'w', encoding='utf8', newline='') #open(f'{header}.jpg', 'wb') as imgfile:
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
                #print(page.url)
                soup = BeautifulSoup(page.text, 'lxml')

                #get all the required book info and append to lis
                book_cat = soup.find_all("a")[3].text
                cat.append(book_cat)

                book_upc = soup.find_all("td")[0].text
                upc.append(book_upc)

                price_ex_vat = soup.find_all("td")[2].text
                priceExVat.append(price_ex_vat)

                price_inc_vat = soup.find_all("td")[3].text
                priceIncVat.append(price_inc_vat)

                available = soup.find_all("td")[5].text
                nums_available.append(available)

                book_rating = soup.find("p", class_ = re.compile("star-rating")).get("class")[1]
                rating.append(book_rating)

                cover_url = soup.find("img").get("src")
                image_url.append(cover_url)

                book_desc = soup.find_all("p")[3].text
                desc.append(book_desc)

                urls = page.url
                book_urls.append(urls)

                book_title = soup.find("h1").text
                title.append(book_title)

                title_formated = book_title.replace(' ', '').replace('\'', '').replace(':','')
                img_url  = urljoin(url, cover_url)
                image_page = requests.get(img_url, stream=True)
                imagefile = open(f'{header}_{title_formated}.jpg', 'wb')
                print(title_formated)
                imagefile.write(image_page.content)
                imagefile.close()
                #print(page.url)
                #image_download.append(image_page.content)
                #print(len(image_download))

                #check for page pagination and set next page
            if next_page_element:
                next_page_url = next_page_element.get('href')
                page_url = urljoin(cat_page, next_page_url)
                page = requests.get(page_url)
                soup = BeautifulSoup(page.text, 'lxml')
            else:
                #write data to csv file from data lists
                '''print(len(title))
                print(len(upc))
                print(len(priceExVat))
                print(len(priceIncVat))
                print(len(nums_available))
                print(len(cat))
                print(len(rating))
                print(len(book_urls))
                print(len(image_url))
                print(len(desc))'''


                for i in range(len(title)):
                    #print(i)
                    #print(title)
                    row = [title[i], upc[i], priceExVat[i], priceIncVat[i], nums_available[i], cat[i], rating[i], book_urls[i], image_url[i], desc[i]]

                    writer.writerow(row)


                    #print(image_page.content)
                    #for chunk in image_page.iter_content(chunk_size=8192):
                        #imgfile.write(chunk)
                    #image = image_download[i]
                    #imgfile.write(image)

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
                image_download.clear()

                break




                    #check for pagination and set next page
