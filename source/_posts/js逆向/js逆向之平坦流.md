---
title: js逆向之平坦流
tags: []
index_img: ../banner_images/banne_photo62.png
categories:
  - js逆向
date: 2023-07-07 21:24:01
---

![](../images/../../images/Pasted%20image%2020230707212436.png)
<font color="#9bbb59">何为平坦流呢？</font>
就是通过一些列的for和while循环来对不同的情况进行判断，然后通过赋值状态的改变来动态调整判断的先后顺讯来扰乱逆向者的思维操作。


<font color="#9bbb59">判断平坦流</font>


```
return function(){
  xxx.apply(this,arguments)
}()
```
看到这个标识找上面js语句，<font color="#ff0000">必定是个平坦流</font>