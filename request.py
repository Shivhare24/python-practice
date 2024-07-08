import requests
import json


r = requests.get('https://dummyjson.com/products/1')
# print(type(r.text))

response = json.loads(r.text)
for keys in response:
    print(keys, response.get(keys))

