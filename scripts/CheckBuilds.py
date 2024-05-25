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

skip = "true"
type = "null"
url = "null"

for i in j:
    data = j[i]
    if data['version'] == version and data['arch'] == arch and data['root_sol'] == root_sol and data['gapps_brand'] == gapps_brand:
        if data['type'] == 'Build':
            if data['timestamp'] + 89*24*60*60 >= time.time() and '-RemovedAmazon' in data['filename']:
                skip = "true"
                type = "Build"
                url = data['url']
        elif data['type'] == 'Release':
            skip = "true"
            type = "Release"
            url = data['url']
os.system("echo skip="+skip+" >> $GITHUB_OUTPUT")
os.system("echo url="+url+" >> $GITHUB_OUTPUT")
os.system("echo type="+type+" >> $GITHUB_OUTPUT")