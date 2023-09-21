---
title: 第二步：jd的fp请求
date: 2023-09-21 21:09:01
tags: []
index_img: ../banner_images/banne_photo83.png
---

```javascript


function q(t, e) {
	for (var n = t.toString().length; n < e; )
		t = "0" + t,
		n++;
	return t
}

function k(t) {
	for (var e = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"], n = "", r = 0; r < t; r++) {
		n += e[Math.floor(35 * Math.random())]
	}
	return n
}

{
h = d.dispatch,
g = d.commit,
v = p.fp_req,
m = p.platformType,
y = p.setFp,
b = p.captchaType,
_ = p.langMap,
t.prev = 2,
t.next = 5,
e = p,
l = void 0,
n = Date.parse(new Date + ""),  //1695302616000
r = n % 19,   //10
o = e.sessionId,  //jasp请求的响应
i = e.host,   "//jcap.m.jd.com"
a = e.tdat_code, 99992
s = e.devcInfo, "{"account":"15952982822","ccode":"86","capfp":{},"cvs":"a04d95f1d97489b23cce20bebd6d6d6b","wgl":"0ef36cfe7a17521389b08af14c0554d0","pr":"1.5","cd":"24","fv":"","fts":"Arial,Calibri,Cambria,Consolas,Courier,CourierNew,Georgia,Helvetica,Impact,LucidaConsole,LucidaSansUnicode,MSGothic,MSPGothic,PalatinoLinotype,SegoePrint,SegoeScript,SegoeUI,Tahoma,Times,TimesNewRoman,TrebuchetMS,Verdana,Wingdings,Symbol,Candara,Constantia,Corbel,Ebrima,FangSong,Gabriola,MicrosoftYaHei,MicrosoftYiBaiti,MingLiUExtB,PMingLiUExtB,SimHei,SimSun,SimSunExtB","scr":"1707x960,1707x912","cpu":"8","pt":"Win32","tzo":"Asia/Shanghai","lan":"zh-CN","wvr":"Google Inc. (NVIDIA)~ANGLE (NVIDIA, NVIDIA GeForce RTX 2060 Direct3D11 vs_5_0 ps_5_0, D3D11)","wdr":false,"mem":8,"sdv":"2.0","lns":"zh-CN,en,en-GB,en-US","tsp":"0"}"  //account和capfp有时候为空
c = e.language, 1
u = e.urlMap, {
    "report": "https://jcapmonitor.m.jd.com/web_jcap_report",
    "img": "https://h5.360buyimg.com/jcap/pc/img/",
    "iframe": "https://h5.360buyimg.com/jcap/html/captchaStorage.html",
    "js": "https://h5.360buyimg.com/jcap/js/",
    "fp": "/cgi-bin/api/fp",
    "refresh": "/cgi-bin/api/refresh",
    "check": "/cgi-bin/api/check",
    "v": 20180110
} 
f = e.tdat_ctx,  "23130303037303236454145424647333930364347354831453137323142373636383333363233303033333234454636454541433246344546333730344346493333373831483530334233303035313030303"  （固定）
(l = {
	si: o,
	ct: "",
	version: 2,
	lang: c,
	client: e.platformOS "m"
}).ct = H(K(r) + q(l.si.length, 4) + l.si + s + n, a, f),
T.a.interfaceId = 268435458,
T.a.interfaceName = "fp",

```



#### 生成st参数给第三步



请求参数

```
1. si:
    
    WO-_xgABAAAE90GXWUkAMI2cq6P4aWCX6wN6BTUJghrMEBjEf5AfE3ZgyfDPWTDXKUcZ2cZFmef5zGiz5wq9YAAAAAA
    
2. ct:
    
    {"data":"g76DHnIgKP_LFvPDWo4yuXC_gOhuhQ7Sz0Ctmm-UpSwXU2uZPwHtiyTp7CyRPB9QYn2f9R64bo8E\n5TWlPry-KH3CDxamopGRSBu39N8IucckzCROMLzKrJPoIoEkaqZGS3DSZCKqHxaJlpM5XZmykYnb\naZ9aRw_mDsx-ej5T8LR4RI8qcK7s9HGcc_FCnJg5RpGgqSl15w0Fm96CC0E3doFBBQPQwTddR9MA\nNyMC3bScVyMS0_XekIDPj6BagTeWKeuFArOfNiIxTMnPXPTCbZMmIaD58akLVfB4T-zaeJioihd5\nTZjaaXTC0zcV32iexNAqFAZ9z0znyh1yrivqXdALzdjl7Qpzngcs2r9nggtxqlWezvyubMC0mwxD\nolRJF2GKDzvyKkfYLhv1694cuzC8JaYGg37DJnMjZ5sn-i6BpI6Rb7IlRF-5QxjItkdTnM4Q0JYs\nQ3wUV3Y5A-xfuldUFNAcoyNuXyIg0r6fl1UdBS_KmbVQ_PvdKlcbHLb77d4beJ4TeNiisvsZh8Fm\nT-UwZfFpETxhhdH4_oTbgblfmfH4gEjXxDIAF10CZvv5DtZb1JrgUTM_kDR51tgHzyRSJnPU4Iut\nbdjftWTBwh4CfD5NmNACpSPSscUk71lPiTDWHiIKofJ_JY2Em8RCRBi23ECy1pndQkgSL2Nj2jKY\nSkbywAor1KafsoIydvs0uAOYC3VQ9n-aaZMPLYacx3sY3t9ggXutg_S3HHNj6Ye0kUcn--p0Zg8x\nD3NtlrYITf-DLlaxMQAzYKDXnwayPy3h3I6huF6zz65xkDQ_7xMP4bGlrPMbWjveE8ll4fuxKFMo\nj4iCtHURELr95j6I4_4VTYTZKIGdYfbKsdAPFyGNj06UCUXTnu18I3jCR3kwzF4Gm-TQjI_ner_q\nuRjuqH1cxuuUdjp0Vjwuv3XE0rzTMH94zuiPannhtOEKapPBbJA3-TNx6-R68suP3mg6EKhypcd5\nGmjKv6hp6WD_TxKVA4OuQJcYTthVRv2q9jv_nLmMs0o2tyDHU0yf7dJMf6Z_RBFaBZs67XdFm4dQ\nyyhlYrcgYwvbeC2QCQyuNfhgpxjWc2OO1nAl_1TLPa-gHSYJMQ5nAdDs6HulwGHg_HcCZaSUePUl\nbF18mAvXxXbU7AIcxEMGixzYL4AVbWruck8u75WXhQsGmi7fm_D0M9Yz5xd4cCZDkutEGvRXU6un\ntRrjWp6oaQGVkTtftlLz5A==","version":2}
    
3. version:
    
    2
    
4. lang:
    
    1
    
5. client:
    
    m

```

响应 
```


{"st":"AxuG0iKCCEIEgaaY","code":0,"msg":"","fp":"n8wUAxWalvZwEAiWGNO7mIqE1y3cK7ybfAYaJWxyzCjxHDJ2KTuyZmGByqbjOUsCnGO6kDxD7khND3F0W4Rktw==","tp":9,"img":""}

```