import requests

resonse = requests.get('https://api.github.com/repos/kubernetes/kubernetes/pulls')

output = resonse.json()

for ouputs in range(len(output)):
    print(output[ouputs]["user"]["login"])