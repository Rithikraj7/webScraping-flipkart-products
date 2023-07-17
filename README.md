# Web Scraping Flipkart Product and Appending to Excel Sheet

This Python script scrapes product information from the Flipkart website and appends the scraped data to an Excel sheet.

## Prerequisites

- Python 3.x
- `requests` library
- `beautifulsoup4` library
- `openpyxl` library

## Installation

1. Clone this repository or download the code files.
2. Install the required libraries by running the following command:

## Usage

1. Update the `url` variable in the code with the URL of the Flipkart product page you want to scrape.
2. Make sure you have an existing Excel file (`products.xlsx`) in the same directory as the code. The Excel file should have a sheet named "Sheet" or you can update the sheet name in the code if it differs.
3. Run the script using the following command: `python main.py`
5. The script will scrape the product title, price, and rating from the Flipkart page and append the data as a row to the Excel sheet.
6. The scraped data will be saved in the Excel file.

## Output

The script will print the scraped data on the console, including the title, price, and rating of the product.

## Notes

- If the product title, price, or rating is not found on the Flipkart page, the script will display "Title not found", "Price not found", or "Rating not found" respectively in the output.


