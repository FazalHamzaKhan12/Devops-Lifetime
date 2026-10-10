import requests

url = "https://fake-json-api.mock.beeceptor.com/users"

response = requests.get(url)
print(response.json())