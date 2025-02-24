# Reading json from a file

import json

# Define the name of the JSON file to be read
filename = "employees.json"

# Open the file in read mode ('r') using a 'with' block (automatically closes the file after use)
with open(filename, "r") as fp:
    # Load the JSON data from the file and convert it into a Python dictionary (or list)
    jsonObject = json.load(fp)

# Print the entire JSON object (dictionary or list) to the console
print(jsonObject)

# Print a separator line for better readability in the output
print("---------------------")

# Loop through each item in the 'employees' list (assuming 'employees' is a key in the JSON object)
for employee in jsonObject['employees']:
    # Print each employee's details (each 'employee' is a dictionary)
    print(employee)