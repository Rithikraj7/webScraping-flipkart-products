import requests
from bs4 import BeautifulSoup
import openpyxl

# URL of the Flipkart product page to scrape
base_url = 'https://www.flipkart.com/search?q=laptop&sid=6bo%2Cb5g&as=on&as-show=on&otracker=AS_QueryStore_OrganicAutoSuggest_1_3_na_na_na&otracker1=AS_QueryStore_OrganicAutoSuggest_1_3_na_na_na&as-pos=1&as-type=RECENT&suggestionId=laptop%7CLaptops&requestId=5f2ba74a-582f-4447-921b-2cb1cbf93b38&as-searchtext=lap'

# Number of pages to scrape
num_pages = 3

# Create an empty list to store the scraped data
data = []

# Loop through the pages
for page in range(1, num_pages + 1):
    # Construct the URL for each page
    url = base_url + '&page=' + str(page)

    # Send a GET request to the URL
    response = requests.get(url)

    # Create a BeautifulSoup object to parse the HTML content
    soup = BeautifulSoup(response.content, 'html.parser')

    # Find the product details on the page
    product_elements = soup.find_all('div', class_='_1AtVbE')

    # Extract the required data from each product element
    for product_element in product_elements:
        title_element = product_element.find('a', class_='_1fQZEK')
        if title_element is not None:
            title = title_element.text.strip()
        else:
            title = 'Title not found'

        price_element = product_element.find('div', class_='_1_WHN1')
        if price_element is not None:
            price = price_element.text.strip()
        else:
            price = 'Price not found'

        rating_element = product_element.find('div', class_='_3LWZlK')
        if rating_element is not None:
            rating = rating_element.text.strip()
        else:
            rating = 'Rating not found'

        # Append the data to the list
        data.append([title, price, rating])

# Append the scraped data to an Excel file
workbook = openpyxl.load_workbook('C:/Users/dilip/PycharmProjects/pythonProjectgit3/products.xlsx')
sheet = workbook.active

for row in data:
    sheet.append(row)

workbook.save('C:/Users/dilip/PycharmProjects/pythonProjectgit3/products.xlsx')

# Print the output
for i, row in enumerate(data, start=1):
    print(f"Product {i}:")
    print("Title:", row[0])
    print("Price:", row[1])
    print("Rating:", row[2])
    print("------------------")
