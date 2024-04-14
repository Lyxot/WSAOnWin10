import json
from datetime import datetime

# Read the contents of build.json file
with open('./builds.json', 'r') as f:
    build_data = json.load(f)

# Sort build_data by filename in ascending order and then by version in descending order
build_data = sorted(build_data.values(), key=lambda x: (x['filename'], x['version']), reverse=True)


version_list = []
for i in build_data:
    if i['version'] not in version_list:
        version_list.append(i['version'])

md_table = ""

md_table += '''# Index
- [Build History](#build-history)
- [Arch](#arch)
  - [Arm64](#arm64)
  - [x64](#x64)
- [Root Solution](#root-solution)
  - [None Root](#none-root)
  - [Magisk](#magisk)
  - [Other Magisk](#other-magisk)
  - [KernelSU](#kernelsu)
- [GApps Brand](#gapps-brand)
  - [None GApps](#none-gapps)
  - [MindTheGapps](#mindthegapps)
  - [OpenGApps](#opengapps)
- [Version](#version)
'''
for i in version_list:
    md_table += "  - [" + i + "](#" + i.replace('.','').replace(' ','-') + ")\n"

md_table += '''- [Type](#type)
  - [Release](#release)
  - [Build](#build)
'''

def generate_md_table(data, expired=False):
    # Get the values from the json file
    filename = data['filename']
    type = data['type']
    version = data['version']
    arch = data['arch']
    root_sol = data['root_sol']
    gapps_brand = data['gapps_brand']
    sha256 = data['sha256']
    url = data['url']
    timestamp = data['timestamp']
    table = ""
    if expired:
        table += '| <text style="color:red;font-style:italic;">expired!!</text>\t' + filename + " | "
    else:
        table += "| " + filename + " | "
    if root_sol == 'none':
        table += type + " | `" + version + "` | `" + arch + "` | &#10006; |"
    else:
        table += type + " | `" + version + "` | `" + arch + "` | `" + root_sol.replace('magisk','Magisk').replace('kernelsu','KernelSU').replace('canary','Canary').replace('beta','Beta').replace('debug','Debug') + "` |"
    if gapps_brand == 'none':
        table += "&#10006; | `" + sha256 + "` | " + url + " | "
    else:
        table += "`" + gapps_brand + "` | `" + sha256 + "` | " + url + " | "

    # convert timestamp to human readable format
    timestamp = datetime.fromtimestamp(int(timestamp)).strftime('%Y-%m-%d %H:%M:%S')
    table += timestamp + " |\n"
    return table

# Create the header for the Markdown table
header = "| Filename | Type | Version | Arch | Root Solution | GApps Brand | SHA256 | URL | Build Date |\n| -------- | :----: | ------- | :----: | :-------------: | :-----------: | ------ | --- | --------- |\n"

# Create the Markdown table
md_table += "# Build History\n"
md_table += header
for i in version_list:
    for data in build_data:
        if data['type'] == 'Release' and data['version'] == i:
            md_table += generate_md_table(data)
for i in version_list:
    for data in build_data:
        if data['type'] == 'Build' and data['version'] == i:
            if data['timestamp'] + 90*24*60*60 < int(datetime.now().timestamp()):
                md_table += generate_md_table(data, True)
            else:
                md_table += generate_md_table(data, False)
# Add back to top link
md_table += "\n[Back to top](#index)\n"

# sort the history by Arch
md_table += "# Arch\n"
for j in ['x64', 'arm64']:
    md_table += "## " + j.replace('arm64','Arm64') + "\n"
    md_table += header
    for i in version_list:
        for data in build_data:
            if data['version'] == i and data['type'] == 'Release' and data['arch'] == j:
                md_table += generate_md_table(data)
        for data in build_data:
            if data['version'] == i and data['type'] == 'Build' and data['arch'] == j:
                if data['timestamp'] + 90*24*60*60 < int(datetime.now().timestamp()):
                    md_table += generate_md_table(data, True)
                else:
                    md_table += generate_md_table(data, False)
    # Add back to top link
    md_table += "\n[Back to top](#index)\n"

# sort the history by Root Solution
md_table += "# Root Solution\n"
for j in ['none', 'magisk', 'kernelsu']:
    md_table += "## " + j.replace('magisk','Magisk').replace('kernelsu','KernelSU').replace('none','None Root') + "\n"
    md_table += header
    for i in version_list:
        for data in build_data:
            if data['version'] == i and data['type'] == 'Release' and data['root_sol'] == j:
                md_table += generate_md_table(data)
        for data in build_data:
            if data['version'] == i and data['type'] == 'Build' and data['root_sol'] == j:
                if data['timestamp'] + 90*24*60*60 < int(datetime.now().timestamp()):
                    md_table += generate_md_table(data, True)
                else:
                    md_table += generate_md_table(data, False)
    # Add back to top link
    md_table += "\n[Back to top](#index)\n"
    if j == 'magisk':
        md_table += "## Other Magisk\n"
        md_table += header
        for i in version_list:
            for data in build_data:
                if data['version'] == i and data['type'] == 'Release' and 'magisk ' in data['root_sol']:
                    md_table += generate_md_table(data)
            for data in build_data:
                if data['version'] == i and data['type'] == 'Build' and 'magisk ' in data['root_sol']:
                    if data['timestamp'] + 90*24*60*60 < int(datetime.now().timestamp()):
                        md_table += generate_md_table(data, True)
                    else:
                        md_table += generate_md_table(data, False)
        md_table += "\n[Back to top](#index)\n"

# sort the history by GApps Brand
md_table += "# GApps Brand\n"
for j in ['none', 'MindTheGapps', 'OpenGApps']:
    md_table += "## " + j.replace('none','None GApps') + "\n"
    md_table += header
    for i in version_list:
        for data in build_data:
            if data['version'] == i and data['type'] == 'Release' and data['gapps_brand'] == j:
                md_table += generate_md_table(data)
        for data in build_data:
            if data['version'] == i and data['type'] == 'Build' and data['gapps_brand'] == j:
                if data['timestamp'] + 90*24*60*60 < int(datetime.now().timestamp()):
                    md_table += generate_md_table(data, True)
                else:
                    md_table += generate_md_table(data, False)
    # Add back to top link
    md_table += "\n[Back to top](#index)\n"

# sort the history by version
md_table += "# Version\n"
for i in version_list:
    md_table += "## " + i + "\n"
    md_table += header
    for data in build_data:
        if data['version'] == i and data['type'] == 'Release':
            md_table += generate_md_table(data)
    for data in build_data:
        if data['version'] == i and data['type'] == 'Build':
            if data['timestamp'] + 90*24*60*60 < int(datetime.now().timestamp()):
                md_table += generate_md_table(data, True)
            else:
                md_table += generate_md_table(data, False)
    # Add back to top link
    md_table += "\n[Back to top](#index)\n"

# sort the history by type
md_table += "# Type\n"
for j in ['Release', 'Build']:
    md_table += "## " + j + "\n"
    md_table += header
    for i in version_list:
        for data in build_data:
            if data['version'] == i and data['type'] == j:
                md_table += generate_md_table(data)
    # Add back to top link
    md_table += "\n[Back to top](#index)\n"

# Write the Markdown table to the builds.md file
with open('./builds.md', 'w') as f:
    f.write(md_table)

    
    