tree = ET.parse('path')

root = tree.getroot()

i = 0
for elem in root:
    if i>10:
        break
    for subelem in elem:
        if i>10:
            break
        i+=1
        print(subelem.txt)
