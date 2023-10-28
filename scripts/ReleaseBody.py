import os
import json

latest_version=os.getenv('LATEST_VERSION')
current_version=os.getenv('CURRENT_VERSION')

file_list = [
    'arm64_none_MindTheGapps',
    'arm64_kernelsu_MindTheGapps',
    'arm64_kernelsu_none',
    'arm64_magisk_MindTheGapps',
    'arm64_magisk_none',
    'arm64_none_none',
    'x64_none_MindTheGapps',
    'x64_kernelsu_MindTheGapps',
    'x64_kernelsu_none',
    'x64_magisk_MindTheGapps',
    'x64_magisk_none',
    'x64_none_none'
]

with open('README.md','r') as f:
    txt=f.read()
    txt=txt[txt.find('## Installation'):txt.find('## Uninstallation')]

with open('Changelog.md','w') as f:
    f.write('## Changelog\n')
    f.write('### Update WSA Version From `'+current_version+'` to `'+latest_version+'`\n')
    f.write(txt)
    f.write('## Information\n')
    f.write('| |Filename|Root|GApps|\n|-|-|:-:|:-:|\n')
    for i in file_list:
        with open('output/release_'+i+'/info.json', 'r') as j:
            d = json.load(j)
        for k in d:
            f.write("| |"+d[k]["filename"]+"|")
            if d[k]["root_sol"] == 'none':
                f.write("&#10006;|")
            elif d[k]["root_sol"] == 'magisk':
                f.write("`Magisk`|")
            elif d[k]["root_sol"] == 'kernelsu':
                f.write("`KernelSU`|")
            if d[k]["gapps_brand"] == 'none':
                f.write("&#10006;|")
            else:
                f.write("`"+d[k]["gapps_brand"]+"`|")
            f.write("\n")
            f.write("|SHA256:|`"+d[k]["sha256"]+"`| | |\n")

with open('Changelog.md', 'r') as f:
    print(f.read())

with open('builds.json', 'r') as f:
    data = json.load(f)
for i in file_list:
    with open('output/release_'+i+'/info.json', 'r') as j:
        d = json.load(j)
        data.update(d)
with open('builds.json', 'w') as f:
    json.dump(data, f, indent=4)