import requests
import wget

import sys
import os
import subprocess
import locale
import re

def get_locale_lang() ->str:
    ret_locale = list(locale.getdefaultlocale())
    if ret_locale[1] == 'cp950':
        return 'Big5'
    elif ret_locale[1] == 'cp936':
        return 'GBK'
    elif ret_locale[1] == 'cp1252':
        return 'utf8'
    else:
        return 'utf8'

if len(sys.argv) != 6:
    exit(1)

ARCH = sys.argv[1]
VERSION = sys.argv[2]
BUILD = sys.argv[3]
URL = sys.argv[4]
FORMAT = sys.argv[5]

print("Arch: "+ARCH)
print("Version: "+VERSION)
print("Build: "+BUILD)
print("Download URL: "+URL)
print("Format: "+FORMAT)

wget.download(URL, out="Windows"+FORMAT)

if FORMAT == ".vhdx":
    # os.system("Mount-VHD -path Windows.vhdx")
    os.rmdir("Windows")
    os.mkdir("Windows")
    p1 = subprocess.Popen("diskpart", stdin=subprocess.PIPE, stdout=subprocess.PIPE, env=os.environ)
    res1 = p1.stdin.write(bytes("SELECT VDISK FILE="+os.getcwd()+"\Windows.vhdx\n", 'utf-8'))
    res1 = p1.stdin.write(bytes("ATTACH VDISK READONLY\n", 'utf-8'))

    p2 = subprocess.Popen("diskpart", stdin=subprocess.PIPE, stdout=subprocess.PIPE, env=os.environ)
    res2 = p2.stdin.write(bytes("LIST VDISK\n", 'utf-8'))
    stdout, stderr = p2.communicate()
    output = stdout.decode(get_locale_lang(), errors='ignore')
    output = output.replace("虚拟磁盘","Virtual Volume").replace("磁盘","Volume")
    output = output[output.rfind("Virtual Volume")+len("Virtual Volume"):]
    output = output[output.rfind("Volume")+len("Volume"):]
    output = output[re.search(r"\d",output).start():]
    output = output[:output.find(" ")]
    Disk_Number = output

    p3 = subprocess.Popen("diskpart", stdin=subprocess.PIPE, stdout=subprocess.PIPE, env=os.environ)
    res3 = p3.stdin.write(bytes("SELECT DISK "+Disk_Number+"\n", 'utf-8'))
    res3 = p3.stdin.write(bytes("LIST PARTITION\n", 'utf-8'))
    stdout, stderr = p3.communicate()
    output = stdout.decode(get_locale_lang(), errors='ignore')
    output = output.replace("分区","Partition")
    output = output[output.rfind("Partition")+len("Partition"):]
    output = output[re.search(r"\d",output).start():]
    output = output[:output.find(" ")]
    Partition_Number = output

    p4 = subprocess.Popen("diskpart", stdin=subprocess.PIPE, stdout=subprocess.PIPE, env=os.environ)
    res4 = p4.stdin.write(bytes("SELECT DISK "+Disk_Number+"\n", 'utf-8'))
    res4 = p4.stdin.write(bytes("SELECT PARTITION "+Partition_Number+"\n", 'utf-8'))
    res4 = p4.stdin.write(bytes("REMOVE ALL DISMOUNT\n", 'utf-8'))
    res4 = p4.stdin.write(bytes("ASSIGN MOUNT=" + os.getcwd() + "\Windows\n", 'utf-8'))
    stdout, stderr = p4.communicate()
    output = stdout.decode(get_locale_lang(), errors='ignore')
    
    WINDOWS_ROOT = os.getcwd()+"\Windows"
    
elif FORMAT == ".zip":
    os.rmdir("Windows")
    os.mkdir("Windows")
    os.system("Expand-Archive -Path Windows.zip -DestinationPath Windows")

    WINDOWS_ROOT = os.getcwd()+"\Windows"

elif FORMAT == ".iso":
    p1 = subprocess.Popen("powershell", stdin=subprocess.PIPE, stdout=subprocess.PIPE, env=os.environ)
    res1 = p1.stdin.write(bytes("mount-DiskImage "+os.getcwd()+"\Windows.iso\n", 'utf-8'))
    stdout, stderr = p1.communicate()
    output = stdout.decode(get_locale_lang(), errors='ignore')
    output = output[output.find("DevicePath"):]
    output = output[output.find(":")+1:output.find("\n")].replace(" ","")
    CD_PATH = output

    p2 = subprocess.Popen("powershell", stdin=subprocess.PIPE, stdout=subprocess.PIPE, env=os.environ)
    res2 = p2.stdin.write(bytes("ls "+CD_PATH+"\sources\install.* \n", 'utf-8'))
    stdout, stderr = p2.communicate()
    output = stdout.decode(get_locale_lang(), errors='ignore')
    if "install.wim" in output:
        FILE_PATH = CD_PATH+"\sources\install.wim"
    elif "install.esd" in output:
        FILE_PATH = CD_PATH+"\sources\install.esd"
    else:
        exit()
    p3 = subprocess.Popen("powershell", stdin=subprocess.PIPE, stdout=subprocess.PIPE, env=os.environ)
    res3 = p3.stdin.write(bytes("dism /Apply-Image /ImageFile:"+FILE_PATH+" /Index:4 /ApplyDir:"+os.getcwd()+"\Windows\n", 'utf-8'))
    stdout, stderr = p3.communicate()
    output = stdout.decode(get_locale_lang(), errors='ignore')


    WINDOWS_ROOT = os.getcwd()+"\Windows"

print(WINDOWS_ROOT)