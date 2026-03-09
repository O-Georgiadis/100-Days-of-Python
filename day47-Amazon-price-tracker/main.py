import requests
from bs4 import BeautifulSoup
import os
from dotenv import load_dotenv
import smtplib

load_dotenv(override=True)

# URL = "https://appbrewery.github.io/instant_pot/"
URL = "https://www.amazon.com/dp/B075CYMYK6?psc=1&ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6"
SMTP_ADDRESS = os.getenv("SMTP_ADDRESS_DAY47")
EMAIL_ADDRESS= os.getenv("EMAIL_ADDRESS_DAY47")
EMAIL_PASSWORD = os.getenv("EMAIL_PASSWORD_DAY47")
BUY_PRICE = 100

headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 13_5) AppleWebKit/537.36 "
                  "(KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.9",
    "Accept-Encoding": "gzip, deflate, br",
    "Connection": "keep-alive"
}

response = requests.get(URL, headers=headers)

# print(response.status_code)
# print(response.text[:2000])

soup = BeautifulSoup(response.text, "html.parser")
price_element = soup.find(class_="a-offscreen")

if price_element:
    price = price_element.get_text().split("EUR")
    final_price = float(price[1])
else:
    print("Amazon blocked the request.")
    exit()

title_broken = soup.find(id="productTitle").get_text().strip()
title = "".join(title_broken)

#======================= Send Email =====================================
if final_price <= BUY_PRICE:
    message = f"{title} is on sale for {final_price}"

    with smtplib.SMTP(SMTP_ADDRESS, port=587) as connection:
        connection.starttls()
        result = connection.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
        connection.sendmail(
            from_addr=EMAIL_ADDRESS,
            to_addrs=EMAIL_ADDRESS,
            msg=f"Subject:Amazon Price Alert!\n\n{message}\n{URL}".encode("utf-8")
        )