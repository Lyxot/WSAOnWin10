# WSAOnWin10
### 本项目基于 [MagiskOnWSA](https://github.com/LSPosed/MagiskOnWSALocal) 与 [WSAPatch](https://github.com/cinit/WSAPatch)，使用 Github Actions 自动构建 WSA，整合 Magisk、Google Apps 并使其可以在 Windows 10 上运行
### 本项目仅确保在 Windows 10 上的稳定运行(Windows 11 理论上也能用)，如果您是 Windows 11 用户，最好使用 [WSA-Script](https://github.com/YT-Advanced/WSA-Script)
[English](README.md) | 简体中文 ([国内](https://gitee.com/A-JiuA/WSAOnWin10/blob/master/README.zh-CN.md))

<img src="https://img.shields.io/badge/docs-stable-lime"/> <img src="https://img.shields.io/github/license/A-JiuA/WSAOnWin10"/> <img src="https://img.shields.io/github/downloads/A-JiuA/WSAOnWin10/total"/> <img src="https://img.shields.io/github/stars/A-JiuA/WSAOnWin10"/> <img src="https://img.shields.io/github/release/A-JiuA/WSAOnWin10"/>

---
## 系统要求

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
    <td><img style="float: right;"/><h4>Windows 版本<h4></td>
    <td>Windows™ 11: 21H2 Build 22000.526 或更高</td>
    <td>Windows™ 10: 22H2 Build 10.0.19045.2311 或更高 (推荐)<br /> Windows™ 10: 20H2 Build 10.0.19042.2604 (最低) <br /><br /><b>请确保安装了 <a href="https://www.catalog.update.microsoft.com/Search.aspx?q=KB5014032" target="_blank" rel="noopener noreferrer">KB5014032</a> 及 <a href="https://www.catalog.update.microsoft.com/Search.aspx?q=KB5022834" target="_blank" rel="noopener noreferrer">KB5022834</a> 补丁<b><br /><br /><b></td>
  </tr>
  <tr>
    <td><img style="float: right;" /><h4>内存<h4></td>
    <td colspan="2"><ul><li>8 GB (最低配置)</li><li>16 GB (推荐配置)</li></ul></td>
  </tr>
  <tr>
    <td rowspan="2"><img style="float: right;" /><h4>储存<h4></td>
  </tr>
  <tr>
     <td colspan="2"><b><i>最小空间需求: C盘上至少有10GB的可用空间<b><i></td>
  </tr>
  <tr>
    <td rowspan="5"><img style="float: left;" /><h4>Windows 功能<h4></td>
    <td colspan="2">虚拟机平台 : <b>必选!!</b></td>
  </tr>
  <tr>
    <td colspan="2">Windows 虚拟机监控程序平台 (可选)</td>
  </tr>
  <tr>
    <td colspan="2">适用于 Linux 的 Windows 子系统 (可选)</td>
  </tr>
  <tr>
    <td colspan="2">Hyper-V (可选)</td>
  </tr>
  <tr>
    <td colspan="2"><b><i>这些可选功能用于设置虚拟化，并提供运行WSA所需的组件。您可以通过按键盘上的Windows键+ R并在框中键入“OptionalFeatures.exe”后回车，启用上述功能，然后按确定并重启<b><i></td>
  </tr>
  <tr>
    <td><img style="float: right;" /><h4>虚拟化<h4></td>
    <td colspan="2">您的电脑必须支持硬件虚拟化技术 (Intel VT-x/AMD-V)，并在 BIOS/UEFI 启用它们 </br><br />不同的主板/笔记本有不同的启用方法，具体的方法请前往品牌官网查询，或百度搜索型号+虚拟化 </br> <h3><a href="https://support.microsoft.com/zh-cn/windows/%E5%9C%A8windows-11%E7%94%B5%E8%84%91%E4%B8%8A%E5%90%AF%E7%94%A8%E8%99%9A%E6%8B%9F%E5%8C%96-c5578302-6e43-4b4b-a449-8ced115f58e1" target="_blank" rel="noopener noreferrer">如何启用</a><h3></td>
  </tr>
</tbody>
</table>

## 安装
> **注意** : 
> 如果你已经安装了官方WSA，你必须[完全卸载](#卸载)它来使用本项目构建的WSA

> 如果你想要保留数据 (官方 或 MagiskOnWSA)，你可以在卸载前备份 `%LOCALAPPDATA%\Packages\MicrosoftCorporationII.WindowsSubsystemForAndroid_8wekyb3d8bbwe\LocalCache\userdata.vhdx` 并在安装后恢复它。查看[**备份与恢复**](#备份与恢复)来获得更全面和详细的教程

1. 访问 [Releases 页面](https://github.com/A-JiuA/WSAOnWin10/releases)
2. 在最新的 Release 中，点击 Assets 并下载你选择的 Windows Subsystem For Android™ 版本 (不要下载 "Source code")

> **注意** : 
> 如果你想要使用自定义构建，请访问 [Issues](https://github.com/A-JiuA/WSAOnWin10/issues/new?assignees=&labels=CustomBuild&projects=&template=CustomBuild.yml&title=Custom+Build) 提交申请，然后从Github Actions下载安装包。详情请访问[自定义构建](#自定义构建)

3. 检查安装包完整性
    - 按键盘上的Windows键+ X并根据你的系统点击 Windows Terminal (管理员) 或 Powershell (管理员)
    - 输入下方的命令，将 `{X:\path\to\your\downloaded\archive\package}` (包括`{}`) 替换为你下载安装包的目录，回车

    `cd "{X:\path\to\your\downloaded\archive\package}"`
    - 输入下方的命令，将 `WSA_2XXX.XXXXX.X.X_XXXX_Release-with-magisk-XXXXXXX-XXXXXX-MindTheGapps-XX.X` 替换为你下载安装包的文件名，回车

    `certutil -hashfile "WSA_2XXX.XXXXX.X.X_XXXX_Release-with-magisk-XXXXXXX-XXXXXX-MindTheGapps-XX.X" SHA256`
    - 对比输出的哈希值与 [Release 页面](https://github.com/A-JiuA/WSAOnWin10/releases)中的哈希值，或 Artifacts 中的 `sha256-checksum.txt` 中的哈希值
    > **注意** : 
    > 如果哈希值不一致，请尝试重新下载安装包，**不要安装!!!**
4. 解压安装包
5. 删除安装包(可选)
6. 移动解压出来的文件夹到一个固定的位置并重命名 (推荐)， 因为你需要保留这个文件夹来使用 WSA

> **注意** :  
> 如果你正在升级WSA，移动文件夹并替换所有文件，详见[升级](#升级)

7. 打开文件夹， 双击 `Run.bat`
   - 如果你已经安装过 `MagiskOnWSA`，脚本将自动卸载旧版 WSA 并保留用户数据，然后安装更新，不必为您的数据担心
   - 如果弹出的命令行窗口消失了，没有申请管理员权限且 WSA 没有成功安装，您需要手动以管理员身份运行`Install.ps1`:
      
      - 按键盘上的Windows键+ X并根据你的系统点击 Windows Terminal **(管理员)** 或 Powershell **(管理员)**
      
      - 输入下方的命令，将 `{X:\path\to\your\extracted\folder}` (包括`{}`) 替换为你解压安装包的目录，回车
        ```Powershell
        cd "{X:\path\to\your\extracted\folder}"
        ```  
        
      - 输入下方的命令并回车   
        ```Powershell
        PowerShell.exe -ExecutionPolicy Bypass -File .\Install.ps1
        ```
        
      - 脚本将自动安装 WSA
      - 如果这个方法没有效果，您的电脑不支持 WSA
      
8. 安装完成后，WSA 将启动 (如果这是第一次安装，则会显示一个请求同意诊断信息的窗口。有时会显示两个相同的窗口，这是正常的，请在两个窗口中都单击OK)
9. 单击 PowerShell 窗口，按任意键退出安装脚本
10. 关闭文件资源管理器
11. **Enjoy**

**注意 (对 Windows 10 和 11 都适用):**

1. 您不能删除安装文件夹。
   命令 `Add-AppxPackage -Register .\AppxManifest.xml` 做的是使用一些解压过后的文件来注册 appx 包，所以您需要一直保留这个文件夹直到您想要卸载 WSA
   访问 https://learn.microsoft.com/zh-cn/powershell/module/appx/add-appxpackage?view=windowsserver2022-ps 获取更多信息
2. 您需要注册 WSA appx 包才可以运行 WSA。 
   对于 [WSAOnWin10](https://github.com/A-JiuA/WSAOnWin10) 和 [MagiskOnWSALocal](https://github.com/LSPosed/MagiskOnWSALocal) 用户，您需要运行解压文件夹中的 `Run.bat`
   
   如果脚本不工作，您可以使用下列步骤进行诊断 (需要管理员权限):
    1. 打开 PowerShell 将工作目录改为您的 WSA 安装文件夹
    
    2. 运行下方的命令，它将报错并给出一个 ActivityID，就是下一步所需的 UUID
       ```Powershell
       Add-AppxPackage -ForceApplicationShutdown -ForceUpdateFromAnyVersion -Register .\AppxManifest.xml
       ```
       
    3. 运行下方的命令，它将显示失败操作的日志
       ```Powershell
       Get-AppPackageLog -ActivityID <UUID>
       ```
    4. 检查日志中的错误并修复它

## 升级
### 如何升级 WSA 并保留用户数据

1. 下载你希望升级到的[版本](https://github.com/A-JiuA/WSAOnWin10/releases)
2. 确保 WSA 没有在运行 (在`适用于 Android™ 的 Windows 子系统`中单击关闭子系统，直到旋转的加载条消失)
2. 使用 7-Zip，WinRAR 或任何其它工具打开 .zip 压缩包 
3. 在.zip 压缩包中打开子文件夹 (比如: WSA_2XXX.XXXXX.X.X_XXXX_Release-with-magisk-XXXXXXX-XXXXXX-MindTheGapps-XX.X)
4. 选择子文件夹中的所有文件，将它们解压到你的 WSA 所处的目录 (你解压并安装 WSA 的目录)
5. 当提示是否替换文件时，选择“替换目标中的文件”并确定
6. 双击运行 `Run.bat`
7. 启动`适用于 Android™ 的 Windows 子系统`，点击侧边栏中的 `关于`
8. 检查 WSA 版本是否为你想要升级到的版本

## 卸载
> **注意**: 
> 
> 如果你想要保留你的用户数据，备份 `%LOCALAPPDATA%\Packages\MicrosoftCorporationII.WindowsSubsystemForAndroid_8wekyb3d8bbwe\LocalCache\userdata.vhdx`。 在卸载后，将 VHDX 文件复制回 `%LOCALAPPDATA%\Package\MicrosoftCorporationII.WindowsSubsystemForAndroid_8wekyb3d8bbwe\LocalCache` 文件夹。查看[**备份与恢复**](#备份与恢复)来获得更全面和详细的教程

- 对于使用脚本安装的 WSA:

   - **1.)** 确保 WSA 没有在运行
   - **2.)** 使用 Windows 内置搜索搜索 `适用于 Android™ 的 Windows 子系统`或使用`添加或删除程序`，点击卸载
   - **3.)** 删除安装文件夹 (MagiskOnWSA 文件夹)
   - **4.)** 删除 ``%LOCALAPPDATA%/Packages/`` 中的 ``MicrosoftCorporationII.WindowsSubsystemForAndroid_8wekyb3d8bbwe`` 文件夹
            
      - 如果系统报错，提示无法删除文件，确保 WSA 没有在运行
     
- 对于从 Microsoft Store 安装的 WSA: 
        
   - **1.)** 使用 Windows 内置搜索搜索 `适用于 Android™ 的 Windows 子系统`或使用`添加或删除程序`，点击卸载

## 备份与恢复
### 备份您的用户数据

为了备份用户数据，您必须复制位于 `%LOCALAPPDATA%\Packages\MicrosoftCorporationII.WindowsSubsystemForAndroid_8wekyb3d8bbwe\LocalCache\userdata.vhdx` 的 `Userdata.vhdx` (存储包含但不仅限于 Android Apps 和它们的数据，设置等等的文件) 到一个安全的位置   

### 恢复您的备份

在您尝试恢复备份前，您必须卸载 WSA (如果你安装了)。在您运行 `Run.bat` 脚本前 (在卸载 WSA 后重新安装它)，您需要删除 `Install.ps1` 中的这些行，它们大约位于第57行: 

```pwsh
Start-Process "wsa://com.topjohnwu.magisk"
Start-Process "wsa://com.android.vending"
Start-Process "wsa://com.amazon.venezia"
Start-Process "wsa://com.android.settings"
``` 
在脚本运行完成后，请**不要运行 WSA**，访问 `%localappdata%\Packages` 中的 `MicrosoftCorporationII.WindowsSubsystemForAndroid_8wekyb3d8bbwe\LocalCache\` 文件夹 (如果文件夹不存在，请创建它们) 粘贴 `userdata.vhdx`

现在运行 WSA， 您的数据应该被恢复了

## 自定义构建
|  **重要:**  &nbsp;  `⚠️不要 FORK⚠️`               |
|------------------------------------------------------------------------|
|**这个 Repository 被特别设计为不被 fork。MagiskOnWSA和一些在平台上涌现的各种分支和克隆(***可能***)违反了 GitHub 的服务条款，由于滥用 GitHub Actions 的行为，最终被警告，禁用或禁止**| 
|**因此，除非你是开发人员，想要修改代码本身，或想要为这个 Github Repository 做出贡献，否则不要 fork 这个 Repository**|
|**如果您想创建自定义构建，请遵循下列说明，以避免由于大量 fork 而导致 Github Actions 被滥用而导致 Repository 被关闭。**|


#### **1. 首先检查 [Releases 页面](https://github.com/A-JiuA/WSAOnWin10/releases/)中的构建。如果不包含你想要的构建，继续跟随这个教程。如果包含，请使用那些预构建的 WSA**

#### **2. 访问[这个链接](https://github.com/A-JiuA/WSAOnWin10/issues/new?assignees=&labels=CustomBuild&projects=&template=CustomBuild.yml&title=Custom+Build)，然后根据你想要的构建填写信息，点击 `Submit New Issues` (绿色按钮) 并等待**
![image](https://github.com/A-JiuA/WSAOnWin10/assets/34974508/771f3ef0-8a0f-4c0e-9092-8bf71117d685)


#### **3. 大约20分钟后，github-actions[bot] 会回复你的构建已完成 (如下图)，打开回复中的链接**
![image](https://github.com/A-JiuA/WSAOnWin10/assets/34974508/9c1bbf14-2765-4754-81bc-342116933653)


#### **4. 下载 `Artifacts` 中的文件**
**不要使用多线程下载器下载构建，如 IDM**

![image](https://github.com/A-JiuA/WSAOnWin10/assets/34974508/ba0ccaa7-d3de-4f9c-88f9-8d1bcc373296)


#### **5. 参照[安装](#安装)章节进行安装**

## 提交 Windows 11 镜像中的 `icu.dll` 与 `winhttp.dll`
> Windows 11 镜像中 `icu.dll` 与 `winhttp.dll` 是 WSA 在 Windows 10 上运行的关键，因为 Windows 10 中的上述 dll 文件缺少符号。本仓库提供的所有构建均已包含上述 dll 文件，以及 `WSAPatch.dll`，如果您只是使用本仓库提供的构建，则可以忽略本章节

本仓库使用 Issues 和 Github Actions 自动获取 Windows 11 镜像中的 dll 文件并注入 `WSAPatch.dll`，访问[这个链接](https://github.com/A-JiuA/WSAOnWin10/tree/master/original_dll)可以查看仓库中已有的 dll 文件。如果您希望提交更新 dll 文件，请按照以下步骤进行操作

> **注意** : 
> 请不要胡乱提交 dll 文件，并正确填写相关信息

#### **1. 访问[这个链接](https://github.com/A-JiuA/WSAOnWin10/issues/new?assignees=&labels=UploadDll&projects=&template=UploadDll.yml&title=Upload+Original+Dll+File)，然后根据镜像填写相关信息。如果您对所填写的信息十分确定，勾选 `Upload` 复选框；如果您不能确定，请不要勾选 `Upload` 复选框。点击 `Submit New Issues` (绿色按钮) 并等待**
![image](https://github.com/A-JiuA/WSAOnWin10/assets/34974508/b0a69b64-88ed-44b3-bb33-dc02889276a2)

#### **2. 大约5分钟后，github-actions[bot] 会回复下载已完成 (如下图)，打开回复中的链接可以查看日志，`Artifacts` 中的文件为提取出的 dll 文件**
![image](https://github.com/A-JiuA/WSAOnWin10/assets/34974508/815f5a86-cdcb-4c7e-ab5c-088129ac51fa)

#### **3. 如果您勾选了 `Upload` 复选框，Github Actions 会将提取出的 dll 文件自动上传，无需其它操作。如果您没有勾选 `Upload` 复选框，可以对日志和提取出的 dll 文件进行检查，根据情况重新执行以上步骤**
> 如果您不能提供 Windows 11 镜像的链接，请手动提取 `icu.dll` 与 `winhttp.dll` 后提交 Pull Requests

## FAQ
**运行 WSA 出现问题？**

- 在 Github 上创建一个 [Issue](https://github.com/A-JiuA/WSAOnWin10/issues) 并详细描述您遇到的问题

**在 Windows 10 上运行 WSA 出现问题？**

- `WSAPatch` 项目并不是由我维护的。在 Github 上创建一个 [Issue](https://github.com/A-JiuA/WSAOnWin10/issues)，我会尽力协助你解决问题。要获得全面支持，请访问项目主页并在那里提交一个 [Issue](https://github.com/cinit/WSAPatch/issues/)

**如何获取 logcat？**
- 有两种方法:
   ```
   adb logcat
   ```
   或

-  Windows 目录中的
   ```%LOCALAPPDATA%\Packages\MicrosoftCorporationII.WindowsSubsystemForAndroid_8wekyb3d8bbwe\LocalState\diagnostics\logcat```

**我可以删除安装文件夹吗？**

- 不能

**如何将 WSA 升级到新版本？**

- 正如[升级](#升级)章节中所描述。下载你希望升级到的[版本](https://github.com/A-JiuA/WSAOnWin10/releases) 然后替换你之前的安装文件夹，重新运行`Install.ps1`。不必担心，你的数据将会被保留

**如何升级 Magisk？**

- 与升级 WSA 相同。等待一个包含更新版本 Magisk 的 WSAOnWin10 [版本](https://github.com/A-JiuA/WSAOnWin10/releases)，然后参照[升级](#升级)章节

**能否通过 SafetyNet/Play Integrity？**

- 不能。由于缺乏 Google 的签名，像 WSA 这样的虚拟机不能直接通过这些机制。需要其它的解决方法来通过 (未测试)，比如: <https://github.com/kdrag0n/safetynet-fix/discussions/145#discussioncomment-2170917>

**什么是虚拟化?**

- 运行像 WSA 这样的虚拟机需要虚拟化。`Run.bat` 可以帮助您启用它。重新启动后，重新运行 `Run.bat` 来安装 WSA。如果它仍然不能工作，您必须在BIOS/UEFI中启用虚拟化。具体方法因PC厂商而异，请在网上寻求帮助

**我能否以读写模式挂载 system 分区**

- 不能。WSA 被 Hyper-V 以只读模式挂载。然而，您可以通过创建一个 Magisk module 来修改 system 分区，或直接修改 `system.img` 文件

**我无法运行 `adb connect localhost:58526`**

- 确保开发人员模式已启用。 如果问题依旧，在 `适用于 Android™ 的 Windows 子系统` ---> 高级设置 中检查 WSA 的 IP 地址，然后尝试

   ```
   adb connect ip:5555
   ```

**Magisk 在线模块列表是空的？**

- Magisk主动移除了在线模块存储库。您可以在本地安装 Magisk module 或通过以下步骤安装
  
   **步骤 1** 
      
      adb push module.zip /data/local/tmp

   **步骤 2**  

      adb shell su -c magisk --install-module /data/local/tmp/module.zip


**如何卸载 Magisk？**

- 在 [Releases 页面](https://github.com/A-JiuA/WSAOnWin10/releases)中下载一个不包含 Magisk 的构建，或使用 [Issues](https://github.com/A-JiuA/WSAOnWin10/issues/new?assignees=&labels=CustomBuild&projects=&template=CustomBuild.yml&title=Custom+Build) 创建一个[自定义构建](#自定义构建)，然后参照[升级](#升级)章节

**如何安装 KernelSU Manager**

- 使用 ADB 连接 WSA，运行下列命令

  `adb shell ksuinstall`
- 如果安装成功，KernelSU Manager 将会自动启动

## 致谢
- [Microsoft](https://apps.microsoft.com/store/detail/windows-subsystem-for-android%E2%84%A2-with-amazon-appstore/9P3395VX91NR): For providing Windows Subsystem For Android™ and related files. Windows Subsystem For Android™, Windows Subsystem For Android™ Logo, Windows™ 10 and Windows™ 11 Logos are trademarks of Microsoft Corporation. Microsoft Corporation reserves all rights to these trademarks. By downloading and installing Windows Subsystem For Android™, you agree to the [Terms and Conditions](https://support.microsoft.com/en-gb/windows/microsoft-software-license-terms-microsoft-windows-subsystem-for-android-cf8dfb03-ba62-4daa-b7f3-e2cb18f968ad) and [Privacy Policy](https://privacy.microsoft.com/en-gb/privacystatement)
- [Cinit and the WSAPatch Guide](https://github.com/cinit/WSAPatch): Many thanks for the comprehensive guide, files and support provided by Cinit and the contributers at the WSAPatch repository. Windows™ 10 Builds in this repo rely on the hard work of this project and  hence credit is given where due
- [StoreLib](https://github.com/StoreDev/StoreLib): API for downloading WSA
- [Magisk](https://github.com/topjohnwu/Magisk): The Magic Mask for Android
- [KernelSU](https://github.com/tiann/KernelSU): A Kernel based root solution for Android
- [MagiskOnWSALocal](https://github.com/LSPosed/MagiskOnWSALocal): Integrate Magisk root and Google Apps into WSA
- [WSA-Script](https://github.com/YT-Advanced/WSA-Script): Integrate Magisk root and Google Apps into WSA (Windows Subsystem for Android) with GitHub Actions

***The repository is provided as a utility.***

***Android is a trademark of Google LLC. Windows™ is a trademark of Microsoft LLC.***
