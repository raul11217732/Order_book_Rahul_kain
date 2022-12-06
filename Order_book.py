tree = ET.parse(filepath)

root = tree.getroot()

for elem in root:
    for subelem in elem:
        print(subelem.txt)
