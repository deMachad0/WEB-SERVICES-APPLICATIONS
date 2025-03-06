# API to read http://andrewbeatty1.pythonanywhere.com/books
# Using all the functions

import json
import requests

url = "http://andrewbeatty1.pythonanywhere.com/books"

# Write the function for find by id and test it
def getAllBooks():
    response = requests.get(url)
    return response.json()

def getBookId(id):
    geturl = url + "/" + str(id)
    response = requests.get(geturl)
    return response.json()

# write the code to create and test it (
def createBook(book):
    response = requests.post(url, json=book)

    return response.json()

# Write the update function
def updateBook(id, book):
    updateurl = url + "/" + str(id)
    response = requests.put(updateurl, json=book)
    return response.json()

# Write the delete function
def deleteBook(id):
    deleteurl = url + "/" + str(id)
    response = requests.delete(deleteurl)
    return response.json()


# Convert that into a function and call it from inside a 
# if __name__ == “__main__”:
if __name__ == "__main__":
    book= {
        'author': 'test',
        'title': 'test_title',
        "price": 123
    }
    bookdiff= {
        "price": 1234444
    }
    #print(getAllBooks())
    #print(getBookId(22))
    #print(deleteBook(76))
    #print(createBook(book))
    print(updateBook(22, bookdiff))