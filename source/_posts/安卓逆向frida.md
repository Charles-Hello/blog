---
title: 安卓逆向frida
date: 2023-07-11 18:04:09
tags: [app逆向]
index_img: ../banner_images/banne_photo55.png
---


如果遇到root权限不行的话，尝试
如果在执行`adb shell su -c "/sdcard/temp/frida-server-14.2.17-android-arm64"`命令时收到"Permission denied"错误消息，说明没有执行该文件的权限。

这可能是因为在某些设备上，`/sdcard`目录默认不允许执行文件。你可以尝试将`frida-server`文件移动到其他位置，如`/data/local/tmp`目录，并尝试执行以下命令：


```
adb push frida-server-16.0.19-android-arm64 /sdcard/temp/
adb shell su -c "mv /sdcard/temp/frida-server-16.0.19-android-arm64 /data/local/tmp/frida-server"
adb shell su -c "chmod +x /data/local/tmp/frida-server"
adb shell su -c "/data/local/tmp/frida-server"
```


杀死frida-server
adb shell su -c "ps | grep frida-server"
adb shell su -c "kill -9 20607"

frida -U com.example.one_xposed -l jichu.js

注意了，必须要hook到包名正确，不然找人安卓手机重启



启动注入

frida -U com.example.one_xposed2 -l 02java.js --no-pause（）
我注意到在 Frida 15.2.2（可能在 15.2 中引入）中，应用程序在启动时默认不再暂停。  
因此，您不再需要 --no-pause 参数。

如果您确实想在启动时暂停应用程序，可以使用 --pause



问题1  
{'type': 'error', 'description': "ReferenceError: 'java' is not defined", 'stack': "ReferenceError: 'java' is not defined\n    at main (/script1.js:2)\n    at apply (native)\n    at <anonymous> (frida/runtime/core.js:51)", 'fileName': '/script1.js', 'lineNumber': 2, 'columnNumber': 1}
在js中的java要用大写的Java来表示


对抗检测  启动不同的端口

杀死frida-server
adb shell su -c "ps | grep frida-server"
adb shell su -c "kill -9 20607"

adb shell su -c "/data/local/tmp/frida-server -l 0.0.0.0:1234"  
frida -H 127.0.0.1:1234 -l jdclass.js -f com.jingdong.app.mall