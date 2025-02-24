# Reading json file from a cloud

# Import the requests library to make HTTP requests
import json
import requests

# Define the URL of the API or website you want to request data from
url = "https://api.coingecko.com/api/v3/coins/bitcoin"

# Send a GET request to the specified URL and store the response
response = requests.get(url)

# Parse the response content as JSON and convert it into a Python dictionary (or list)
data = response.json()

# Print the parsed JSON data to the console
print(data)

# Open the file in write mode ('w') using a 'with' block (automatically closes the file after use)
# Saving/writting in a bitcoundump.json file
with open("bitcoindump.json", 'w') as fp:
   json.dump(data, fp)

print("-----------")
current_price = data["market_data"]["current_price"]["usd"]
print(current_price)