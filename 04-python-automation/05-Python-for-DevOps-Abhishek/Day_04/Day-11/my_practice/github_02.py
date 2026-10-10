import requests

response = requests.get('https://api.github.com/repos/kubernetes/kubernetes/pulls')


# print(response.json())

complete_Detail = response.json()

for login in range(len(complete_Detail)):
    print(complete_Detail[login]["user"]["login"]) 


