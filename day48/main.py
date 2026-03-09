from selenium import webdriver
from selenium.webdriver.common.by import By 
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from time import sleep, time


URL = "https://ozh.github.io/cookieclicker/"
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get(URL)

sleep(3)
print("Selecting Language...")
try:
    language_select = driver.find_element(
        By.XPATH,
        "/html/body/div[2]/div[2]/div[12]/div/div[1]/div[1]/div[2]"
    )
    language_select.click()
    print("Selected Language!")
except NoSuchElementException:
    print("Language selection failed")

sleep(2)

cookie = driver.find_element(
    By.XPATH,
    "/html/body/div[2]/div[2]/div[15]/div[8]/button"
)

# collect products
products = []
for i in range(1, 20):
    try:
        product = driver.find_element(
            By.XPATH,
            f"/html/body/div[2]/div[2]/div[19]/div[3]/div[6]/div[{i}]"
        )
        products.append(product)
    except NoSuchElementException:
        break


wait_time = 5
timeout = time() + wait_time
five_min = time() + 60 * 5

while True:

    cookie.click()

    if time() > timeout:
        try:
            cookie_sum = driver.find_element(By.ID, "cookies").text
            cookie_count = int(cookie_sum.split()[0].replace(",", ""))

            best_item = None

            for product in reversed(products):
                if "enabled" in product.get_attribute("class"):
                    best_item = product
                    break

            if best_item:
                best_item.click()
                print(f"Bought item: {best_item.get_attribute('id')}")

        except (NoSuchElementException, ValueError):
            print("Couldnt find cookie count or items")

        timeout = time() + wait_time

    if time() > five_min:
        try:
            cookies_element = driver.find_element(By.ID, "cookies")
            print(f"Final result: {cookies_element.text}")
        except NoSuchElementException:
            print("Couldnt get final cookie count")
        break