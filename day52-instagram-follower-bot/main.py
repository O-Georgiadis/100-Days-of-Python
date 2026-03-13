from selenium import webdriver
from selenium.webdriver.common.by import By 
import time
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import ElementClickInterceptedException
import os
from dotenv import load_dotenv

load_dotenv(override=True)

TARGET_ACCOUNT = ""
USERNAME = os.getenv("EMAIL_ADDRESS_DAY52")
PASSWORD = os.getenv("PASSWORD_DAY52")


class InstaFollower:
    def __init__(self):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(options=chrome_options)
        
        

    def login(self):
        URL = "https://www.instagram.com/accounts/login"
        self.driver.get(URL)
        self.cookies = self.driver.find_element(By.XPATH,"/html/body/div[3]/div[1]/div/div[2]/div/div/div/div/div[2]/div/button[2]")
        self.cookies.click()        
        time.sleep(3)
        username = self.driver.find_element(By.NAME, "username")
        username.send_keys(USERNAME)
        password = self.driver.find_element(By.NAME, "password")
        password.send_keys(PASSWORD)
        password.send_keys(Keys.ENTER)

        time.sleep(3)
        save_login_prompt = self.driver.find_element(By.XPATH, value="//div[contains(text(), 'Not now')]")
        try:
            save_login_prompt = self.driver.find_element(By.XPATH, "//button[contains(text(),'Not Now')]")
            save_login_prompt.click()
        except:
            pass

        time.sleep(4)

        notifications = self.driver.find_element(By.XPATH, value="//button[contains(text(), 'Not Now')]")
        if notifications:
            notifications.click()


    
    def find_followers(self):
        time.sleep(5)
        self.driver.get(f"https://www.instagram.com/{TARGET_ACCOUNT}/followers")
        time.sleep(10)
        modal = self.driver.find_element(By.XPATH, "/html/body/div[6]/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[2]")
        for i in range(10):
            self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", modal)
            time.sleep(2)


    def follow(self):
        all_buttons = self.driver.find_elements(By.CSS_SELECTOR, value='._aano button')

        for button in all_buttons:
            try:
                button.click()
                time.sleep(1.1)

            except ElementClickInterceptedException:
                cancel_button = self.driver.find_element(By.XPATH, "//button[contains(text(), 'Cancel')]")
                cancel_button.click()


bot = InstaFollower()
bot.login()
bot.find_followers()
bot.follow()
