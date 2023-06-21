import os
import json

js = json.loads(os.getenv("ARTIFACTS_LIST"))
c=0
for i in js:
    if i["name"][:3] == "WSA":
        print("echo foldername"+str(c)+"="+i["name"]+" >> $GITHUB_OUTPUT")
        os.system("echo foldername"+str(c)+"="+i["name"]+" >> $GITHUB_OUTPUT")
        c+=1
    