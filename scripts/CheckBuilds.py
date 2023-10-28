import json
import sys
import time
import os

version = sys.argv[1]
arch = sys.argv[2]
root_sol = sys.argv[3]
gapps_brand = sys.argv[4]

with open('builds.json', 'r') as f:
    j = json.load(f)

for i in j:
    data = j[i]
    if data['version'] == version and data['arch'] == arch and data['root_sol'] == root_sol and data['gapps_brand'] == gapps_brand:
        if data['type'] == 'Build':
            if data['timestamp'] + 89*24*60*60 >= time.time() and '-RemovedAmazon' in data['filename']:
                os.system("echo skip=true >> $GITHUB_OUTPUT")
                os.system("echo type=Build >> $GITHUB_OUTPUT")
                os.system("echo url="+data['url']+" >> $GITHUB_OUTPUT")
                exit()
        elif data['type'] == 'Release':
            os.system("echo skip=true >> $GITHUB_OUTPUT")
            os.system("echo type=Release >> $GITHUB_OUTPUT")
            os.system("echo url="+data['url']+" >> $GITHUB_OUTPUT")
            exit()
os.system("echo skip=false >> $GITHUB_OUTPUT")
os.system("echo url=null >> $GITHUB_OUTPUT")
os.system("echo type=null >> $GITHUB_OUTPUT")