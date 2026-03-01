import requests
import os
from requests.auth import HTTPBasicAuth
from dotenv import load_dotenv


load_dotenv()

SHEETY_PRICE_ENDPOINT = 'https://api.sheety.co/52c3da1c2fbd2c09a015775404a8d078/flightDeals/prices'


class DataManager:
    def __init__(self):
        self._user = os.environ["SHEETY_USERNAME"]
        self._password = os.environ["SHEETY_PASSWORD"]
        self._authorization = HTTPBasicAuth(self._user, self._password)
        self.destination_data = {}

    def get_destination_data(self):
        response = requests.get(url=SHEETY_PRICE_ENDPOINT, auth=self._authorization)
        data = response.json()
        self.destination_data = data["price"]
        return self.destination_data


    def update_destination_code(self):
        for city in self.destination_data:
            new_data = {
                "price": {
                    "iataCode": city["iataCode"]
                }
            }
            response = requests.put(url=f"{SHEETY_PRICE_ENDPOINT}/{city['id']}",
                                    json=new_data,
                                    auth=self._authorization
                                    )
            print(response.text)
            

    
