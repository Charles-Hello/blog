---
title: rsa加密
tags: []
index_img: ../banner_images/banne_photo92.png
categories:
  - js逆向
date: 2023-07-08 20:27:39
---

通常由这三部曲构成
```
new res  =  10001
setkey 
执行加密 encrypt
```

点击查看加密函数必有Bigint这个东东

可以快速搜索10001这个关键词直接定位rsa


常见先把代码全部复制过来，然后折叠，然后去搜索对应的代码，分析哪一段需要扣，哪一段不需要扣

function(){
}()这个是自执行方法


