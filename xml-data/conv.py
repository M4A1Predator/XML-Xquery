import csv
import xml.etree.ElementTree as ET

data_list = []

with open('dc-wikia-data.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    c = 0

    print(reader.dialect)

    for row in reader:
        data_list.append(row)

        c += 1

        # if c >= 100:
        #     break


xml_file_name = 'my_dc.xml'

root = ET.Element("DC")
dc_hero = ET.SubElement(root, 'heros')

for data in data_list:
    hero = ET.SubElement(dc_hero, 'hero')

    for k, v in data.items():
        # Check if has value, then create element
        if v:

            # Check custom condition
            if k == 'urlslug':
                element = ET.SubElement(hero, k, url=v)
                continue

            elif k == 'page_id':
                element = hero.set('page_id', v)
                continue

            # Remove element spaces
            k = k.strip(' ')
            k = k.replace(' ', '_')

            # Create element node
            k = k.lower()
            element = ET.SubElement(hero, k).text = v

# Write XML file
tree = ET.ElementTree(root)
tree.write(xml_file_name)
