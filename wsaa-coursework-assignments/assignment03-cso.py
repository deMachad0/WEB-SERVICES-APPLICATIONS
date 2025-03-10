# Reading a file multidimensional 

import requests
import json 


urlBegining = "https://ws.cso.ie/public/api.restful/PxStat.Data.Cube_API.ReadDataset/"
urlEnd = "/JSON-stat/2.0/en"

def getAllAsFile(dataset):
    with open("cso.json", "wt") as fp:
        print(json.dumps(getAll(dataset)), file=fp)


def getAll(dataset):
    url = urlBegining + dataset + urlEnd
    response = requests.get(url)
    return response.json()

def getFormattedAsFile(dataset):
    with open("cso-formatted.json", "wt") as fp:
        print(json.dumps(getFormated(dataset)), file=fp)

def getFormated(dataset):
    data = getAll(dataset)
    ids = data["id"]
    values = data["value"]
    dimensions = data["dimension"]
    sizes = data["size"]
    valueCount = 0
    result = {}
   

    for dim0 in range(0, sizes[0]):
        currentId = ids[0]
        index = dimensions[currentId]["category"]["index"][dim0]
        label0 = dimensions[currentId]["category"]["label"][index]
        result[label0]={}
        print(label0)
        for dim1 in range(0, sizes[1]):
            currentId = ids[1]
            index = dimensions[currentId]["category"]["index"][dim1]
            label1 = dimensions[currentId]["category"]["label"][index]
            result[label0][label1]={}
            print("\t", label1)
            for dim2 in range(0, sizes[2]):
                currentId = ids[2]
                index = dimensions[currentId]["category"]["index"][dim2]
                label2 = dimensions[currentId]["category"]["label"][index]
                result[label0][label1][label2]= values[valueCount]
                print("\t\t", label2, " ", values[valueCount])
                valueCount +=1
                
   
    return result

if __name__ == "__main__":
    #getAllAsFile("FIQ02")
    getFormattedAsFile("FIQ02")