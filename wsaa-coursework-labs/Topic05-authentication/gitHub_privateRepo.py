# Getting information from private repo on GitHub using key

import requests
import json
from config import apikeys as cfg  # Importing configuration file with API keys

# Name of the file where we'll save the repository information
filename = "repos-private.json"

# GitHub API URL for the specific repository we want to access
# Format: https://api.github.com/repos/{owner}/{repo_name}
url = "https://api.github.com/repos/deMachad0/Hello-World"

# Get the GitHub API key from our configuration file
apikey = cfg['githubkeys']

# Make a GET request to the GitHub API
# The 'auth' parameter is using token-based authentication
# Note: GitHub's preferred auth method is now using a Bearer token in headers
response = requests.get(url, auth=('token', apikey))

# Print the HTTP status code to check if request was successful
# 200 means success, 401 means unauthorized, 404 means not found
print(response.status_code)

# Open the file in write mode to save the API response
with open(filename, "w") as fp:
    # Convert the response to JSON format
    repoJSON = response.json()
    
    # Write the JSON data to the file with proper formatting (indent=4)
    # This makes the JSON file human-readable with proper indentation
    json.dump(repoJSON, fp, indent=4)
