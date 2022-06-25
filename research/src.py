# import pandas as pd
# import numpy as np
import cv2
import os

# xml_files = os.listdir('all/')
# img_files = os.listdir('all_xml/')
txt_files = os.listdir('all_text_proc/')
print("start")
print(txt_files)
max_q, max_w, max_e = 1000, 1000, 1000
dict_of_txt = dict()
edited ="""
1208.txt
776.txt
0_ (47).txt
1082.txt
1082.txt
1196.txt
1196.txt
1019.txt
540.txt
1131.txt
743.txt
954.txt
954.txt
1065.txt
651.txt
1072.txt
1072.txt
862.txt
862.txt
575.txt
871.txt
663.txt
1064.txt
605.txt
1035.txt
660.txt
660.txt
1017.txt
587.txt
587.txt
1033.txt
600.txt
600.txt
791.txt
749.txt
1100.txt
1140.txt
693.txt
631.txt
631.txt
631.txt
593.txt
593.txt
1117.txt
1029.txt
715.txt
1102.txt
951.txt
1026.txt
659.txt
1192.txt
1192.txt
452.txt
1038.txt
672.txt
994.txt
671.txt
671.txt
603.txt
603.txt
793.txt
830.txt
874.txt
810.txt
1237.txt
1101.txt
1125.txt
533.txt
753.txt
771.txt
751.txt
546.txt
1160.txt
1160.txt
858.txt
1018.txt
535.txt
1189.txt
1189.txt
1003.txt
566.txt
757.txt
665.txt
0_ (27).txt
0_ (27).txt
833.txt
690.txt
1191.txt
948.txt
1243.txt
1124.txt
1233.txt
1127.txt
1046.txt
1046.txt
563.txt
1047.txt
1106.txt
1106.txt
760.txt
760.txt
""".split("\n")

for i in txt_files:
    # if i not in edited:
    #     continue
    with open(f"all_text_proc/{i}") as file:
        txt = file.readlines()
        txt = list(map(lambda x: x.replace('\n', '').split()[1:], txt))
    img = cv2.imread(f'all/{i[:-3]}jpg')
    print(i)
    for j in txt:
        q = list(map(int, j))
        print(q)
        x, y, w, h = q
        cv2.rectangle(img, (x, y), (w, h), (0, 255, 0), 2)
    cv2.imwrite(f'all_jpeg_with_bb/{i[:-3]}jpg', img)

# cv2.imwrite(f'/home/kirill/Загрузки/Telegram Desktop/all_jpeg_with_bb/{i[:-3]}jpg', img)
# print(f'/home/kirill/Загрузки/Telegram Desktop/all_jpeg_with_bb/{i[:-3]}jpg')
# print(txt)
