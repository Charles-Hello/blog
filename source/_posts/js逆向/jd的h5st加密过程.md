---
tags: []
index_img: ../banner_images/banne_photo96.png
categories:
  - js逆向
date: 2023-07-16 09:12:38
title:
---

p(s)为body加密
sign(r)为h5st加密
![](../Pasted%20image%2020230716091309.png)


操作前提：追异步得慢慢追，按f11逐步跳过，遇到连续循环的话就按shift+f11跳出当前函数。


![](../Pasted%20image%2020230716091717.png)

遇到大量的平坦流就就在每个ruturn打下断点。里面很多重复混淆的操作，不要管，先运行，看结果是否是我们所需要的，然后在断定哪个参数是我需要找出来的，然后一步步解出来。


这里我们记录一下8这个点的操作流程，还是老规则，每个关键的case都打上断点，记录一下执行的结果和顺序，了解整个加密的过程是如何实现的，这里要用恢复脚本执行来迅速判断。

![](../Pasted%20image%2020230716092117.png)

1. 跳7，获取13位时间戳![](../Pasted%20image%2020230716092314.png)
2. 跳6的S的赋值，略过
3. 跳3的W的赋值![](../Pasted%20image%2020230716092448.png)
4. 跳1应该是用“，”分割字符串![](../Pasted%20image%2020230716092750.png)
5. 跳2是h5st的执行结果![](../Pasted%20image%2020230716092916.png)可以看到有w，A，s，r四个参数，w是上述的3的W赋值，A为7的时间戳，S为时间具体数![](../Pasted%20image%2020230716093138.png)r为body的值![](../Pasted%20image%2020230716093234.png)
到这里我们分析到了整个h5st


[""[s(1300, 0, 0, 1418)](r), ""[a(0, 0, 1112, 1200)](this[a(0, 0, 1235, 1089) + "nt"]), ""[a(0, 0, 1112, 1207)](this[s(1438, 0, 0, 1465)]), ""[a(0, 0, 1112, 999)](this[s(1239, 0, 0, 1109)] ? this._token : this[a(0, 0, 1011, 970) + s(1394, 0, 0, 1444)]), ""[s(1300, 0, 0, 1255)](e), "".concat(this[a(0, 0, 1247, 1196)]), ""[s(1300, 0, 0, 1382)](t), "".concat(n)][a(0, 0, 1236, 1342)](";")
"20230716092019005;mm5z9t6nig5353w5;95cb3;tk03wb56e1c7f18n1hIoD5JrXiyAXLCU3I70x-wqdJOi6zzxAvvtKpuByuSJpe0gBvjSJi8LqOD2z1ZOTqwHoh2F3BjG;29a9f183bd9b1d11c4d03a7bf4e1f465;4.1;1689470419005;ee3cf7f6b94dc20e9265d83066bb9cee06c9d012b4d563d6da825f399a1bb7301c0d5ff3240351c7bdff196e5c0df0152761dc3179f8a3012b41eba050ac89622a963c4994748609e839d26c8abba1d18171b069a129b7f74236f719246d60e8ae5b0242ecda636d657b3b585dcf2ccefeaa79c07467945c28e49f4806b25ec597eeb6f059eaa71b47ec1c7b6d37df347fd657a62af8c56bc99cfc72a26bee1cbbd4ca69ad97cc9d41b419695a6983f53a686eb9cccdfe9bf873130d404b89163fe0d8d436f97efbd1e1e43835cbc6cf"


"<font color="#c0504d">20230716092019005</font>;<font color="#9bbb59">mm5z9t6nig5353w5</font>;<font color="#f79646">95cb3</font>;<font color="#e36c09">tk03wb56e1c7f18n1hIoD5JrXiyAXLCU3I70x-wqdJOi6zzxAvvtKpuByuSJpe0gBvjSJi8LqOD2z1ZOTqwHoh2F3BjG;29a9f183bd9b1d11c4d03a7bf4e1f465</font>;<font color="#548dd4">4.1</font>;<font color="#953734">1689470419005</font>;<font color="#ffff00">ee3cf7f6b94dc20e9265d83066bb9cee06c9d012b4d563d6da825f399a1bb7301c0d5ff3240351c7bdff196e5c0df0152761dc3179f8a3012b41eba050ac89622a963c4994748609e839d26c8abba1d18171b069a129b7f74236f719246d60e8ae5b0242ecda636d657b3b585dcf2ccefeaa79c07467945c28e49f4806b25ec597eeb6f059eaa71b47ec1c7b6d37df347fd657a62af8c56bc99cfc72a26bee1cbbd4ca69ad97cc9d41b419695a6983f53a686eb9cccdfe9bf873130d404b89163fe0d8d436f97efbd1e1e43835cbc6cf</font>"

由7个部分组成，我们还得一一研究
1. mm5z9t6nig5353w5
2. 95cb3
3. tk03wb56e1c7f18n1hIoD5JrXiyAXLCU3I70x-wqdJOi6zzxAvvtKpuByuSJpe0gBvjSJi8LqOD2z1ZOTqwHoh2F3BjG;29a9f183bd9b1d11c4d03a7bf4e1f465
这三个值的由来

