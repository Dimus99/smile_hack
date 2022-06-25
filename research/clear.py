import os
from os import listdir
from os.path import isfile, join
import shutil
import xml.etree.ElementTree as ET

a = """1246
1245
1244
1239
1165
1048
1051
1034
1027
1010
1008
979
977
976
970
969
966
950
906
901
900
899
898
897
893
873
868
853
843
835
834
831
827
819
815
814
805
803
800
795
786
777
763
761
748
747
745
738
737
721
720
719
718
713
710
708
707
704
683
681
675
647
635
629
628
999
0_(22)
0_(32)
0_(36)
0_(49)
41
105
109
144
154
159
165
169
237
240
242
251
265
266
272
273
286
290
312
317
323
354
356
364
381
398
399
401
402
432
469
470
472
482
483
507
509
568
585
592
593
603
604
614
625
691
739
884
904
913
955
993
1007
1013
1016
1017
1026
1029
1059
1060
1061
1062
1068
1071
1073
1092
1135
1145
1155
1157
1158
1174
1178
1183
1187
1201
1216
1235
1236
1243
612""".split("\n")
b = "1 45 68 77 81 93 107 115 131 140 146 147 149 153 162 170 177 200 208 212 222 223 233 234 244 258 261 271 275 297 311 325 326 327 382 406 417 454 455 481 503 599".split()
c = a + b
mypath = "all_txt"
onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]

for file in onlyfiles:
    if not file.split(".")[0] in c:
        with open(f"all_txt/{file}") as r:
            with open(f"all_text_proc/{file}", 'w') as w:
                for l in r.readlines():
                    d = l.split()
                    r = str(d[0])
                    for el in d[1:]:
                        v = min(256, max(0, int(el)))
                        if v != int(el):
                            print(file)
                        r += " " + str(v)
                    w.write(r+"\n")
        shutil.copy(f"all/{file.split('.')[0]}.jpg", f"all_img_proc/{file.split('.')[0]}.jpg")
