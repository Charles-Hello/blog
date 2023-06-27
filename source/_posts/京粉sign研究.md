



str1没有byte之前
-------------------
b3d087800fbda114&jf_app&{"clientPageId":"jingfen_app","funName":"share","param":{"shareReq":[{"command":1,"notAllowAddToShareManagement":1,"plainUrl":"https://item.m.jd.com/product/100059194543.html?utm_user=plusmember&gx=RnEykW9ZazLcmNRP--tzCLOIdgHUJtY4teq1&ad_od=share&utm_source=androidapp&utm_medium=appshare&utm_campaign=t_335139774&utm_term=CopyURL","platform":1,"shareType":1,"skuId":100059194543,"spuId":0}]}}&20220474&android&3.12.42&Xiaomi&22041211AC&unionShare&13&XiaoMi&2280*1080&1687848528327&00000000-0000-0000-ffff-ffffd76d294b

str1是个根据plainUrl变化的值。


str2是个固定的值 53b0dc1fea2b46ef9651e324ddb1f5b2


functionId=unionShare返回值的返回结果

https://api.m.jd.com/api?functionId=unionShare&body={"clientPageId":"jingfen_app","funName":"share","param":{"shareReq":[{"command":1,"notAllowAddToShareManagement":1,"plainUrl":"https://item.m.jd.com/product/100014134468.html?&utm_source=iosapp&utm_medium=appshare&utm_campaign=t_335139774&utm_term=CopyURL&ad_od=share&utm_user=plusmember&gx=RnAowWFbbDfeyJEVsox3W_9mFJnWh5E&gxd=RnAokGJbYTTczcoU-dd0WcnpPCgpyeZBB3uNDDQ3NwFNe7UhyAxjDKGcA12IzWM","platform":1,"shareType":1,"skuId":100014134468,"spuId":0}]}}&appid=jf_app&t=1687849057584&clientVersion=3.12.42&build=20220474&client=android&d_brand=Xiaomi&d_model=22041211AC&osVersion=13&screen=2280*1080&partner=XiaoMi&androidId=b3d087800fbda114&uuid=00000000-0000-0000-ffff-ffffd76d294b&sign=e3bb31f69558d68d9694f66d8c334819d682dcf1a186aa34de3b0b91004ca144

一般我们都是通过unionShare这个函数拿到返回返利口令的，所以我们分析正确的

现在我们分析一下主要的流程是我们拿到https://item.m.jd.com/product/100059194543.html?utm_user=plusmember&gx=RnEykW9ZazLcmNRP--tzCLOIdgHUJtY4teq1&ad_od=share&utm_source=androidapp&utm_medium=appshare&utm_campaign=t_335139774&utm_term=CopyURL链接，然后通过unionShare这个函数拿到sign。






![](../images/Pasted%20image%2020230627150729.png)

此时此刻sign有了，还差个body的加密

我们就可以实现魔法了。加油！！


回顾上文：从拿到sign的那里body还没有进行加密的，现在我们是找到加密的后的方法给找出来，才能得知body到底是如何加密的才能进行请求
