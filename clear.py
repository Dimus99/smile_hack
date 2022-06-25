import os
from os import listdir
from os.path import isfile, join
import xml.etree.ElementTree as ET

a="""1246
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
612""".split("\n")
b = "1 45 68 77 81 93 107 115 131 140 146 147 149 153 162 170 177 200 208 212 222 223 233 234 244 258 261 271 275 297 311 325 326 327 382 406 417 454 455 481 503 599".split()
c = a+b
mypath = "all_text_proc"
onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]

for file in onlyfiles:
    if file.split(".")[0] in c:
        try:
            os.remove(f"all_text_proc/{file}")
        except:
            pass

