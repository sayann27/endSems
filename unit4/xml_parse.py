import xml.etree.ElementTree as ET

tree = ET.parse('demo.xml')
root = tree.getroot()

Books = root.findall('Book1')

for book in Books:
    name = book.find('Name').text
    author = book.get('author')
    print("\n\nName: " + name)
    print("Author: " + author)
