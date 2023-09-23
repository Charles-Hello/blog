---
title: 第三步 jd的m端滑块 check
date: 2023-09-20 17:23:59
tags: []
index_img: ../banner_images/banne_photo86.png
---
先拿到原来的图片，然后对图片的正确大小，用网页进行缩放使其达到正常的图片大小，然后根据断点滑块的值来判断最后滑动的距离。

![](../images/Pasted%20image%2020230920172406.png)


![](../images/Pasted%20image%2020230921204808.png)


``` javascript

function q(t, e) {
                for (var n = t.toString().length; n < e; )
                    t = "0" + t,
                    n++;
                return t
}




r = n.sessionId ="fIS8JQABAAAIPtAi5FkAMHu---j78gy-GB0Hi1vlU50IYL3V0VefS5LFuK1KAf1wE0S8hgdj3af0wjXtsEplgAAAAAA"(由  
https://plogin.m.jd.com/cgi-bin/mm/jcapsid的post的得到) 解决
o = n.language =1 （固定） 解决
i = n.tdat_code =99992 （固定） 解决
a = n.host ="//jcap.m.jd.com" （固定） 解决
s = n.st ="taJvP8ua60xCxdby" (会变)  
c = n.devcInfo ="{"account":"15015344889","ccode":"86","capfp":"xpo7vzpVL5aRVVkbpmzqh117VZR_o7SNJgiJE24rprnSGM5XwlDKoQCe9EvBac2ym_S13lLjJgRpiIQitr6HRw==","cvs":"a04d95f1d97489b23cce20bebd6d6d6b","wgl":"0ef36cfe7a17521389b08af14c0554d0","pr":"1.5","cd":"24","fv":"","fts":"Arial,Calibri,Cambria,Consolas,Courier,CourierNew,Georgia,Helvetica,Impact,LucidaConsole,LucidaSansUnicode,MSGothic,MSPGothic,PalatinoLinotype,SegoePrint,SegoeScript,SegoeUI,Tahoma,Times,TimesNewRoman,TrebuchetMS,Verdana,Wingdings,Symbol,Candara,Constantia,Corbel,Ebrima,FangSong,Gabriola,MicrosoftYaHei,MicrosoftYiBaiti,MingLiUExtB,PMingLiUExtB,SimHei,SimSun,SimSunExtB","scr":"1707x960,1707x912","cpu":"8","pt":"Win32","tzo":"Asia/Shanghai","lan":"zh-CN","wvr":"Google Inc. (NVIDIA)~ANGLE (NVIDIA, NVIDIA GeForce RTX 2060 Direct3D11 vs_5_0 ps_5_0, D3D11)","wdr":false,"mem":8,"sdv":"2.0","lns":"zh-CN,en,en-GB,en-US","tsp":"0"}" (只变account) 解决
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

d = 1695208930000 （时间戳最后的时间加几秒）  解决
p = d % 41  解决




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








g  = "{"account":"15015344889","ccode":"86","capfp":"m14jVxG3CClLHe5yUTpVWEeiwjCIAet-ObrCbyZjmQW9F3dPWaxZgQBcf8eaHlgocYg_PNVSnnKkUhRwXux87w==","cvs":"a04d95f1d97489b23cce20bebd6d6d6b","wgl":"0ef36cfe7a17521389b08af14c0554d0","pr":"1.5","cd":"24","fv":"","fts":"Arial,Calibri,Cambria,Consolas,Courier,CourierNew,Georgia,Helvetica,Impact,LucidaConsole,LucidaSansUnicode,MSGothic,MSPGothic,PalatinoLinotype,SegoePrint,SegoeScript,SegoeUI,Tahoma,Times,TimesNewRoman,TrebuchetMS,Verdana,Wingdings,Symbol,Candara,Constantia,Corbel,Ebrima,FangSong,Gabriola,MicrosoftYaHei,MicrosoftYiBaiti,MingLiUExtB,PMingLiUExtB,SimHei,SimSun,SimSunExtB","scr":"1707x960,1707x912","cpu":"8","pt":"Win32","tzo":"Asia/Shanghai","lan":"zh-CN","wvr":"Google Inc. (NVIDIA)~ANGLE (NVIDIA, NVIDIA GeForce RTX 2060 Direct3D11 vs_5_0 ps_5_0, D3D11)","wdr":false,"mem":8,"sdv":"2.0","lns":"zh-CN,en,en-GB,en-US","tsp":"0"}"

si的值 "Xg0aRAABAAAFmK5kzRwAMKVa_Y9J2O3Ykj5TQDFqCdp-zeR8FRzerqJXwRqY8Wm-In2e_ikG492CF27dIzauDgAAAAA"  由https://jcap.m.jd.com/cgi-bin/api/fp响应中得到  

tk = "{"data":"SrI7IVcFlDJKHcJF9S2uIY-····" 解决



getSensorInfo: function(e, t) {
	try {
		if (t && "string" == typeof t) {
			var n = JSON.parse(e)
			  , r = JSON.parse(t);
			return r && r.sen && (n.sen = r.sen),
			JSON.stringify(n)
		}
		return e
	} catch (t) {
		return e
	}
},



	var r = n.sessionId
	  , o = n.language
	  , i = n.tdat_code
	  , a = n.host
	  , s = n.st 
	  , c = n.devcInfo
	  , u = n.urlMap
	  , f = n.platformOS
	  , l = n.tdat_ctx;
	t = encodeURI(t);
	var d = Date.parse(new Date + "")
	  , p = d % 41
	  , h = {
		touchList: Object(T.d)("touche_message")
	}
	  , g = G.getSensorInfo(c, e)  // e =""
	  , v = {
		si: r, 
		lang: o,
		tk: H(d + q(r.length, 4) + r + q(s.length, 4) + s + q(t.length, 6) + t + JSON.stringify(h) + K(p), i, l),
		ct: H(K(d % 19) + q(r.length, 4) + r + g + d, i, l),
		version: 2,
		client: f



流程 发送第一个check  拿到对应的图片

第二个check 则请求验证

```


分析第一次check


```javascript

t = ""

touchList =[
    {
        "eid": "click",
        "did": "",
        "cn": "acc-input mobile J_ping",
        "sx": 252,
        "sy": 198,
        "px": 248,
        "py": 94,
        "time": 1695304768930
    },
    {
        "eid": "click",
        "did": "",
        "cn": "policy_tip-checkbox",
        "sx": 35,
        "sy": 601,
        "px": 31,
        "py": 497,
        "time": 1695304773658
    },
    {
        "eid": "click",
        "did": "",
        "cn": "getMsg-btn text-btn J_ping timer",
        "sx": 370,
        "sy": 261,
        "px": 366,
        "py": 157,
        "time": 1695304777061
    }
]

g ="{"account":"15695302611","ccode":"86","capfp":{},"cvs":"a04d95f1d97489b23cce20bebd6d6d6b","wgl":"0ef36cfe7a17521389b08af14c0554d0","pr":"1.5","cd":"24","fv":"","fts":"Arial,Calibri,Cambria,Consolas,Courier,CourierNew,Georgia,Helvetica,Impact,LucidaConsole,LucidaSansUnicode,MSGothic,MSPGothic,PalatinoLinotype,SegoePrint,SegoeScript,SegoeUI,Tahoma,Times,TimesNewRoman,TrebuchetMS,Verdana,Wingdings,Symbol,Candara,Constantia,Corbel,Ebrima,FangSong,Gabriola,MicrosoftYaHei,MicrosoftYiBaiti,MingLiUExtB,PMingLiUExtB,SimHei,SimSun,SimSunExtB","scr":"1707x960,1707x912","cpu":"8","pt":"Win32","tzo":"Asia/Shanghai","lan":"zh-CN","wvr":"Google Inc. (NVIDIA)~ANGLE (NVIDIA, NVIDIA GeForce RTX 2060 Direct3D11 vs_5_0 ps_5_0, D3D11)","wdr":false,"mem":8,"sdv":"2.0","lns":"zh-CN,en,en-GB,en-US","tsp":"0"}" 与第二次一样

var r = n.sessionId 
	  , o = n.language
	  , i = n.tdat_code
	  , a = n.host
	  , s = n.st 
	  , c = n.devcInfo
	  , u = n.urlMap
	  , f = n.platformOS
	  , l = n.tdat_ctx;
	t = encodeURI(t);
	var d = Date.parse(new Date + "")
	  , p = d % 41
	  , h = {
		touchList: Object(T.d)("touche_message")
	}
	  , g = G.getSensorInfo(c, e)  // e =""
	  , v = {
		si: r, 
		lang: o,
		tk: H(d + q(r.length, 4) + r + q(s.length, 4) + s + q(t.length, 6) + t + JSON.stringify(h) + K(p), i, l),
		ct: H(K(d % 19) + q(r.length, 4) + r + g + d, i, l),
		version: 2,
		client: f
```


第二次check
```javascript


t = 坐标轨迹
"%7B%22ht%22:222,%22wt%22:359,%22bw%22:73,%22sw%22:359,%22mw%22:73,%22list%22:%5B%5B0,0,0%5D,%5B1,0,111%5D,%5B2,0,8%5D,%5B2,0,4%5D,%5B3,0,10%5D,%5B4,0,4%5D,%5B4,0,3%5D,%5B5,0,4%5D,%5B6,0,3%5D,%5B6,0,3%5D,%5B7,0,6%5D,%5B8,0,1%5D,%5B8,0,3%5D,%5B9,0,1%5D,%5B10,0,3%5D,%5B10,0,1%5D,%5B11,0,3%5D,%5B12,0,2%5D,%5B12,0,2%5D,%5B13,0,0%5D,%5B14,0,2%5D,%5B14,0,4%5D,%5B15,0,2%5D,%5B16,0,0%5D,%5B16,0,3%5D,%5B17,0,1%5D,%5B18,0,2%5D,%5B18,0,3%5D,%5B19,0,5%5D,%5B20,0,1%5D,%5B20,0,1%5D,%5B21,0,4%5D,%5B22,0,3%5D,%5B22,0,7%5D,%5B23,0,6%5D,%5B24,0,4%5D,%5B24,0,7%5D,%5B25,0,6%5D,%5B25,1,5%5D,%5B26,1,2%5D,%5B26,1,13%5D,%5B27,1,5%5D,%5B28,1,4%5D,%5B28,1,6%5D,%5B29,1,5%5D,%5B30,1,5%5D,%5B30,1,11%5D,%5B31,1,9%5D,%5B32,1,5%5D,%5B32,1,8%5D,%5B33,1,5%5D,%5B34,1,13%5D,%5B34,1,12%5D,%5B35,1,9%5D,%5B36,1,24%5D,%5B36,1,12%5D,%5B37,1,17%5D,%5B38,1,16%5D,%5B38,1,4%5D,%5B39,1,7%5D,%5B40,1,5%5D,%5B40,1,4%5D,%5B41,1,4%5D,%5B42,1,8%5D,%5B42,1,3%5D,%5B43,1,7%5D,%5B44,1,2%5D,%5B44,1,7%5D,%5B45,1,5%5D,%5B46,1,18%5D%5D%7D"


"{"ht":222,"wt":359,"bw":73,"sw":359,"mw":73,"list":[[0,0,0],[1,0,7],[1,0,65],[2,0,2],[3,0,3],[3,0,2],[4,0,1],[5,0,4],[5,0,0],[6,0,0],[7,0,2],[7,0,1],[8,0,2],[9,0,2],[9,0,1],[10,0,1],[11,0,2],[11,0,0],[12,0,1],[13,-1,2],[17,-1,10],[17,-1,1],[22,-1,8],[23,-1,1],[23,-1,1],[24,-1,1],[25,-1,1],[25,-1,0],[26,-1,4],[27,-1,1],[27,-1,1],[28,-1,1],[29,-1,2],[29,-1,0],[30,-1,3],[31,-1,1],[31,-1,1],[32,-1,2],[33,-1,1],[33,-1,0],[34,-1,3],[35,-1,2],[35,-1,2],[36,-1,2],[37,-1,1],[37,-1,4],[38,-1,1],[39,-1,2],[39,-1,2],[40,-1,3],[41,-1,2],[41,-1,5],[42,-1,4],[43,-1,3],[43,-1,7],[44,-1,3],[45,-1,11],[45,-1,9],[46,-1,4],[47,-1,5],[47,-1,5],[48,-1,3],[49,-1,4],[49,-1,5],[50,-1,3],[51,-1,4],[51,-1,2],[52,-1,3],[53,-1,2],[53,-1,5],[54,-1,5],[55,-1,1],[55,-1,3],[56,-1,3],[57,-1,6],[57,-1,5],[58,-1,2],[59,-1,13],[59,-1,30],[59,-1,41],[60,-1,2]]}"
ht,wt,bw,sw,mw
ht是缺口图的宽
sw = wt  wt是缺口图的长
mw = bw  是滑块的长度


touchList
[
    {
        "eid": "click",
        "did": "",
        "cn": "policy_tip-checkbox",
        "sx": 37,
        "sy": 599,
        "px": 33,
        "py": 495,
        "time": 1695305782314
    },
    {
        "eid": "click",
        "did": "",
        "cn": "input-container",
        "sx": 215,
        "sy": 207,
        "px": 211,
        "py": 103,
        "time": 1695305783282
    },
    {
        "eid": "click",
        "did": "",
        "cn": "acc-input mobile J_ping",
        "sx": 212,
        "sy": 191,
        "px": 208,
        "py": 87,
        "time": 1695305783523
    },
    {
        "eid": "click",
        "did": "authcode",
        "cn": "acc-input J_ping authcode",
        "sx": 268,
        "sy": 256,
        "px": 264,
        "py": 152,
        "time": 1695305793773
    },
    {
        "eid": "click",
        "did": "",
        "cn": "getMsg-btn text-btn J_ping timer",
        "sx": 389,
        "sy": 260,
        "px": 385,
        "py": 156,
        "time": 1695305796825
    },
    {
        "eid": "click",
        "did": "",
        "cn": "",
        "sx": 152,
        "sy": 650,
        "px": 148,
        "py": 546,
        "time": 1695305843035
    }
]

```