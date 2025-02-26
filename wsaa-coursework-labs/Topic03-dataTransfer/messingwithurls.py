import requests

url = "https://atu.ie"

response = requests.get(url)
print(response.status_code)