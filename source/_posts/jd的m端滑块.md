---
title: jd的m端滑块
date: 2023-09-20 17:23:59
tags: []
index_img: ../banner_images/banne_photo86.png
---
先拿到原来的图片，然后对图片的正确大小，用网页进行缩放使其达到正常的图片大小，然后根据断点滑块的值来判断最后滑动的距离。
![](../images/Pasted%20image%2020230920172406.png)



`````` javascript
function q(t, e) {
                for (var n = t.toString().length; n < e; )
                    t = "0" + t,
                    n++;
                return t
}




r = n.sessionId ="fIS8JQABAAAIPtAi5FkAMHu---j78gy-GB0Hi1vlU50IYL3V0VefS5LFuK1KAf1wE0S8hgdj3af0wjXtsEplgAAAAAA"(由  
https://plogin.m.jd.com/cgi-bin/mm/jcapsid的post的得到)
o = n.language =1 （固定）
i = n.tdat_code =99992 （固定）
a = n.host ="//jcap.m.jd.com" （固定）
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
}（固定）
f = n.platformOS ="m" （固定）
l = n.tdat_ctx ='23130303037303236454145424647333930364347354831453137323142373636383333363233303033333234454636454541433246344546333730344346493333373831483530334233303035313030303' （固定）

这里的e是 touche_message
var t = window.localStorage.getItem(e) || "{}";


return JSON.parse(t)
h = {
    touchList: Object(T.d)("touche_message")
}=[
    {
        "eid": "click",
        "did": "",
        "cn": "acc-input mobile J_ping",
        "sx": 146,
        "sy": 186,
        "px": 142,
        "py": 82,
        "time": 1695258916201 （最早）
    },
    {
        "eid": "click",
        "did": "",
        "cn": "policy_tip-checkbox",
        "sx": 37,
        "sy": 596,
        "px": 33,
        "py": 492,
        "time": 1695258922162
    },
    {
        "eid": "click",
        "did": "",
        "cn": "getMsg-btn text-btn J_ping timer",
        "sx": 546,
        "sy": 267,
        "px": 542,
        "py": 163,
        "time": 1695258923367
    },
    {
        "eid": "click",
        "did": "",
        "cn": "",
        "sx": 322,
        "sy": 665,
        "px": 318,
        "py": 561,
        "time": 1695258933085
    },
    {
        "eid": "click",
        "did": "",
        "cn": "",
        "sx": 271,
        "sy": 662,
        "px": 267,
        "py": 558,
        "time": 1695259055128
    },
    {
        "eid": "click",
        "did": "",
        "cn": "acc-input mobile J_ping",
        "sx": 254,
        "sy": 188,
        "px": 250,
        "py": 84,
        "time": 1695260364384
    },
    {
        "eid": "click",
        "did": "",
        "cn": "acc-input mobile J_ping",
        "sx": 171,
        "sy": 187,
        "px": 167,
        "py": 83,
        "time": 1695260369505
    },
    {
        "eid": "click",
        "did": "",
        "cn": "policy_tip-checkbox",
        "sx": 36,
        "sy": 600,
        "px": 32,
        "py": 496,
        "time": 1695260371452
    },
    {
        "eid": "click",
        "did": "",
        "cn": "getMsg-btn text-btn J_ping timer",
        "sx": 538,
        "sy": 262,
        "px": 534,
        "py": 158,
        "time": 1695260372637
    },
    {
        "eid": "click",
        "did": "",
        "cn": "",
        "sx": 190,
        "sy": 661,
        "px": 186,
        "py": 557,
        "time": 1695260446609 （最后）
    }
]（10个，sx,sy,px,py 上下正负10，time为滑块花费的时间然后取10次）

d = 1695208930000 （时间戳最后的时间加几秒）
p = d % 41 




function K(t) {
                for (var e = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"], n = "", r = 0; r < t; r++) {
                    n += e[Math.floor(35 * Math.random())]
                }
return n
}


t = "{"ht":260,"wt":421,"bw":86,"sw":421,"mw":86,"list":[[0,0,0]····················[144,-5,383]]}"（传的list不固定，得从py的fastapi那里获取，其他均固定）

tk = H(d + q(r.length, 4) + r + q(s.length, 4) + s + q(t.length, 6) + t + JSON.stringify(h) + K(p), i, l)



function getEncryptData(arg0, arg1) {
if (arguments.length !== 2) {
throwBindingError('function getEncryptData called with ' + arguments.length + ' arguments, expected 2 args!');
}
var arg0Wired = argType0.toWireType(null, arg0); // std::string
var arg1Wired = argType1.toWireType(null, arg1); // std::string
var rv = invoker(fn, arg0Wired, arg1Wired);
arg0Wired_dtor(arg0Wired); // std::string
arg1Wired_dtor(arg1Wired); // std::string
var ret = retType.fromWireType(rv);
return ret;
}

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

n ="23130303037303236454145424647333930364347354831453137323142373636383333363233303033333234454636454541433246344546333730344346493333373831483530334233303035313030303" （固定）

```


``` javascript
鼠标事件



{
	key: "start",
	value: function(t) {
		G.doStartCheck(),
		this.spImg = "https://h5.360buyimg.com/jcap/img_20190409/right-white.png",
		this.moveX = Object(T.e)(t), //160
		this.moveY = Object(T.f)(t), //570
		this.lastTime = Date.now(),
		this.xyList.push([0, 0, 0]),
		t.stopPropagation(),
		t.cancelable && t.preventDefault()
	}
}


{
{key: "move",
value: function(t) {
	var e = Object(T.e)(t) - this.moveX
	  , n = Object(T.f)(t) - this.moveY;
	0 <= e && e < this.$refs.cpc_img.width - this.$refs.move_img.width && (this.spMsg = this.langMap.code_23,
	this.$refs.move_img.style.left = e + "px",
	this.$refs.small_img.style.left = e + "px",
	this.$refs.bg_blue.style.width = e + 20 + "px",
	this.$refs.sp_msg.getBoundingClientRect().left,
	this.$refs.sp_msg.getBoundingClientRect().top,
	this.xyList.push([Number(e.toFixed(2)), Number(n.toFixed(2)), Date.now() - this.lastTime]),
	this.lastTime = Date.now()),
	t.stopPropagation(),
	t.cancelable && t.preventDefault()
}}

这里主要拿到xyList这个表。是由x，y，t
滑满则为一般分为400，也就是400/275 = 1.45每份
也就是 1.45*滑动的距离 = 多少分成多少份
x 的格式为滑动距离
y 可以伪造范围为正负10左右
t 花费时间 一开始为1-4s左右，后来接近抖动的时候赋值30-350ms 这里跳动很大的，有时候30，有时候170，又回归到30,这样的抖动

```