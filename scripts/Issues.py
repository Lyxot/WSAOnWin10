import os
import sys

# BODY = os.getenv("BODY")
BODY = '''### Arch

x64

### WSA Release Channel

Retail

### Root solution

Non-root

### GApps brand

MindTheGapps

### Remove Amazon

- [ ] Remove Amazon'''

list = BODY.split("\n\n")
for i in list:
    if "###" in i:
        list.remove(i)

if sys.argv[1] == "Custom Build":
    arch_dist = {"x64":"--arch x64", "arm64":"--arch arm64"}
    release_type_dist = {"Retail":"--release-type retail", "Release Preview":"--release-type RP", "Insider Slow":"--release-type WIS", "Insider Fast":"--release-type WIF"}
    root_sol_dist = {"Non-root":"--root-sol none", "Magisk Stable":"--root-sol magisk --magisk-ver stable", "Magisk Beta":"--root-sol magisk --magisk-ver beta", "Magisk Canary":"--root-sol magisk --magisk-ver canary", "Magisk Debug":"--root-sol magisk --magisk-ver debug", "KernelSU": "--root-sol kernelsu"}
    gapps_brand_dist = {"MindTheGapps":"--gapps-brand MindTheGapps", "OpenGApps":"--gapps-brand OpenGApps", "No GApps": "none"}

    arch = arch_dist[list[0]]
    release_type = release_type_dist[list[1]]
    root_sol = root_sol_dist[list[2]]
    gapps_brand = gapps_brand_dist[list[3]]
    if list[4] == "- [ ] Remove Amazon":
        remove_amazon = "--remove-amazon"
    else:
        remove_amazon = ""
    output = arch + " " + release_type + " " + root_sol + " " + gapps_brand + " " + remove_amazon

    
print(output)