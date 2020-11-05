import requests
import json

url = "https://www.balldontlie.io/api/v1/teams"
response = requests.get(url)
data = json.loads(response.text)

print(response.text)

print(data['data'][1]['full_name'])

