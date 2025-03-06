# reading data from https://api.oireachtas.ie/v1/houses

import json
import requests

url = "https://api.oireachtas.ie/v1/houses"

# Send a GET request to the API and store the response
response = requests.get(url)
# Parse the JSON response into a Python dictionary
list_of_houses = response.json()
# Print the HTTP status code to check if the request was successful
print("Status Code:", response.status_code)

# Print the second house in the results list (for debugging or inspection)
print(list_of_houses["results"][1])
# Pretty-print the entire JSON response for better readability
print(json.dumps(list_of_houses, indent=4))

for house in list_of_houses["results"]:
    # Access the nested "house" dictionary within each result
    house_data = house["house"]
    print(f"House Code: {house_data['houseCode']}, House Number: {house_data['houseNo']}")

print("\nHouse's Range of Date")
for house in list_of_houses["results"]:
    # Access the nested "dateRange" dictionary within each house
    house_data = house["house"]["dateRange"]
    
    print(f"House start_date: {house_data['start']}, House end_date: {house_data['end']}")

print("\nCounting the number of houses")
count = 0  
total = 0  

for house in list_of_houses["results"]:
    # Access the nested "house" dictionary within each result
    house_data = house["house"]
    # Convert the house number (houseNo) from string to integer
    house_no = int(house_data["houseNo"])
    # Add the house number to the total
    total += house_no
    count += 1
# Print the total number of houses and the sum of their house numbers
print(f"Number of houses: {count}")
print(f"Number of houses built: {total}")
