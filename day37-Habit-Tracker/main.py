import requests
from datetime import datetime
import os

USERNAME = 'odysseas'
TOKEN = os.environ.get("HABIT_TOKEN")
pixela_endpoint = 'https://pixe.la/v1/users'
GRAPH_ID = 'graph1'

#----------------create a new account on pixela-------------#
user_params = {
    'token': TOKEN,
    'username': USERNAME,
    'agreeTermsOfService': 'yes',
    'notMinor': 'yes',

}

# response = requests.post(url=pixela_endpoint,json=user_params)
# print(response.text)


#-----------------Setup new graph--------------------#
graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config = {
    'id': GRAPH_ID,
    'name': 'Python Graph',
    'unit': 'hours',
    'type': 'int',
    'color': 'momiji'
}

# Authenticate using a header
headers = {
    'X-USER-TOKEN': TOKEN
}

# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)

#-------------Post a pixel-----------------#

pixel_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"

today = datetime.now()
# print(today.strftime('%Y%m%d'))
today_formatted = today.strftime('%Y%m%d')

pixel_body = {
    'date': today_formatted,
    'quantity': '2',
}

# response = requests.post(url=pixel_endpoint, json=pixel_body, headers=headers)
# print(response.text)


#--------Update the pixel of a specific date-----------#

pixel_update = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{today_formatted}"

pixel_update_value = {
    'quantity': '0'
}

# response = requests.put(url=pixel_update, json=pixel_update_value, headers=headers)
# print(response.text)



#-------------Delete pixel----------------#

pixel_delete = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{today_formatted}"

# response = requests.delete(url=pixel_delete, headers=headers)
# print(response.text)

#-----URL----#
# https://pixe.la/v1/users/odysseas/graphs/graph1.html