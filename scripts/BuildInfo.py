import sys
import json
import time
import hashlib

name = sys.argv[1]
version = sys.argv[2]
arch = sys.argv[3]
root_sol = sys.argv[4]
magisk_ver = sys.argv[5]
gapps_brand = sys.argv[6]
with open('output/'+name+'.zip', 'rb') as fp:
    hash = str(hashlib.sha256(fp.read()).hexdigest())
workflow_id = sys.argv[7]

if root_sol == 'magisk' and magisk_ver != 'stable':
    root_sol = root_sol+' '+magisk_ver

j = {
    name: {
        'filename': name+'.zip',
        'type': 'Build',
        'version': version,
        'arch': arch,
        'root_sol': root_sol,
        'gapps_brand': gapps_brand,
        'sha256': hash,
        'url': 'https://github.com/A-JiuA/WSAOnWin10/actions/runs/'+workflow_id,
        'timestamp': time.time()
    }
}

with open('builds.json', 'r') as f:
    data = json.load(f)
data.update(j)
with open('builds.json', 'w') as f:
    json.dump(data, f, indent=4)