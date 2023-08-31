---
title: Stream抓京东wskey
date: 2023-06-01 15:55:18
tags: []
index_img: /images/Pasted%20image%2020230601155534.png
---

**步骤1 启动抓包**，下图点击圈1开始抓包

![](../images/DC1188E8-F2DD-4E61-8893-81ECAA48A2B3_kcSNY1uULp.jpeg)

启动以后打开app，滑来滑去几十秒

## 步骤2:  抓京东的pin

然后回来stream，关闭抓包，找到上图的抓包历史

![](../images/42D6959B-9932-43E0-A97D-E535E83674F3_c32pc08Fx8.jpeg)

点击搜索，输入pt\_pin

这个时候随便点击一个抓包请求点进去，如下图所示

![](../images/0F131827-24A6-422A-A223-B915D60E4839_rtxhG2phX7.jpeg)

复制圈中内容

例如:    pt\_pin=122272973-6464846;&#x20;

## 步骤3:  抓wskey

下图同理搜索wskey

![](../images/02B326C6-7792-4470-93EB-8C53F7958BAC_X1Y9pGLqWR.jpeg)

随便点开一个包，如下图所示

![](../images/1184CADF-FBB7-4547-8910-FCA91189C5CC_FdGTuMozcf.jpeg)

复制圈内内容的wskey

例如:

wskey=AAJiltn9AEC6r3vDa5q6k1zlGa49QSEpd3g64i1TEsoj06MyVQSOss1xkvvebSx9lv9H5sFc9LIND6w\_vLbvldr17s-R806q;

## 将前面的pin➕wskey拼起来

例如:

**pt\_pin=122272973-6464846;wskey=AAJiltn9AEC6r3vDa5q6k1zlGa49QSEpd3g64i1TEsoj06MyVQSOss1xkvvebSx9lv9H5sFc9LIND6w\_vLbvldr17s-R806q;**

#### 这样复制给🐱🐱🐱机器人即可

![](../images/5F560978-4BA1-4FF4-8A57-E86EF5DF0859_QeRK9NEkqx.jpeg)

#### 提示如上图所示，则为成功

# 其他抓包软件同理！！
