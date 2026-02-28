import requests
from datetime import datetime
import os

APP_ID = os.environ['APP_ID']
API_KEY = os.environ['API_KEY']
SHEET_TOKEN = os.environ['SHEET_TOKEN']

sheets_endpoint = 'https://api.sheety.co/52c3da1c2fbd2c09a015775404a8d078/workoutTracking/workouts'

exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"

GENDER = 'male'
WEIGHT = 83
HEIGHT = 184
AGE = 26


exercises = input('Tell me which exercises you did: ')

headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
}

parameters = {
    'query': exercises,
    'gender': GENDER,
    'weight_kg': WEIGHT,
    'height_cm': HEIGHT,
    'age': AGE,
}

response = requests.post(url=exercise_endpoint, json=parameters, headers=headers)
result = response.json()
print(result)

today = datetime.now()
today_formatted_date = today.strftime('%d/%m/%Y')
today_time = today.strftime("%X")


for exercise in result['exercises']:
    sheet_inputs = {
        "workout": {
          "date": today_formatted_date,
          "time": today_time,
          'exercise': exercise['name'].title(),
          'duration': exercise['duration_min'],
          'calories': exercise['nf_calories'],
      }
    }

    # sheet_response = requests.post(url=sheets_endpoint, json=sheet_inputs)
    # print(sheet_response.text)

    #Bearer Token Authentication
    bearer_headers = {
        "Authorization": f"Bearer {SHEET_TOKEN}"
    }
    sheet_response = requests.post(
        sheets_endpoint,
        json=sheet_inputs,
        headers=bearer_headers
    )

    print(sheet_response.text)


#---------------LINK OF GOOGLE SHEET------------------------#
#https://docs.google.com/spreadsheets/d/1wheIBc8WwpSsGOemAMIMh0fVT-P28Gbz6FjUYgu