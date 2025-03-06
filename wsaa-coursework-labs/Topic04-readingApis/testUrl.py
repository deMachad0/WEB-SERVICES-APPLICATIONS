# Test to see if requests is working for you 

import requests

url = "http://google.com"

response = requests.get(url)

print(response.text)