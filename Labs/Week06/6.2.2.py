import requests
import json

url = 'https://api.github.com/Caoimhinv/aprivateone'
apiKey = 'XXX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XXX'
filename = 'github.json'

response = requests.get(url, auth=('token',apiKey))
repoJSON = response.json()
# print (response.json())
file = open(filename, 'w')
json.dump(repoJSON, file, indent=4)