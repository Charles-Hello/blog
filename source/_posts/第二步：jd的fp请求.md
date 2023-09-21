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
s = e.devcInfo, "{"account":"15952982822","ccode":"86","capfp":{},"cvs":"a04d95f1d97489b23cce20bebd6d6d6b","wgl":"0ef36cfe7a17521389b08af14c0554d0","pr":"1.5","cd":"24","fv":"","fts":"Arial,Calibri,Cambria,Consolas,Courier,CourierNew,Georgia,Helvetica,Impact,LucidaConsole,LucidaSansUnicode,MSGothic,MSPGothic,PalatinoLinotype,SegoePrint,SegoeScript,SegoeUI,Tahoma,Times,TimesNewRoman,TrebuchetMS,Verdana,Wingdings,Symbol,Candara,Constantia,Corbel,Ebrima,FangSong,Gabriola,MicrosoftYaHei,MicrosoftYiBaiti,MingLiUExtB,PMingLiUExtB,SimHei,SimSun,SimSunExtB","scr":"1707x960,1707x912","cpu":"8","pt":"Win32","tzo":"Asia/Shanghai","lan":"zh-CN","wvr":"Google Inc. (NVIDIA)~ANGLE (NVIDIA, NVIDIA GeForce RTX 2060 Direct3D11 vs_5_0 ps_5_0, D3D11)","wdr":false,"mem":8,"sdv":"2.0","lns":"zh-CN,en,en-GB,en-US","tsp":"0"}"
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