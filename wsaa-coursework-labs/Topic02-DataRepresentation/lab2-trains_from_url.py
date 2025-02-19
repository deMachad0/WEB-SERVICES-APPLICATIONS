# Reading api.irishrail.ie as XML file
# Author: Andre

import requests
from xml.dom.minidom import parseString

url = "https://api.irishrail.ie/realtime/realtime.asmx/getCurrentTrainsXML"

page = requests.get(url)
doc = parseString(page.content)

print(doc.toprettyxml(), end="")

objTrainPositions = doc.getElementsByTagName("objTrainPositions")
print(len(objTrainPositions))
for trainPositions in objTrainPositions:
    firstTrainCode = trainPositions.getElementsByTagName("TrainCode").item(0)
    trainCode = firstTrainCode.firstChild.nodeValue.strip()
    print(trainCode)

print("Part 2 ---------------------------")
# Printing the latitude

objTrainPositions = doc.getElementsByTagName("objTrainPositions")
for trainPositions in objTrainPositions:
    firstTrainLatitude = trainPositions.getElementsByTagName("TrainLatitude").item(0)
    trainLatitude = firstTrainLatitude.firstChild.nodeValue.strip()
    print(trainLatitude)