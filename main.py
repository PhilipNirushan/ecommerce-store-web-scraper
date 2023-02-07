# import libraries
import requests
import openpyxl
from bs4 import BeautifulSoup

# Create a new Excel file
excel = openpyxl.Workbook()
# Make the sheet as active - To load the data into that sheet
sheet = excel.active
# Giving name to the sheet
sheet.title = 'Life Mobile Extraction'
# Giving column names
sheet.append(
    ['Categories', 'Name', 'Availability', 'Highlights', 'Discount', 'Price', 'Color', 'Warranty', 'Url-of-Image'])


def find_devices():
    # Using the Requests Library to see a Website's HTML
    html_text = requests.get("https://lifemobile.lk/product-category/unit-only-devices/").text
    soup = BeautifulSoup(html_text, 'html.parser')
    cards = soup.find_all('div', class_="product-inner product-item__inner")
    # Looping through device objects
    for card in cards:
        # Getting the url of device's single page
        link = card.find('a', class_="woocommerce-LoopProduct-link woocommerce-loop-product__link")['href']
        # Using the Requests Library to see a Website's HTML
        source = requests.get(link).text
        source_soup = BeautifulSoup(source, 'html.parser')
        device = source_soup.find('div', class_="single-product-wrapper row")
        # Getting Categories of the device
        categories = device.find('span', class_="loop-product-categories").text
        # Getting Name of the device
        name = device.find('h1', class_="product_title entry-title").text.split('(')[0]
        # Getting Stock details
        availability = device.find('span', class_="electro-stock-availability").text
        # Getting information of Highlights in HTML Format
        highlights = device.find('div', class_="woocommerce-product-details__short-description").ul
        # Encoding the highlights because we cannot convert html values into Excel
        encoded_highlights = highlights.encode('unicode_escape')
        # Getting Discount and Price
        amounts = device.find_all('span', class_="woocommerce-Price-amount amount")
        if len(amounts) == 2:
            discount = amounts[0].text
            price = amounts[1].text
        else:
            discount = None
            price = amounts[0].text
        # Getting Colors
        color_list = []
        select_tag_for_color = device.find('select', id="pa_colour")
        color_opinions = select_tag_for_color.find_all('option')
        for color_opinion in color_opinions[1:]:
            color_list.append(color_opinion.text)
        # Storing color_list values into string called 'color' because we can convert list values into Excel
        color = ', '.join(color_list)
        # Getting Warranty
        warranty_list = []
        select_tag_for_warranty = device.find('select', id="pa_select-warranty")
        warranty_opinions = select_tag_for_warranty.find_all('option')
        for warranty_opinion in warranty_opinions[1:]:
            warranty_list.append(warranty_opinion.text)
        # Storing warranty_list values into string called 'warranty' because we can convert list values into Excel
        warranty = ', '.join(warranty_list)
        # Getting Url of the image
        image_link = device.find('a')['href']
        # Saving all the data into particular columns accordingly
        sheet.append([categories, name, availability, encoded_highlights, discount, price, color, warranty, image_link])
    # To save Excel file
    excel.save('Life Mobile Extraction.xlsx')
    print(f'File Saved')


if __name__ == "__main__":
    find_devices()

