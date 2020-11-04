import requests
import json

url = "https://www.balldontlie.io/api/v1/stats"
response = requests.get(url)
print (response.text)