from os import listdir
from os.path import isfile, join
from utils import get_img

mypath = "research/all_img_proc"
onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]
onlyfiles.sort()
bad = []
for file in onlyfiles:
    with open(f"research/all_img_proc/{file}", 'rb') as img:
        with open(f"research/all_text_proc/{file.split('.')[0]}.txt") as txt:
            goal = len([el for el in txt.readlines() if el[0]=="1"]) > 0
            res = get_img(img.read())[1] > 0
            if goal != res:
                print("\n!!!")
                print(goal, res, file)
                bad.append(file)
            print(file, goal, res)
