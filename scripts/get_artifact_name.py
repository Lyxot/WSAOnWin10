import os
import json

json = json.loads(os.getenv("ARTIFACTS_LIST"))
for i in range(len(json)):
    os.system("echo foldername"+str(i)+"="+json[i]["name"]+" >> $GITHUB_OUTPUT")
    