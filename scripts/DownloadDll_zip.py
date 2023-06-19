import os
import subprocess

result = os.popen("unzip -l Windows.zip").read()

if ".iso" in result:
    result = os.popen("unzip -l Windows.zip | grep .iso").read()
    result = result[result.rfind(" ")+1:result.rfind(".iso")+4]
    os.system("unzip Windows.zip "+result+" -d zip/")
    os.system("sudo mount -o loop "+result+" iso")
    result2 = os.popen("ls iso/sources/install.*")
    file_path = "iso/sources/"+result2
    type = ".iso"
elif ".iso" in result:
    result = os.popen("unzip -l Windows.zip | grep .wim").read()
    result = result[result.rfind(" ")+1:result.rfind(".wim")+4]
    os.system("unzip Windows.zip "+result+" -d zip/")
    file_path = "zip/"+result
elif ".esd" in result:
    result = os.popen("unzip -l Windows.zip | grep .esd").read()
    result = result[result.rfind(" ")+1:result.rfind(".esd")+4]
    os.system("unzip Windows.zip "+result+" -d zip/")
    file_path = "zip/"+result
else:
    exit(2)
os.system("wimextract "+file_path+" 1 /Windows/System32/icu.dll --dest-dir=dll")
os.system("wimextract "+file_path+" 1 /Windows/System32/winhttp.dll --dest-dir=dll")
if type:
    os.system("sudo umount iso")