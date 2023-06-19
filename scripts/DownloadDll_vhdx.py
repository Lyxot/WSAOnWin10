import os
import sys

if len(sys.argv) < 2:
    exit(2)

output=[]

if len(sys.argv) == 2:
    print(sys.argv[1])
    exit()

for i in sys.argv[1:]:
    if "p" in i:
        result = os.popen("sudo fdisk -l "+i+" | awk 'NR==1'").read()
        if "：" in result and "，" in result:
            result = result[result.find("：")+1:result.find("，")]
        else:
            result = result[result.find(":")+1:result.find(",")]
        if "GiB" in result:
            print(i)
            exit()
exit(3)