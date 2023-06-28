



str1没有byte之前
-------------------
b3d087800fbda114&jf_app&{"clientPageId":"jingfen_app","funName":"share","param":{"shareReq":[{"command":1,"notAllowAddToShareManagement":1,"plainUrl":"https://item.m.jd.com/product/100059194543.html?utm_user=plusmember&gx=RnEykW9ZazLcmNRP--tzCLOIdgHUJtY4teq1&ad_od=share&utm_source=androidapp&utm_medium=appshare&utm_campaign=t_335139774&utm_term=CopyURL","platform":1,"shareType":1,"skuId":100059194543,"spuId":0}]}}&20220474&android&3.12.42&Xiaomi&22041211AC&unionShare&13&XiaoMi&2280*1080&1687848528327&00000000-0000-0000-ffff-ffffd76d294b

str1是个根据plainUrl变化的值。


str2是个固定的值 53b0dc1fea2b46ef9651e324ddb1f5b2


functionId=unionShare返回值的返回结果

https://api.m.jd.com/api?functionId=unionShare&body={"clientPageId":"jingfen_app","funName":"share","param":{"shareReq":[{"command":1,"notAllowAddToShareManagement":1,"plainUrl":"https://item.m.jd.com/product/100014134468.html?&utm_source=iosapp&utm_medium=appshare&utm_campaign=t_335139774&utm_term=CopyURL&ad_od=share&utm_user=plusmember&gx=RnAowWFbbDfeyJEVsox3W_9mFJnWh5E&gxd=RnAokGJbYTTczcoU-dd0WcnpPCgpyeZBB3uNDDQ3NwFNe7UhyAxjDKGcA12IzWM","platform":1,"shareType":1,"skuId":100014134468,"spuId":0}]}}&appid=jf_app&t=1687849057584&clientVersion=3.12.42&build=20220474&client=android&d_brand=Xiaomi&d_model=22041211AC&osVersion=13&screen=2280*1080&partner=XiaoMi&androidId=b3d087800fbda114&uuid=00000000-0000-0000-ffff-ffffd76d294b&sign=e3bb31f69558d68d9694f66d8c334819d682dcf1a186aa34de3b0b91004ca144

一般我们都是通过unionShare这个函数拿到返回返利口令的，所以我们分析正确的

现在我们分析一下主要的流程是我们拿到https://item.m.jd.com/product/100059194543.html?utm_user=plusmember&gx=RnEykW9ZazLcmNRP--tzCLOIdgHUJtY4teq1&ad_od=share&utm_source=androidapp&utm_medium=appshare&utm_campaign=t_335139774&utm_term=CopyURL链接，然后通过unionShare这个函数拿到sign。



sign解密一致

![](../images/Pasted%20image%2020230628162950.png)![](../images/Pasted%20image%2020230628163013.png)


![](../images/Pasted%20image%2020230627150729.png)


此时此刻sign有了，还差个body的加密

我们就可以实现魔法了。加油！！


回顾上文：从拿到sign的那里body还没有进行加密的，现在我们是找到加密的后的方法给找出来，才能得知body到底是如何加密的才能进行请求



httpUrl=https://api.m.jd.com/api?functionId=unionShare&body=%7B%22clientPageId%22%3A%22jingfen_app%22%2C%22funName%22%3A%22share%22%2C%22param%22%3A%7B%22shareReq%22%3A%5B%7B%22command%22%3A1%2C%22notAllowAddToShareManagement%22%3A1%2C%22plainUrl%22%3A%22https%3A%2F%2Fitem.m.jd.com%2Fproduct%2F100020596287.html%3Futm_user%3Dplusmember%26gx%3DRnEykW9ZazLcmNRP--tzCLOIdgHUJtY4teq1%26ad_od%3Dshare%26utm_source%3Dandroidapp%26utm_medium%3Dappshare%26utm_campaign%3Dt_335139774%26utm_term%3DCopyURL%22%2C%22platform%22%3A1%2C%22shareType%22%3A1%2C%22skuId%22%3A100020596287%2C%22spuId%22%3A0%7D%5D%7D%7D&appid=jf_app&t=1687857068856&clientVersion=3.12.42&build=20220474&client=android&d_brand=Xiaomi&d_model=22041211AC&osVersion=13&screen=2280*1080&partner=XiaoMi&androidId=b3d087800fbda114&uuid=00000000-0000-0000-ffff-ffffd76d294b&sign=953c1881023bbf905ce30f43509408df19ba1f47705aa56882b022f10061bf4a

![](../images/Pasted%20image%2020230627172257.png)
HttpUrl.queryParameter[str] result={"clientPageId":"jingfen_app","funName":"share","param":{"shareReq":[{"command":1,"notAllowAddToShareManagement":1,"plainUrl":"https://item.m.jd.com/product/100020596287.html?utm_user=plusmember&gx=RnEykW9ZazLcmNRP--tzCLOIdgHUJtY4teq1&ad_od=share&utm_source=androidapp&utm_medium=appshare&utm_campaign=t_335139774&utm_term=CopyURL","platform":1,"shareType":1,"skuId":100020596287,"spuId":0}]}}
str=appid
HttpUrl.queryParameter[str] result=jf_app
str=clientVersion
HttpUrl.queryParameter[str] result=3.12.42
str=build
HttpUrl.queryParameter[str] result=20220474
str=client
HttpUrl.queryParameter[str] result=android
str=d_brand
HttpUrl.queryParameter[str] result=Xiaomi
str=d_model
HttpUrl.queryParameter[str] result=22041211AC
str=osVersion
HttpUrl.queryParameter[str] result=13
str=screen
HttpUrl.queryParameter[str] result=2280*1080
str=partner
HttpUrl.queryParameter[str] result=XiaoMi
str=androidId
HttpUrl.queryParameter[str] result=b3d087800fbda114
str=uuid
HttpUrl.queryParameter[str] result=00000000-0000-0000-ffff-ffffd76d294b

![](../images/Pasted%20image%2020230627172431.png)

组装hashMap
HashMap hashMap = new HashMap();
                for (String str : queryParameterNames) {
                            hashMap.put(str, httpUrl.queryParameter(str));
}

长这个样子
{
   "clientPageId": "jingfen_app",
   "funName": "share",
   "param": "{\"shareReq\":[{\"command\":1,\"notAllowAddToShareManagement\":1,\"plainUrl\":\"https://item.m.jd.com/product/100014134468.html?&utm_source=iosapp&utm_medium=appshare&utm_campaign=t_335139774&utm_term=CopyURL&ad_od=share&utm_user=plusmember&gx=RnAowWFbbDfeyJEVsox3W_9mFJnWh5E&gxd=RnAokGJbYTTczcoU-dd0WcnpPCgpyeZBB3uNDDQ3NwFNe7UhyAxjDKGcA12IzWM\",\"platform\":1,\"shareType\":1,\"skuId\":100014134468,\"spuId\":0}]}",
   "appid": "jf_app",
   "t": "1687849057584",
   "clientVersion": "3.12.42",
   "build": "20220474",
   "client": "android",
   "d_brand": "Xiaomi",
   "d_model": "22041211AC",
   "osVersion": "13",
   "screen": "2280*1080",
   "partner": "XiaoMi",
   "androidId": "b3d087800fbda114",
   "uuid": "00000000-0000-0000-ffff-ffffd76d294b"
}


![](../images/Pasted%20image%2020230627172636.png)

拿到body



JSONObject jSONObject = new JSONObject();
    com.jd.phc.utils.b.b(d, "brian cipher type is :" + pHCCipherSuite.value());
    for (String str2 : map.keySet()) {
    String str3 = map.get(str2);
    String a2 = f.a(str3.getBytes());
    com.jd.phc.utils.b.b(d, "brian Encoded str of " + str3 + " is :" + a2);
    jSONObject.put(str2, a2);
    }




