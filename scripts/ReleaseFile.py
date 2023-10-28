import sys
import hashlib
import json
import time

version = sys.argv[1]
arch = sys.argv[2]
root_sol = sys.argv[3]
gapps_brand = sys.argv[4]
foldername = sys.argv[5]

name = 'WSA_'+version+'_'+arch+'_Release'
if root_sol != 'none' or gapps_brand != 'none':
    name += foldername[foldername.find('Release-Nightly')+len('Release-Nightly'):foldername.rfind('-RemovedAmazon')]
name = name.replace('-stable','').replace('-NoGApps','').replace('-RemovedAmazon','').replace(foldername[foldername.find('('):foldername.find(')')+1],'')
print(name)

with open(foldername+'.zip', 'rb') as fp:
    hash = str(hashlib.sha256(fp.read()).hexdigest())

j = {
    name: {
        'filename': name+'.zip',
        'type': 'Release',
        'version': version,
        'arch': arch,
        'root_sol': root_sol,
        'gapps_brand': gapps_brand,
        'sha256': hash,
        'url': 'https://github.com/A-JiuA/WSAOnWin10/releases/download/'+version+'/'+name+'.zip',
        'timestamp': time.time()
    }
}

with open('info.json', 'w') as f:
    # 使用json.dump()函数将序列化后的JSON格式的数据写入到文件中
    json.dump(j, f, indent=4)