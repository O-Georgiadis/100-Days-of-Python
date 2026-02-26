import requests
api_key = ""

MY_LAT = 37.9838
MY_LONG = 23.7275


parameters = {
    "appid": api_key,
    "lat": MY_LAT,
    "lon": MY_LONG
}


response = requests.get(url="https://api.openweathermap.org/data/2.5/forecast", params = parameters)

print(response.json())