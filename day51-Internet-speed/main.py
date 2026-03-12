from selenium import webdriver
from selenium.webdriver.common.by import By 
import time


URL = "https://www.speedtest.net/"


class InternetSpeedTwitterBot:
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.upload_speed = 0
        self.download_speed = 0
        


    def get_internet_speed(self):
        self.driver.get(URL)
        time.sleep(3)

        go_button = self.driver.find_element(By.XPATH,"/html/body/div[3]/div[1]/div[3]/div/div/div/div[2]/div[2]/div/div[2]/a/span[4]")
        go_button.click()
        time.sleep(40)

        self.download_speed = self.driver.find_element(By.XPATH,"/html/body/div[3]/div[1]/div[3]/div/div/div/div[2]/div[2]/div/div[4]/div/div[3]/div/div/div[2]/div[1]/div[1]/div/div[2]/span").text
        self.upload_speed = self.driver.find_element(By.XPATH,"/html/body/div[3]/div[1]/div[3]/div/div/div/div[2]/div[2]/div/div[4]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span").text
        print(f"Download speed: {self.download_speed}, Upload_speed: {self.upload_speed}")


    def tweet_at_provider(self):
        # Dont have, or want Twitter account
        pass


bot = InternetSpeedTwitterBot()
bot.get_internet_speed()
bot.tweet_at_provider()