import os
import sys

arch_dist = {"x64":"x64", "arm64":"arm64"}
release_type_dist = {"Retail":"retail", "Release Preview":"RP", "Insider Slow":"WIS", "Insider Fast":"WIF"}
root_sol_dist = {"Non-root":["none", "stable"], "Magisk Stable":["magisk", "stable"], "Magisk Beta":["magisk", "beta"], "Magisk Canary":["magisk", "canary"], "Magisk Debug":["magisk", "debug"], "KernelSU": ["kernelsu", "stable"]}
gapps_brand_dist = {"MindTheGapps":"MindTheGapps", "OpenGApps":"OpenGApps", "No GApps": "none"}

if sys.argv[1] == "Custom Build(workflow_dispatch)":
    list = []
    for i in sys.argv[2:]:
        list.append(i)
else:
    BODY = os.getenv("BODY")
    USERNAME = os.getenv("USERNAME")

    list = BODY.split("\n\n")
    for i in list:
        if "#" in i:
            list.remove(i)

if sys.argv[1] == "Custom Build" and len(list) != 5:
    if not (list[0] in arch_dist and list[1] in release_type_dist and list[2] in root_sol_dist and list[3] in gapps_brand_dist):
        os.system("echo isSuccess=false >> $GITHUB_OUTPUT")
        exit()
elif sys.argv[1] == "Upload Original Dll File" and len(list) != 7:
    if not (list[0] in arch_dist and list[2].isdigit() and list[4] in [".iso", ".wim", ".esd", ".vhdx", ".zip"]):
        os.system("echo isSuccess=false >> $GITHUB_OUTPUT")
        exit()
    

if sys.argv[1] == "Custom Build" or sys.argv[1] == "Custom Build(workflow_dispatch)":
    arch = arch_dist[list[0]]
    release_type = release_type_dist[list[1]]
    root_sol = root_sol_dist[list[2]][0]
    magisk_ver = root_sol_dist[list[2]][1]
    gapps_brand = gapps_brand_dist[list[3]]
    if sys.argv[1] == "Custom Build":
        remove_amazon = "--remove-amazon"
    elif sys.argv[1] == "Custom Build(workflow_dispatch)":
        if list[4] == "true":
            remove_amazon = "--remove-amazon"
        else:
            remove_amazon = " "
    os.system("echo arch='"+arch+"' >> $GITHUB_OUTPUT")
    os.system("echo release_type='"+release_type+"' >> $GITHUB_OUTPUT")
    os.system("echo root_sol='"+root_sol+"' >> $GITHUB_OUTPUT")
    os.system("echo magisk_ver='"+magisk_ver+"' >> $GITHUB_OUTPUT")
    os.system("echo gapps_brand='"+gapps_brand+"' >> $GITHUB_OUTPUT")
    os.system("echo remove_amazon='"+remove_amazon+"' >> $GITHUB_OUTPUT")
elif sys.argv[1] == "Upload Original Dll File":
    os.system("echo arch='"+list[0]+"' >> $GITHUB_OUTPUT")
    os.system("echo version='"+list[1]+"' >> $GITHUB_OUTPUT")
    os.system("echo build='"+list[2]+"' >> $GITHUB_OUTPUT")
    os.system("echo url='"+list[3]+"' >> $GITHUB_OUTPUT")
    os.system("echo format='"+list[4]+"' >> $GITHUB_OUTPUT")
    os.system("echo email='"+list[5]+"' >> $GITHUB_OUTPUT")
    os.system("echo username='"+USERNAME+"' >> $GITHUB_OUTPUT")
    if list[6] == "- [ ] Upload":
        os.system("echo upload=false >> $GITHUB_OUTPUT")
    else:
        os.system("echo upload=true >> $GITHUB_OUTPUT")

os.system("echo isSuccess=true >> $GITHUB_OUTPUT")