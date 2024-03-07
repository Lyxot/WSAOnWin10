# WSAOnWin10
### WARNING: WSAOnWin10 will no longer be available after March 5, 2025. [Learn more](https://learn.microsoft.com/en-us/windows/android/wsa/).
### This Repository is based on [MagiskOnWSA](https://github.com/LSPosed/MagiskOnWSALocal) and [WSAPatch](https://github.com/cinit/WSAPatch), uses Gihub Actions to automatically integrate Magisk root and Google Apps into WSA and make it run on Windows 10
### This project only ensures stable running on Windows 10 (also can work on Windows 11 in theory), if you are using Windows 11, [WSA-Script](https://github.com/YT-Advanced/WSA-Script) is a better choice.
English | [简体中文](README.zh-CN.md) ([国内](https://gitee.com/A-JiuA/WSAOnWin10/blob/master/README.zh-CN.md))

<img src="https://img.shields.io/badge/docs-stable-lime"/> <img src="https://img.shields.io/github/license/Lyxot/WSAOnWin10"/> <img src="https://img.shields.io/github/downloads/Lyxot/WSAOnWin10/total"/> <a href="https://github.com/Lyxot/WSAOnWin10/releases"><img src="https://img.shields.io/github/stars/Lyxot/WSAOnWin10"/> <img src="https://img.shields.io/github/release/Lyxot/WSAOnWin10"/></a> <a href="builds.md"><img src="https://img.shields.io/badge/history%20builds-C95863"/></a>

**Download latest release [here](https://github.com/Lyxot/WSAOnWin10/releases), and find all builds [here](builds.md)**

---
## System Requirement

<center><table>
<thead>
  <tr>
    <th></th>
    <th><img src="https://upload.wikimedia.org/wikipedia/commons/thumb/e/e6/Windows_11_logo.svg/320px-Windows_11_logo.svg.png" style="width: 200px;"/></th>
    <th><img src="https://upload.wikimedia.org/wikipedia/commons/thumb/0/05/Windows_10_Logo.svg/320px-Windows_10_Logo.svg.png" style="width: 200px;"/></th>
  </tr>
</thead>
<tbody>
  <tr>
    <td><img style="float: right;"/><h4>Windows Build Number<h4></td>
    <td>Windows™ 11: 21H2 Build 22000.526 or higher</td>
    <td>Windows™ 10: 22H2 Build 10.0.19045.2311 or higher (Recommended)<br /> Windows™ 10: 20H2 Build 10.0.19042.2604 (Minimum) <br /><br /><b>To use WSA, you must install <a href="https://www.catalog.update.microsoft.com/Search.aspx?q=KB5014032" target="_blank" rel="noopener noreferrer">KB5014032</a> then install <a href="https://www.catalog.update.microsoft.com/Search.aspx?q=KB5022834" target="_blank" rel="noopener noreferrer">KB5022834</a> to use WSA on these Windows 10 builds<b><br /><br /><b></td>
  </tr>
  <tr>
    <td><img style="float: right;" /><h4>RAM<h4></td>
    <td colspan="2"><ul><li>8 GB (Minimum)</li><li>16 GB (Recommended)</li></ul></td>
  </tr>
  <tr>
    <td rowspan="2"><img style="float: right;" /><h4>Storage<h4></td>
  </tr>
  <tr>
     <td colspan="2"><b><i>Minimum Storage Requirements: You must have at least 10GB free on the system drive (C:\)<b><i></td>
  </tr>
  <tr>
    <td rowspan="5"><img style="float: left;" /><h4>Windows Features Needed<h4></td>
    <td colspan="2">Virtual Machine Platform Enabled : <b>Require!!</b></td>
  </tr>
  <tr>
    <td colspan="2">Windows Hypervisor Platform Enabled (Optional)</td>
  </tr>
  <tr>
    <td colspan="2">Windows Subsystem For Linux™ Enabled (Optional)</td>
  </tr>
  <tr>
    <td colspan="2">Hyper-V Enabled (Optional)</td>
  </tr>
  <tr>
    <td colspan="2"><b><i>These optional settings are for virtualization and provide components that are needed to run WSA. You can enable these settings by pressing the Windows Key + R on your keyboard and typing "OptionalFeatures.exe" into the box, pressing enter and selecting the features above followed by pressing apply<b><i></td>
  </tr>
  <tr>
    <td><img style="float: right;" /><h4>Virtualization<h4></td>
    <td colspan="2">The Computer must support virtualization (Intel VT-x/AMD-V) and be enabled in BIOS/UEFI and Optional Features. </br><br />Different motherboards/notebooks have different enabling methods, the specific method please go to the brand official website query, or search online </br> <h3><a href="https://support.microsoft.com/zh-cn/windows/%E5%9C%A8windows-11%E7%94%B5%E8%84%91%E4%B8%8A%E5%90%AF%E7%94%A8%E8%99%9A%E6%8B%9F%E5%8C%96-c5578302-6e43-4b4b-a449-8ced115f58e1" target="_blank" rel="noopener noreferrer">Guide on how to enable</a><h3></td>
  </tr>
</tbody>
</table>

## Installation
> **Note** : 
> If you have the official Windows Subsystem For Android™ installed, you must [completely uninstall](#uninstallation) it to use MagiskOnWSA. 

> In case you want to preserve your data from the previous installation (official or MagiskOnWSA), you can backup `%LOCALAPPDATA%\Packages\MicrosoftCorporationII.WindowsSubsystemForAndroid_8wekyb3d8bbwe\LocalCache\userdata.vhdx` before uninstallation and restore it after installation. For a more comprehensive and detailed guide, take a look at the [Backup and Restore section](#backup-and-restore-userdata)

1. Go to the [Releases page](https://github.com/Lyxot/WSAOnWin10/releases)
2. In the latest release, go to the Assets section and download the Windows Subsystem For Android™ version of your choosing (do not download "Source code")

> **Note** : 
> If you want to build your custom build, please open an [Issue](https://github.com/Lyxot/WSAOnWin10/issues/new?assignees=&labels=CustomBuild&projects=&template=CustomBuild.yml&title=Custom+Build)，and then download the Artifact from Github Actions. Please visit [Custom Build](#custom-build) for more information.

3. Check integrity of downloaded file
    - Press Win + X on your keyboard and select Windows™ Terminal (Admin) or Powershell (Admin) depending on the version of Windows™ you are running
    - Input the command below and press enter, replacing {X:\path\to\your\downloaded\archive\package} including the {} with the path of the downloaded archive package

    `cd "{X:\path\to\your\downloaded\archive\package}"`
    - Input the command below and press enter, replacing `WSA_2XXX.XXXXX.X.X_XXXX_Release-with-magisk-XXXXXXX-XXXXXX-MindTheGapps-XX.X` with the name of the archive package

    `certutil -hashfile "WSA_2XXX.XXXXX.X.X_XXXX_Release-with-magisk-XXXXXXX-XXXXXX-MindTheGapps-XX.X" SHA256`
    - Compare the SHA256 output with ones at [Releases page](https://github.com/Lyxot/WSAOnWin10/releases) or in the sha256-checksum.txt (if you download artifact from the Custom Build task).
    > **Note** :
    > If package don't have the same SHA-256 Hash, please download then check again. **DO NOT INSTALL!!!**
4. Extract the zip file
5. Delete the zip file
6. Move the newly extracted folder to a suitable location and rename it (Recommended), as you will need to keep the folder on your PC to use WSAOnWin10

> **Note** :  
> If you're updating WSA, merge the folders and replace the files for all items when asked. Please visit [Updating instructions](#updating) for more information.

7. Open the Windows Subsystem For Android™ folder: Search for and double-click `Run.bat`
   - If you previously have a MagiskOnWSA installation, it will automatically uninstall the previous one while preserving all user data and install the new one, so don't worry about your data.
   - If the popup windows disappear without asking administrative permission and Windows Subsystem For Android™ is not installed successfully, you should manually run Install.ps1 as administrator:
      
      - Press `Win+X` and select **Windows™ Terminal (Admin)**
      
      - Input the command below and press enter, replacing {X:\path\to\your\extracted\folder} including the {} with the path of the extracted folder
        ```Powershell
        cd "{X:\path\to\your\extracted\folder}"
        ```  
        
      - Input the command below and press enter   
        ```Powershell
        PowerShell.exe -ExecutionPolicy Bypass -File .\Install.ps1
        ```
        
      - The script will run and Windows Subsystem For Android™ will be installed
      - If this workaround does not work, your PC is not supported for WSA
      
8. Once the installation process completes, Windows Subsystem For Android™ will launch (if this is a first-time install, a window asking for consent to diagnositic information will be shown instead. Sometimes two identical windows will show, this is fine and nothing bad happens if you click OK in both windows)
9. Click on the PowerShell window, then press any key on the keyboard, the PowerShell window should close
10. Close File Explorer
11. **Enjoy**

### Notice (Applicable for both Windows 10 and 11):

1. You can NOT delete the Windows Subsystem For Android™ installation folder.
   What `Add-AppxPackage -Register .\AppxManifest.xml` does is to register an appx package with some existing unpackaged files,
   so you need to keep them as long as you want to use Windows Subsystem For Android™. 
   Check https://learn.microsoft.com/en-us/powershell/module/appx/add-appxpackage?view=windowsserver2022-ps for more details.
2. You need to register your Windows Subsystem For Android™ appx package before you can run Windows Subsystem For Android™. 
   For [WSAOnWin10](https://github.com/Lyxot/WSAOnWin10) and [MagiskOnWSALocal](https://github.com/LSPosed/MagiskOnWSALocal) users, you need to run `Run.bat` in the extracted dir.

   If the script fails, you can take the following steps for diagnosis (admin privilege required):
    1. Open a PowerShell window and change working directory to your Windows Subsystem For Android™ directory.
    
    2. Run the command below in PowerShell. This should fail with an ActivityID, which is a UUID required for the next step.
       ```Powershell
       Add-AppxPackage -ForceApplicationShutdown -ForceUpdateFromAnyVersion -Register .\AppxManifest.xml
       ```
       
    3. Run the command below in PowerShell. This should print the log of the failed operation.
       ```Powershell
       Get-AppPackageLog -ActivityID <UUID>
       ```
    4. Check the log for the reason of failure and fix it.

## Updating
### How do I update without losing any of my apps and data on Windows Subsystem for Android (WSA)

1. [Download the build](https://github.com/Lyxot/WSAOnWin10/releases) that you want to update to
2. Make sure Windows Subsystem For Android is not running (Click on "Turn off" in the WSA Settings and wait for the spinning loader to disappear)
2. Using 7-Zip, WinRAR or any other tool of choice, open the .zip file 
3. Within the .zip archive open the subfolder (Example: WSA_2XXX.XXXXX.X.X_XXXX_Release-with-magisk-XXXXXXX-XXXXXX-MindTheGapps-XX.X)
4. Select all the files that are within this subfolder and extract them to the current folder where the file for Windows Subsystem For Android are (the folder you extracted, and installed WSA from)
5. When prompted to replace folders, select "Do this for all current items" and click on "Yes" 
6. When prompted to replace files, click on "Replace the files in the destination"
7. Run  the ``Run.bat`` file
8. Launch Windows Subsystem For Android Settings app and go to the ``About`` tab using the sidebar
9. Check if the WSA version matches the latest version/ the version number that you want to update to

## Uninstallation
> **Note**: 
> 
> If you want to preseve your data, make a backup of the `%LOCALAPPDATA%\Packages\MicrosoftCorporationII.WindowsSubsystemForAndroid_8wekyb3d8bbwe\LocalCache\userdata.vhdx` file. After uninstalling, copy the VHDX file back to the `%LOCALAPPDATA%\Package\MicrosoftCorporationII.WindowsSubsystemForAndroid_8wekyb3d8bbwe\LocalCache` folder. For a more comprehensive and detailed guide, take a look at the [Backup and Restore section](#backup-and-restore-userdata) in this README markdown

- To remove WSA installed:

   - **1.)** Make sure that Windows Subsystem For Android™ is not running
   - **2.)** Search for ``Windows Subsystem For Android™ Settings`` using the built-in Windows Search, or through Add and Remove Programs and press uninstall
   - **3.)** Delete the WSA folder that extracted you extracted and Run.bat was run from to install WSA (MagiskOnWSA folder)
   - **4.)** Go to ``%LOCALAPPDATA%/Packages/`` and delete the folder named ``MicrosoftCorporationII.WindowsSubsystemForAndroid_8wekyb3d8bbwe``
            
      - If you get an error that states that the file(s) could not be deleted, make sure that WSA is turned off
     
- To remove WSA installed from the Microsoft Store: 
        
   - **1.)** Search for ``Windows Subsystem For Android™ Settings`` using the built-in Windows Search, or through Add and Remove Programs and press uninstall

## Backup and Restore Userdata
## Backing Up Your Userdata

In order to make a backup of your WSA data you must copy the Userdata.vhdx (which includes, but is not limited Android Apps and their data, settings etc.), located at `%LOCALAPPDATA%\Packages\MicrosoftCorporationII.WindowsSubsystemForAndroid_8wekyb3d8bbwe\LocalCache\userdata.vhdx`, to a safe location     

## Restoring Your Backup

Before attempting to restore your backup, you must remove WSA if installed. Then before you run the "Run.bat" script (to reinstall WSA after removing it), you need to remove these lines from Install.ps1: 

```pwsh
Start-Process "wsa://com.topjohnwu.magisk"
Start-Process "wsa://com.android.vending"
Start-Process "wsa://com.amazon.venezia"
Start-Process "wsa://com.android.settings"
``` 
After running the script, **DO NOT RUN WSA** at all, and go to `%localappdata%\Packages` and (if the folders do not exist, create them) in `MicrosoftCorporationII.WindowsSubsystemForAndroid_8wekyb3d8bbwe\LocalCache\` paste the `userdata.vhdx`

Now run WSA and your serdata should hopefully be restored

## Custom Build
| :exclamation: **Important:**  &nbsp;  `⚠️DO NOT FORK⚠️`               |
|------------------------------------------------------------------------|
|**This repository is designed specifically not to be forked. MagiskOnWSA and some of the various forks and clones that have sprung up on the platform (***potentially***) violate GitHub's Terms of Service due to abuse of GitHub Actions and have been ultimately warned, disabled or banned.**| 
|**Therefore, don't fork this repository unless you're a developer and want to modify the code itself and/or want to contribute to this Github repository.**|
|**If you want to create your Custom Build, please follow the instructions set out clearly, to avoid the repo from being taken down as a result of a misuse of Github Actions due to the large number of forks. AND ALSO if you want to build with Latest Insider version, please skip the first 7 steps**|


#### **1. Check the version from [Releases](https://github.com/Lyxot/WSAOnWin10/releases/) first. If it does not have the version you want, continue to follow this guide. If it does, then feel free to use those prebuild WSA builds**

#### **2. Open [this page directly](https://github.com/Lyxot/WSAOnWin10/issues/new?assignees=&labels=CustomBuild&projects=&template=CustomBuild.yml&title=Custom+Build) then choose the option that you want to build. Then you click "Submit New Issues" (green button) and wait.**
![image](https://github.com/Lyxot/WSAOnWin10/assets/34974508/771f3ef0-8a0f-4c0e-9092-8bf71117d685)

#### **3. After about 20 minutes, the bot will reply that the workflow have built successfully (like the picture below), OPEN THE LINK BELOW THE BOT COMMENT**
![image](https://github.com/Lyxot/WSAOnWin10/assets/34974508/9c1bbf14-2765-4754-81bc-342116933653)

#### **4. Download the package as artifact**
**DO NOT download it via multithread downloaders like IDM**

![image](https://github.com/Lyxot/WSAOnWin10/assets/34974508/ba0ccaa7-d3de-4f9c-88f9-8d1bcc373296)

#### **5. Install like normal using [the instructions](#installation) in this repository**

## How to Upload `icu.dll` and `winhttp.dll` from Windows 11 images
> `icu.dll` and `winhttp.dll` in Windows 11 images are the key to WSA running on Windows 10, because some functions do not exist the above dll files in Windows 10 images. All builds provided by this repository already contain the dll files mentioned above, as well as' WSAPatch.dll ', so you can ignore this section if you are just using the builds provided by this repository

This repository uses Issues and Github Actions to automatically fetch dll files in Windows 11 images and inject 'WSAPatch.dll'. Visit [this link](https://github.com/Lyxot/WSAOnWin10/tree/master/original_dll) to see the dll files already in the repository. If you wish to submit an updated dll file, follow these steps

> **Note**
> Please do not upload the dll file arbitrarily, and fill in the information correctly

#### **1. Visit [this link](https://github.com/Lyxot/WSAOnWin10/issues/new?assignees=&labels=UploadDll&projects=&template=UploadDll.yml&title=Upload+Original+Dll+File), then fill in the information according to the image. If you are sure about the information you fill in, select the 'Upload' check box; If you are not sure, do not select the 'Upload' check box. Then you click "Submit New Issues" (green button) and wait.**
![image](https://github.com/Lyxot/WSAOnWin10/assets/34974508/b0a69b64-88ed-44b3-bb33-dc02889276a2)

#### **2. After about 5 minutes, the bot will reply that the download have finished successfully (like the picture below), open the link below the bot comment to view the log. The files in Artifacts are the fetched dll files**
![image](https://github.com/Lyxot/WSAOnWin10/assets/34974508/815f5a86-cdcb-4c7e-ab5c-088129ac51fa)

#### **3. If you selected the 'Upload' check box, Github Actions will automatically upload fetched dll files. If you didn't, you can check the log and fetched dll files, and then repeat the steps above according to the situation**
> If you cannot provide the link of Windows 11 images, please fetch `icu.dll` and `winhttp.dll` manually, and then open a pull request.

## FAQ
**Help me, I am having problems with the MagiskOnWSA Builds**

- Open an [issue in Github](https://github.com/Lyxot/WSAOnWin10/issues) and describe the issue with sufficent detail

**Help me, I am having problems with installing Windows Subsystem For Android™ on Windows™ 10**

- I am not working on the patch, and nor claim to.  Open an [issue in Github](https://github.com/Lyxot/WSAOnWin10/issues), and I will try to assist you with the problem if possible. For full support visit the project homepage and open an [Issue](https://github.com/cinit/WSAPatch/issues/) there

**How do I get a logcat?**
- There are two ways:
   ```
   adb logcat
   ```
   or

-  Location in Windows ---> <br/> `%LOCALAPPDATA%\Packages\MicrosoftCorporationII.WindowsSubsystemForAndroid_8wekyb3d8bbwe\LocalState\diagnostics\logcat`

**Can I delete the installed folder?**

- No.

**How can I update Windows Subsystem For Android™ to a new version?**

- As Explained [Updating instructions](#updating). Download the [Windows Subsystem For Android™ Version](https://github.com/Lyxot/WSAOnWin10/releases) that you want to update to and replace the content of your previous installation and rerun `Install.ps1`. Don't worry, your data will be preserved

**How do I update Magisk?**

- Do the same as updating Windows Subsystem For Android™.  Wait for a new [MagiskOnWSA release](https://github.com/Lyxot/WSAOnWin10/releases) that includes the newer Magisk version, then follow the [Updating instructions](#updating) to update

**Can I pass SafetyNet/Play Integrity?**

- No. Virtual machines like Windows Subsystem For Android™ cannot pass these mechanisms on their own due to the lack of signing by Google. Passing requires more exotic (and untested) solutions like: <https://github.com/kdrag0n/safetynet-fix/discussions/145#discussioncomment-2170917>

**What is virtualization?**

- Virtualization is required to run virtual machines like Windows Subsystem For Android™.  `Run.bat` helps you enable it. After rebooting, re-run `Run.bat` to install Windows Subsystem For Android™.  If it's still not working, you have to enable virtualization in your BIOS/UEFI. Instructions vary by PC vendor, look for help online

**Can I remount system partition as read-write?**

- No. Windows Subsystem For Android™ is mounted as read-only by Hyper-V. You can, however, modify the system partition by creating a Magisk module, or by directly modifying the `system.img` file

**I cannot adb connect localhost:58526**

- Make sure developer mode is enabled. If the issue persists, check the IP address of Windows Subsystem For Android™ on the Settings ---> Developer page and try 

   ```
   adb connect ip:5555
   ```

**Magisk online module list is empty?**

- Magisk actively removes the online module repository. You can install the module locally or by 
  
   **Step 1** 
      
      adb push module.zip /data/local/tmp

   **Step 2**  

      adb shell su -c magisk --install-module /data/local/tmp/module.zip


**How do I uninstall Magisk?**

- Request, using [Issues](https://github.com/Lyxot/WSAOnWin10/issues/new?assignees=&labels=CustomBuild&projects=&template=CustomBuild.yml&title=Custom+Build), a Windows Subsystem For Android™ version that doesn't include Magisk from the [Releases page](https://github.com/Lyxot/WSAOnWin10/releases). Then follow the [Updating instructions](#updating)

**How to install KernelSU Manager?**

- Connect to WSA with ADB.
- Run the following command:

  `adb shell ksuinstall`
- If the installation completes successfully, the KernelSU Manager will launching.

## Star History

[![Star History Chart](https://api.star-history.com/svg?repos=Lyxot/WSAOnWin10&type=Date)](https://star-history.com/#Lyxot/WSAOnWin10&Date)

## Credits
- [Microsoft](https://apps.microsoft.com/store/detail/windows-subsystem-for-android%E2%84%A2-with-amazon-appstore/9P3395VX91NR): For providing Windows Subsystem For Android™ and related files. Windows Subsystem For Android™, Windows Subsystem For Android™ Logo, Windows™ 10 and Windows™ 11 Logos are trademarks of Microsoft Corporation. Microsoft Corporation reserves all rights to these trademarks. By downloading and installing Windows Subsystem For Android™, you agree to the [Terms and Conditions](https://support.microsoft.com/en-gb/windows/microsoft-software-license-terms-microsoft-windows-subsystem-for-android-cf8dfb03-ba62-4daa-b7f3-e2cb18f968ad) and [Privacy Policy](https://privacy.microsoft.com/en-gb/privacystatement)
- [Cinit and the WSAPatch Guide](https://github.com/cinit/WSAPatch): Many thanks for the comprehensive guide, files and support provided by Cinit and the contributers at the WSAPatch repository. Windows™ 10 Builds in this repo rely on the hard work of this project and  hence credit is given where due
- [StoreLib](https://github.com/StoreDev/StoreLib): API for downloading WSA
- [Magisk](https://github.com/topjohnwu/Magisk): The Magic Mask for Android
- [KernelSU](https://github.com/tiann/KernelSU): A Kernel based root solution for Android
- [MagiskOnWSALocal](https://github.com/LSPosed/MagiskOnWSALocal): Integrate Magisk root and Google Apps into WSA
- [WSA-Script](https://github.com/YT-Advanced/WSA-Script): Integrate Magisk root and Google Apps into WSA (Windows Subsystem for Android) with GitHub Actions

***The repository is provided as a utility.***

***Android is a trademark of Google LLC. Windows™ is a trademark of Microsoft LLC.***