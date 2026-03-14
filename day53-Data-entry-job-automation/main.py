from bs4 import BeautifulSoup
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By 
import time
import os
from dotenv import load_dotenv


load_dotenv(override=True)

FORM_LINK = os.getenv("SHEET_DAY53")
URL = "https://appbrewery.github.io/Zillow-Clone/"

response = requests.get(URL)
web_page = response.text

soup = BeautifulSoup(web_page, "html.parser")

# Home prices
prices = soup.find_all(class_="PropertyCardWrapper__StyledPriceLine")
price_list = []
for price in prices:
    text = price.getText()
    clean_price = text.split("+")[0]
    even_cleaner_price = clean_price.split("/")[0]
    price_list.append(even_cleaner_price)

print(price_list)

# Address

addresses = soup.find_all(class_="StyledPropertyCardDataArea-anchor")
address_list = [address.getText().strip() for address in addresses]
print(address_list)

# Home links
links = soup.find_all(class_="StyledPropertyCardDataArea-anchor")
link_list = [link.get("href") for link in links]
print(link_list)


