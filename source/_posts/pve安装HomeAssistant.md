---
title: pve安装HomeAssistant
date: 2023-08-29 22:16:47
tags: []
index_img: ../banner_images/banne_photo38.png
---

[Installation - Home Assistant (home-assistant.io)](https://www.home-assistant.io/installation/)
打开HomeAssistant官方，点击
![](../images/Pasted%20image%2020230829221734.png)

![](../images/Pasted%20image%2020230829221754.png)
下载kvm，然后ssh连接pve终端，导入进去

接下来看这个教程
[Proxmox VE（PVE）安装HomeAssistant - 北极星小队 (wink98.top)](http://blog.wink98.top/index.php/archives/222.html#:~:text=%E5%9B%9E%E5%88%B0pve%EF%BC%8C%E7%82%B9%E5%87%BB%E5%B7%A6%E4%BE%A7%E7%9A%84%E8%8A%82%E7%82%B9%EF%BC%88%E4%B8%8D%E6%98%AF%E8%99%9A%E6%8B%9F%E6%9C%BA%EF%BC%89%EF%BC%8C%E9%80%89%E6%8B%A9shell%20%E8%BE%93%E5%85%A5cd%20%2Ftmp%EF%BC%8Ccd%E5%88%B0tmp%E7%9B%AE%E5%BD%95%EF%BC%8C%E4%B9%9F%E5%B0%B1%E6%98%AF%E5%88%9A%E5%88%9A%E8%99%9A%E6%8B%9F%E6%9C%BA%E6%96%87%E4%BB%B6%E4%B8%8A%E4%BC%A0%E7%9A%84%E6%96%87%E4%BB%B6%E5%A4%B9%20%E8%BE%93%E5%85%A5%E5%AF%BC%E5%85%A5%E5%91%BD%E4%BB%A4qm%20importdisk%20101%20haos_ova-8.0.rc1.qcow2,local-lvm%2017%E3%80%81%E5%AF%BC%E5%85%A5%E5%AE%8C%E6%88%90%EF%BC%8C%E5%A6%82%E4%B8%8B%E5%9B%BE%E6%89%80%E7%A4%BA%EF%BC%8C%E5%8D%B3%E8%A1%A8%E7%A4%BA%E5%AF%BC%E5%85%A5%E6%88%90%E5%8A%9F%2018%E3%80%81%E6%B7%BB%E5%8A%A0%E7%A1%AC%E7%9B%98%EF%BC%8C%E7%82%B9%E5%87%BBpve%E5%B7%A6%E4%BE%A7%E6%96%B0%E5%BB%BA%E7%9A%84hassOS%E8%99%9A%E6%8B%9F%E6%9C%BA%EF%BC%8C%E5%9C%A8%E5%8F%B3%E4%BE%A7%E9%80%89%E6%8B%A9%E7%A1%AC%E4%BB%B6%EF%BC%8C%E4%BC%9A%E5%8F%91%E7%8E%B0%E5%87%BA%E7%8E%B0%E4%B8%80%E4%B8%AA%E6%9C%AA%E4%BD%BF%E7%94%A8%E7%9A%84%E7%A3%81%E7%9B%980%EF%BC%8C%E9%80%89%E6%8B%A9%E7%BC%96%E8%BE%91%EF%BC%8C%E9%BB%98%E8%AE%A4%E6%B7%BB%E5%8A%A0%E5%8D%B3%E5%8F%AF%2019%E3%80%81%E6%9B%B4%E6%94%B9%E5%BC%95%E5%AF%BC%E9%A1%BA%E5%BA%8F%EF%BC%8C%E5%90%AF%E7%94%A8%E7%A1%AC%E7%9B%98%E5%BC%95%E5%AF%BC%EF%BC%8C%E5%B9%B6%E5%B0%86%E5%85%B6%E6%8B%96%E8%87%B3%E9%A6%96%E4%BD%8D%2020%E3%80%81%E5%90%AF%E5%8A%A8hassOS%E8%99%9A%E6%8B%9F%E6%9C%BA%2021%E3%80%81%E7%AD%89%E5%BE%85%E7%B3%BB%E7%BB%9F%E6%9C%80%E5%90%8E%E5%AE%89%E8%A3%85%E5%AE%8C%E6%88%90%EF%BC%8C%E6%89%93%E5%BC%80%E7%BD%91%E9%A1%B5%E7%AB%AF%EF%BC%8C%E6%B5%8F%E8%A7%88%E5%99%A8%E9%87%8C%E9%9D%A2%E8%BE%93%E5%85%A5%E8%BF%99%E4%B8%AA%E7%BD%91%E5%9D%80%E5%B9%B6%E6%89%93%E5%BC%80%EF%BC%9A%20http%3A%2F%2Fhomeassistant.local%3A8123)

输入这个命令qm importdisk 106 haos_ova-10.5.qcow2 local-lvm
然后启动。
如果没有科学的话。
在看[Home Assistant虚拟机版，修改ip地址和网关 - 哔哩哔哩 (bilibili.com)](https://www.bilibili.com/read/cv17123823/)
然后看[Home Assistant](http://192.168.1.60:8123/onboarding.html)点击登录即可


还是建议搭建samba
![](../images/Pasted%20image%2020230829231749.png)
忘记密码的可以删除这个文件夹，重启ha再注册
