# Reading Employees.xml file

from xml.dom.minidom import parse

filename = r"C:\Users\demac\OneDrive\Desktop\WEB-SERVICES-APPLICATIONS\wsaa-coursework-labs\Topic02-DataRepresentation\employees.xml"

with open(filename) as fp:
    doc = parse(fp)

print(doc.toprettyxml(), end="")

employeeNodeList = doc.getElementsByTagName("Employee")
print(len(employeeNodeList))
for employeeNode in employeeNodeList:
    firstNameNode = employeeNode.getElementsByTagName("FirstName").item(0)
    firstName = firstNameNode.firstChild.nodeValue.strip()
    print(firstName)

# getElementsByTagName("FirstName"): Finds all FirstName tags within the current Employee node.
# .item(0): Gets the first FirstName node (index 0).
# .firstChild.nodeValue: Extracts the text value inside the FirstName node.
# .strip(): Removes any leading/trailing whitespace from the text.
# print(firstName): Prints the first name to the console.