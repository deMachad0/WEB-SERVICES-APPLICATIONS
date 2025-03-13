# Getting an API key using Requests

import requests  
import urllib.parse  
from config import apikeys as cfg  # Importing API keys from a config file

# The target URL we want to convert into a PDF
targetUrl =  "https://en.wikipedia.org"

# Getting the API key from the config file
apikey = cfg["htmltopdfkey"]

# The API endpoint for converting HTML to PDF
apiurl = "https://api.html2pdf.app/v1/generate"

# Setting up the parameters required for the API request
params = {'html': targetUrl, 'apikey': apikey}

# Encoding the parameters to be used in the URL
parsedparams = urllib.parse.urlencode(params)

# Constructing the final request URL
requestUrl = apiurl + "?" + parsedparams
print(requestUrl)  # Printing the request URL for debugging

# Sending a GET request to the API
response = requests.get(requestUrl)

# Printing the HTTP status code to check if the request was successful
print(response.status_code)

# Getting the response content (the generated PDF)
result = response.content

# Saving the PDF file to the local system
with open("document.pdf", "wb") as handler:
    handler.write(result)  # Writing the binary content to a file

