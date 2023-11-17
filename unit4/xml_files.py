import xml.etree.ElementTree as ET

root = ET.Element("Library")

child1 = ET.SubElement(root, "Book1")

subchild1 = ET.SubElement(child1, "Name")
subchild1.text = "Python"
child1.set('author', 'Enid Blyton')



child2 = ET.SubElement(root, "Book1")

subchild1 = ET.SubElement(child2, "Name")
subchild1.text = "Hello"

#This sets an attribute
child2.set('author', 'Sayan Mandal')

tree = ET.ElementTree(root)
tree.write("demo.xml")

#Printing it as a string
xmlString = ET.tostring(root)
print(xmlString.decode())