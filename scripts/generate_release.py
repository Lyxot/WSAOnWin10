import os
import sys
import hashlib

last_version=os.getenv('LATEST_TAG')
file_list = os.listdir('.')
file_list.sort()
print(file_list)
version = '0.0.0.0'
for i in file_list:
    cv = i[i.find('_')+1:]
    cv = cv[:cv.find('_')]
    v_l = version.split('.')
    cv_l = cv.split('.')
    if cv_l[0] >= v_l[0] and cv_l[1] >= v_l[1] and cv_l[2] >= v_l[2] and cv_l[3] >= v_l[3]:
        version = cv
    os.system('mv "'+i+'" "'+i.replace('-Nightly','').replace('-stable','').replace('-NoGApps','').replace('-RemovedAmazon','').replace(i[i.find('('):i.find(')')+1],'')+'" 2>/dev/null || :')
os.system('echo "version='+version+'" >> "$GITHUB_OUTPUT"')
if last_version == version:
    exit()
file_list = os.listdir('.')
file_list.sort()
with open('Changelog.md','w') as f:
    f.write('# Changelog\n')
    f.write('## Update WSA Version From `'+last_version+'` to `'+version+'`\n')
    f.write('### SHA256 Checksum\n')
    f.write('```\n')
    for i in file_list:
        with open(i, 'rb') as fp:
            f.write(str(hashlib.sha256(fp.read()).hexdigest())+' '+i+'\n')
    f.write('```\n')
with open('Changelog.md','r') as f:
    print(f.read())

for i in range(len(file_list)):
    os.system('echo "filename'+str(i)+'='+file_list[i]+'" >> "$GITHUB_OUTPUT"')
