# Reading APIS using urllib.parse
# What's the purpose?
# This is useful when you need to include special characters in a URL, 
# as URLs can only contain certain characters. 
# Encoding ensures the URL works correctly.

import urllib.parse  # Import module for URL encoding

query = 'Hello Wold@Pythin'  # String to encode
parsed = urllib.parse.quote(query)  # Encode special characters for URLs
print(parsed)  # Print the encoded string (e.g., Hello%20Wold%40Python)


# Encode parameters with Function using urlencode()

params = {'q': 'Python URL enconding', 'as_sitesearch': 'www.urlencoder.io'}
parsedparams = urllib.parse.urlencode(params)
print(parsedparams)

