import os
import sys



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

if sys.argv[1] == "Custom Build" or sys.argv[1] == "Custom Build(workflow_dispatch)":
    arch_dist = {"x64":"--arch x64", "arm64":"--arch arm64"}
    release_type_dist = {"Retail":"--release-type retail", "Release Preview":"--release-type RP", "Insider Slow":"--release-type WIS", "Insider Fast":"--release-type WIF"}
    root_sol_dist = {"Non-root":"--root-sol none", "Magisk Stable":"--root-sol magisk --magisk-ver stable", "Magisk Beta":"--root-sol magisk --magisk-ver beta", "Magisk Canary":"--root-sol magisk --magisk-ver canary", "Magisk Debug":"--root-sol magisk --magisk-ver debug", "KernelSU": "--root-sol kernelsu"}
    gapps_brand_dist = {"MindTheGapps":"--gapps-brand MindTheGapps", "OpenGApps":"--gapps-brand OpenGApps", "No GApps": "none"}

    arch = arch_dist[list[0]]
    release_type = release_type_dist[list[1]]
    root_sol = root_sol_dist[list[2]]
    gapps_brand = gapps_brand_dist[list[3]]
    if sys.argv[1] == "Custom Build":
        if list[4] == "- [ ] Remove Amazon":
            remove_amazon = ""
        else:
            remove_amazon = "--remove-amazon"
    elif sys.argv[1] == "Custom Build(workflow_dispatch)":
        if list[4] == "true":
            remove_amazon = "--remove-amazon"
        else:
            remove_amazon = ""
    output = arch + " " + release_type + " " + root_sol + " " + gapps_brand + " " + remove_amazon
    os.system("echo cmd="+output+" >> $GITHUB_OUTPUT")
    os.system("echo arch="+arch+" >> $GITHUB_OUTPUT")
elif sys.argv[1] == "Upload Original Dll File":
    os.system("echo 'arch="+list[0]+"' >> $GITHUB_OUTPUT")
    os.system("echo 'version="+list[1]+"' >> $GITHUB_OUTPUT")
    os.system("echo 'build="+list[2]+"' >> $GITHUB_OUTPUT")
    os.system("echo 'url="+list[3]+"' >> $GITHUB_OUTPUT")
    os.system("echo 'format="+list[4]+"' >> $GITHUB_OUTPUT")
    os.system("echo 'email="+list[5]+"' >> $GITHUB_OUTPUT")
    os.system("echo 'username="+USERNAME+"' >> $GITHUB_OUTPUT")
    if list[6] == "- [ ] Upload":
        os.system("echo upload=false >> $GITHUB_OUTPUT")
    else:
        os.system("echo upload=true >> $GITHUB_OUTPUT")