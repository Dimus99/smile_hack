from os import listdir
from os.path import isfile, join
import xml.etree.ElementTree as ET

mypath = "all_xml"
onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]
res = []
for file in onlyfiles:
    res_res = []
    with open(f"all_xml/{file}", encoding="cp1251") as f:

        xml = f.read()
        print(file)
        if xml:
            responseXml = ET.fromstring(xml)
            print(responseXml)
            filename = responseXml.find("filename")
            objects = responseXml.findall("object")
            for object1 in objects:
                res = []
                if object1.find("name").text == "teeth":
                    res.append("0")
                else:
                    res.append(("1"))
                size = [el.text for el in object1.find("bndbox").findall("bndbox")]
                for i in size:
                    res.append(str(i))
                res_res.append(res)

            print(size)
    with open(f"all_txt/{file.split('.')[0]}.txt", "w") as f:
        if res_res and res_res[0]:
            f.write(
                "\n".join(
                    [" ".join(s) for s in res_res]
                )
            )
