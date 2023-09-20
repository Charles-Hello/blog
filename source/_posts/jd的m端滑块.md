---
title: jd的m端滑块
date: 2023-09-20 17:23:59
tags: []
index_img: ../banner_images/banne_photo86.png
---
先拿到原来的图片，然后对图片的正确大小，用网页进行缩放使其达到正常的图片大小，然后根据断点滑块的值来判断最后滑动的距离。
![](Pasted%20image%2020230920172406.png)



```
function q(t, e) {
                for (var n = t.toString().length; n < e; )
                    t = "0" + t,
                    n++;
                return t
}
r = n.sessionId
o = n.language
i = n.tdat_code
a = n.host
s = n.st 
c = n.devcInfo
u = n.urlMap
f = n.platformOS
l = n.tdat_ctx;
r = n.sessionId ="fIS8JQABAAAIPtAi5FkAMHu---j78gy-GB0Hi1vlU50IYL3V0VefS5LFuK1KAf1wE0S8hgdj3af0wjXtsEplgAAAAAA"
s = 
d = 1695208930000
tk = H(d + q(r.length, 4) + r + q(s.length, 4) + s + q(t.length, 6) + t + JSON.stringify(h) + K(p), i, l)


tk  = d + 

```
