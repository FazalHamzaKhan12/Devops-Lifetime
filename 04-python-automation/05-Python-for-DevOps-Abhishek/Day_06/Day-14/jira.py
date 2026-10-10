# This code sample uses the 'requests' library:
# http://docs.python-requests.org
import requests
from requests.auth import HTTPBasicAuth
import json

url = "https://fazalhamzakhan.atlassian.net/rest/api/3/project"


API_TOKEN="ATATT3xFfGF0oyJ_Vnws2l8gWXvSFKHmBNRm4HuqgAJr9HzlF8SyFdNstVUmKxKldJkFk7TsVEZaIDZUvKTtqoQLQSDpVtfe0AsJyo69ESrHBSzmplRVu9CXk6CSALqOmf8rGSjj2ABZ7_72DYQ2_3fQj6M2wNIxCV8mYRje_MS54tq0ZkxEA80=79AA1086"
auth = HTTPBasicAuth("theunknown.pak@gmail.com", API_TOKEN)

headers = {
  "Accept": "application/json"
}

response = requests.request(
   "GET",
   url,
   headers=headers,
   auth=auth
)


output = json.loads(response.text)

name = output[0]["name"]
print(name)