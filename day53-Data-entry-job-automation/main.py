from bs4 import BeautifulSoup
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By 
import time
import os
from selenium.webdriver.common.keys import Keys
from dotenv import load_dotenv


load_dotenv(override=True)

FORM_LINK = os.getenv("SHEET_DAY53")
URL = "https://appbrewery.github.io/Zillow-Clone/"
headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 13_5) AppleWebKit/537.36 "
                  "(KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.9",
    "Accept-Encoding": "gzip, deflate, br",
    "Connection": "keep-alive"
}

response = requests.get(URL, headers=headers)

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


chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)
driver.get(FORM_LINK)

for i in range(len(link_list)):
    time.sleep(3)
    first = driver.find_element(By.XPATH,"/html/body/div/div[2]/form/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input")
    first.send_keys(address_list[i])

    second = driver.find_element(By.XPATH, "/html/body/div/div[2]/form/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input")
    second.send_keys(price_list[i])

    third = driver.find_element(By.XPATH, "/html/body/div/div[2]/form/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input")
    third.send_keys(link_list[i])

    submit = driver.find_element(By.XPATH, "/html/body/div/div[2]/form/div[2]/div/div[3]/div[1]/div[1]/div/span/span")
    submit.click()
  