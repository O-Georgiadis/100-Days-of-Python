import requests
from twilio.rest import Client
import os


MY_LAT = 38.000259
MY_LONG = 23.797831
MY_NUMBER = +306911111111

api_key = os.environ.get("OWM_API_KEY")
account_sid = os.environ.get("TWILIO_SID")
auth_token = os.environ.get("OWM_AUTH_TOKEN")


parameters = {
        "lat": MY_LAT,
        "lon": MY_LONG,
        "appid": api_key,
        "cnt": 4,
    }
response = requests.get(url='http://api.openweathermap.org/data/2.5/forecast', params=parameters)
response.raise_for_status()
data = response.json()

will_rain = False
for i in data['list']:
    weather_id = i['weather'][0]['id']
    description = i['weather'][0]['description']
    timestamp = i['dt_txt']
    #print(f'Time: {timestamp}, Weather_id: {weather_id}, Description: {description}')

    if weather_id > 700:
        will_rain = True

if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        from_='whatsapp:+14155238886',
        body= "It's going to rain today!",
        to=f'whatsapp:{MY_NUMBER}'
    )

    print(message.status)
