import os
from os import listdir
from os.path import isfile, join
import random
import xml.etree.ElementTree as ET

mypath = "all_text_proc"
onlyfiles = [f.split(".")[0] for f in listdir(mypath) if isfile(join(mypath, f))]
res = []
while len(res) <= len(onlyfiles)*0.8:
    el = random.choice(onlyfiles)
    if el not in res:
        res.append(el)
ot = set(onlyfiles) - set(res)
ot = list(ot)
for i in res:
    os.replace(f"all_text_proc/{i}.txt", f"80/{i}.txt")
    os.replace(f"all/{i}.jpg", f"80/{i}.jpg")
for i in ot:
    os.replace(f"all_text_proc/{i}.txt", f"20/{i}.txt")
    os.replace(f"all/{i}.jpg", f"20/{i}.jpg")


