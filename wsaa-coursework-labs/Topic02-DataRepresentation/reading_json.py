# Reading Json file

# Import the json module to work with JSON data
import json

# Create a dictionary called 'data' with some key-value pairs
data = {
    'name': 'Joe',  # Key 'name' with value 'Joe'
    'age': 21,      # Key 'age' with value 21
    "student": True # Key 'student' with value True
}

# Print the dictionary to the console
print(data)

# Open a file named 'simple.json' in write mode ('w')
file = open("simple.json", 'w')

# (Commented out) Use json.dump() to write the dictionary 'data' into the file with an indentation of 4 spaces
# json.dump(data, file, indent=4)

# Convert the dictionary 'data' into a JSON-formatted string
jsonString = json.dumps(data)

# Print the JSON-formatted string to the console
print(jsonString)

# Closing the file
file.close()