# Reading a multidimensional file

import requests  
import json      

# Define the base URL for the API
urlBegining = "https://ws.cso.ie/public/api.restful/PxStat.Data.Cube_API.ReadDataset/"
urlEnd = "/JSON-stat/2.0/en"

# Function to save the raw JSON data to a file
def getAllAsFile(dataset):
    with open("cso.json", "wt") as fp:  # Open a file in write mode
        print(json.dumps(getAll(dataset)), file=fp)  # Write the JSON data to the file

# Function to fetch raw JSON data from the API
def getAll(dataset):
    url = urlBegining + dataset + urlEnd  # Construct the full URL
    response = requests.get(url)         # Make a GET request to the API
    return response.json()               # Return the JSON response

# Function to save the formatted JSON data to a file
def getFormattedAsFile(dataset):
    with open("cso-formatted.json", "wt") as fp:  # Open a file in write mode
        print(json.dumps(getFormated(dataset)), file=fp)  # Write the formatted JSON data to the file

# Function to format the JSON data into a nested dictionary structure
def getFormated(dataset):
    data = getAll(dataset)  # Fetch the raw JSON data
    ids = data["id"]        # Get the list of dimension IDs
    values = data["value"]  # Get the list of values
    dimensions = data["dimension"]  # Get the metadata for each dimension
    sizes = data["size"]    # Get the size of each dimension
    valueCount = 0          # Initialize a counter for the values array
    result = {}             # Initialize an empty dictionary to store the formatted data

    # Loop through the first dimension
    for dim0 in range(0, sizes[0]):
        currentId = ids[0]  # Get the ID of the first dimension
        index = dimensions[currentId]["category"]["index"][dim0]  # Get the index for the current dimension
        label0 = dimensions[currentId]["category"]["label"][index]  # Get the label for the current dimension
        result[label0] = {}  # Initialize a nested dictionary for the first dimension

        # Loop through the second dimension
        for dim1 in range(0, sizes[1]):
            currentId = ids[1]  # Get the ID of the second dimension
            index = dimensions[currentId]["category"]["index"][dim1]  # Get the index for the current dimension
            label1 = dimensions[currentId]["category"]["label"][index]  # Get the label for the current dimension
            result[label0][label1] = {}  # Initialize a nested dictionary for the second dimension

            # Loop through the third dimension
            for dim2 in range(0, sizes[2]):
                currentId = ids[2]  # Get the ID of the third dimension
                index = dimensions[currentId]["category"]["index"][dim2]  # Get the index for the current dimension
                label2 = dimensions[currentId]["category"]["label"][index]  # Get the label for the current dimension
                result[label0][label1][label2] = {}  # Initialize a nested dictionary for the third dimension

                # Loop through the fourth dimension
                for dim3 in range(0, sizes[3]):
                    currentId = ids[3]  # Get the ID of the fourth dimension
                    index = dimensions[currentId]["category"]["index"][dim3]  # Get the index for the current dimension
                    label3 = dimensions[currentId]["category"]["label"][index]  # Get the label for the current dimension
                    result[label0][label1][label2][label3] = values[valueCount]  # Assign the value to the nested dictionary
                    valueCount += 1  # Increment the value counter

    return result  # Return the formatted nested dictionary

# Main block to execute the code
if __name__ == "__main__":
    # getAllAsFile("FP001")
    
    # Save the formatted JSON data to a file
    getFormattedAsFile("FP001")