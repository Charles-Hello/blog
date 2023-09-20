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
r = n.sessionId ="fIS8JQABAAAIPtAi5FkAMHu---j78gy-GB0Hi1vlU50IYL3V0VefS5LFuK1KAf1wE0S8hgdj3af0wjXtsEplgAAAAAA"(会变)
o = n.language =1
i = n.tdat_code =99992
a = n.host ="//jcap.m.jd.com"
s = n.st ="taJvP8ua60xCxdby" (会变)
c = n.devcInfo ="{"account":"15015344889","ccode":"86","capfp":"xpo7vzpVL5aRVVkbpmzqh117VZR_o7SNJgiJE24rprnSGM5XwlDKoQCe9EvBac2ym_S13lLjJgRpiIQitr6HRw==","cvs":"a04d95f1d97489b23cce20bebd6d6d6b","wgl":"0ef36cfe7a17521389b08af14c0554d0","pr":"1.5","cd":"24","fv":"","fts":"Arial,Calibri,Cambria,Consolas,Courier,CourierNew,Georgia,Helvetica,Impact,LucidaConsole,LucidaSansUnicode,MSGothic,MSPGothic,PalatinoLinotype,SegoePrint,SegoeScript,SegoeUI,Tahoma,Times,TimesNewRoman,TrebuchetMS,Verdana,Wingdings,Symbol,Candara,Constantia,Corbel,Ebrima,FangSong,Gabriola,MicrosoftYaHei,MicrosoftYiBaiti,MingLiUExtB,PMingLiUExtB,SimHei,SimSun,SimSunExtB","scr":"1707x960,1707x912","cpu":"8","pt":"Win32","tzo":"Asia/Shanghai","lan":"zh-CN","wvr":"Google Inc. (NVIDIA)~ANGLE (NVIDIA, NVIDIA GeForce RTX 2060 Direct3D11 vs_5_0 ps_5_0, D3D11)","wdr":false,"mem":8,"sdv":"2.0","lns":"zh-CN,en,en-GB,en-US","tsp":"0"}" (只变account)
u = n.urlMap = {
    "report": "https://jcapmonitor.m.jd.com/web_jcap_report",
    "img": "https://h5.360buyimg.com/jcap/pc/img/",
    "iframe": "https://h5.360buyimg.com/jcap/html/captchaStorage.html",
    "js": "https://h5.360buyimg.com/jcap/js/",
    "fp": "/cgi-bin/api/fp",
    "refresh": "/cgi-bin/api/refresh",
    "check": "/cgi-bin/api/check",
    "v": 20180110
}
f = n.platformOS ="m"
l = n.tdat_ctx ='23130303037303236454145424647333930364347354831453137323142373636383333363233303033333234454636454541433246344546333730344346493333373831483530334233303035313030303'


var t = window.localStorage.getItem(e) || "{}";

1. "[{\"eid\":\"click\",\"did\":\"\",\"cn\":\"\",\"sx\":216,\"sy\":660,\"px\":212,\"py\":556,\"time\":1695210205669},{\"eid\":\"click\",\"did\":\"\",\"cn\":\"getMsg-btn text-btn J_ping timer\",\"sx\":532,\"sy\":270,\"px\":528,\"py\":166,\"time\":1695210401014},{\"eid\":\"click\",\"did\":\"\",\"cn\":\"acc-input mobile J_ping\",\"sx\":311,\"sy\":193,\"px\":307,\"py\":89,\"time\":1695210408168},{\"eid\":\"click\",\"did\":\"\",\"cn\":\"policy_tip-checkbox\",\"sx\":39,\"sy\":600,\"px\":35,\"py\":496,\"time\":1695210412964},{\"eid\":\"click\",\"did\":\"\",\"cn\":\"getMsg-btn text-btn J_ping timer\",\"sx\":514,\"sy\":253,\"px\":510,\"py\":149,\"time\":1695210414950},{\"eid\":\"click\",\"did\":\"\",\"cn\":\"\",\"sx\":223,\"sy\":661,\"px\":219,\"py\":557,\"time\":1695210421522},{\"eid\":\"click\",\"did\":\"\",\"cn\":\"captcha_drop\",\"sx\":369,\"sy\":121,\"px\":365,\"py\":17,\"time\":1695210792485},{\"eid\":\"click\",\"did\":\"\",\"cn\":\"getMsg-btn text-btn J_ping timer\",\"sx\":539,\"sy\":259,\"px\":535,\"py\":155,\"time\":1695210793652},{\"eid\":\"click\",\"did\":\"\",\"cn\":\"captcha_drop\",\"sx\":373,\"sy\":123,\"px\":369,\"py\":19,\"time\":1695210802219},{\"eid\":\"click\",\"did\":\"\",\"cn\":\"getMsg-btn text-btn J_ping timer\",\"sx\":554,\"sy\":267,\"px\":550,\"py\":163,\"time\":1695210803422}]"


return JSON.parse(t)
h = {
    touchList: Object(T.d)("touche_message")
}=[
    {
        "eid": "click",
        "did": "",
        "cn": "acc-input mobile J_ping",
        "sx": 289,
        "sy": 196,
        "px": 285,
        "py": 92,
        "time": 1695201591043
    },
    {
        "eid": "click",
        "did": "",
        "cn": "policy_tip-checkbox",
        "sx": 53,
        "sy": 596,
        "px": 49,
        "py": 492,
        "time": 1695201595164
    },
    {
        "eid": "click",
        "did": "",
        "cn": "getMsg-btn text-btn J_ping timer",
        "sx": 586,
        "sy": 256,
        "px": 582,
        "py": 152,
        "time": 1695201598058
    },
    {
        "eid": "click",
        "did": "",
        "cn": "",
        "sx": 304,
        "sy": 659,
        "px": 300,
        "py": 555,
        "time": 1695201613573
    },
    {
        "eid": "click",
        "did": "",
        "cn": "acc-input mobile J_ping",
        "sx": 284,
        "sy": 190,
        "px": 280,
        "py": 86,
        "time": 1695208898504
    },
    {
        "eid": "click",
        "did": "",
        "cn": "policy_tip-checkbox",
        "sx": 32,
        "sy": 596,
        "px": 28,
        "py": 492,
        "time": 1695208903034
    },
    {
        "eid": "click",
        "did": "",
        "cn": "page",
        "sx": 364,
        "sy": 130,
        "px": 360,
        "py": 26,
        "time": 1695208910828
    },
    {
        "eid": "click",
        "did": "",
        "cn": "getMsg-btn text-btn J_ping timer",
        "sx": 562,
        "sy": 254,
        "px": 558,
        "py": 150,
        "time": 1695208910856
    }
]（随机）

d = 1695208930000 （时间戳）
p = d % 41 


tk = H(d + q(r.length, 4) + r + q(s.length, 4) + s + q(t.length, 6) + t + JSON.stringify(h) + K(p), i, l)



function H(t, e, n) {
                var r = t
                  , o = i;
                e && (a = e);
                try {
                    return n ? JSON.stringify(window.f.getEncryptData(r, n)) : s(r, o)
                } catch (t) {
                    return s(r, o)
                }
}


这里的H的参数t= "16952089300000091fIS8JQABAAAIPtAi5FkAMHu---j78gy-GB0Hi1vlU50IYL3V0VefS5LFuK1KAf1wE0S8hgdj3af0wjXtsEplgAAAAAA0016taJvP8ua60xCxdby000000{"touchList":[{"eid":"click","did":"","cn":"acc-input mobile J_ping","sx":289,"sy":196,"px":285,"py":92,"time":1695201591043},{"eid":"click","did":"","cn":"policy_tip-checkbox","sx":53,"sy":596,"px":49,"py":492,"time":1695201595164},{"eid":"click","did":"","cn":"getMsg-btn text-btn J_ping timer","sx":586,"sy":256,"px":582,"py":152,"time":1695201598058},{"eid":"click","did":"","cn":"","sx":304,"sy":659,"px":300,"py":555,"time":1695201613573},{"eid":"click","did":"","cn":"acc-input mobile J_ping","sx":284,"sy":190,"px":280,"py":86,"time":1695208898504},{"eid":"click","did":"","cn":"policy_tip-checkbox","sx":32,"sy":596,"px":28,"py":492,"time":1695208903034},{"eid":"click","did":"","cn":"page","sx":364,"sy":130,"px":360,"py":26,"time":1695208910828},{"eid":"click","did":"","cn":"getMsg-btn text-btn J_ping timer","sx":562,"sy":254,"px":558,"py":150,"time":1695208910856}]}foapmqy5ck2e"

e = 99992

n ="23130303037303236454145424647333930364347354831453137323142373636383333363233303033333234454636454541433246344546333730344346493333373831483530334233303035313030303"

```
