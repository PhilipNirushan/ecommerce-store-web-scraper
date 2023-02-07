# Web Scraper for lifemobile.lk
This program is a web scraper for the website lifemobile.lk. It retrieves the information of mobile devices specified in the URL.

### Note:-
This code is just a starting point and you may need to make changes depending on the specific requirements of your project. Additionally, it is important to keep in mind that web scraping can be against a website's terms of service, and it is always best to check the website's policies before scraping their data.

# Getting Started
These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

## Prerequisites
### What things you need to install the software and how to install them:

* Python 3.x
* pip

### Use the package manager pip to install the following libraries:

``` py
pip install requests
pip install beautifulsoup4
pip install openpyxl
```

## Usage
Run the following command to execute the script:

``` py
python main.py
```

The script will scrape the information about the mobile devices, including the device name, price, and description, and store it in a Excel file named Life Mobile Extraction.xlsx. The file will be created in the same directory as the script. The excel file will contain the following details:

* Device Name
* Device Categories
* Stock Availability
* Highlights
* Current Price
* Discount Price
* Colors
* Warranty
* Url of Image

# Built With

* Python
* Requests - HTTP library for Python
* BeautifulSoup - A library for pulling data out of HTML and XML files
* OpenPyXL - A Python library for reading and writing Excel files

# License
This project is licensed under the MIT License - see the LICENSE file for details.







