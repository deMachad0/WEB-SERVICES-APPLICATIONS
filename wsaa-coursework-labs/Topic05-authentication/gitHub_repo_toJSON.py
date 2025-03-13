# Getting Repository information on GitHub

import requests
import json

# Name the file where we will save the repository information
filename = "repos-Hello-Word-private.json"

# GitHub API URL for the specific repository we want to access
# Format: https://api.github.com/repos/{owner}/{repo_name}
url = "https://api.github.com/users/deMachad0/repos"
url2 = "https://api.github.com/repos/deMachad0/WEB-SERVICES-APPLICATIONS/contents/"

# Make a GET request to the GitHub API
response = requests.get(url2)

# Print the HTTP status code to check if request was successful
# 200 means success, 401 means unauthorized, 404 means not found
print(response.status_code)

# Convert the response to JSON format
repoJSON = response.json()
# Open the file in write mode to save the API response
with open(filename, "w") as fp:
    # Write the JSON data to the file with proper formatting (indent=4)
    # This makes the JSON file human-readable with proper indentation
    json.dump(repoJSON, fp, indent=4)