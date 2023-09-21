---
title: jd的m端滑块
date: 2023-09-20 17:23:59
tags: []
index_img: ../banner_images/banne_photo86.png
---
先拿到原来的图片，然后对图片的正确大小，用网页进行缩放使其达到正常的图片大小，然后根据断点滑块的值来判断最后滑动的距离。

![](../images/Pasted%20image%2020230920172406.png)


![](../images/Pasted%20image%2020230921204808.png)


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






si的值 "Xg0aRAABAAAFmK5kzRwAMKVa_Y9J2O3Ykj5TQDFqCdp-zeR8FRzerqJXwRqY8Wm-In2e_ikG492CF27dIzauDgAAAAA"

tk= "{"data":"SrI7IVcFlDJKHcJF9S2uIY-HrhrO1BfEsDB9zP13Fw2J7swJQDMKtNPEOpSAYd5E_8jY58cWRwrZ\nJGaY69oqjjHvH85oi8KltSPHkOaLiDE6d7xFVvGtDVcKxqsnPj0A4PjIcWRFkgqLrenlUY9mleXF\nPrCYud2ll22tRuVhHUWiOEKyWmqn-JF5zRhvCg5AjQR8MN6w2DN_4UwrmmlwVJPz6bWWJR5aYH0i\n1W9QF1CpYr9Nz4Znv-wR8T4pmIFvImnBIH_FUyRNKT3hlS3ndin7e10qLmQxzRWwmmWZtrJou7Ll\ns205EV_mKWtZFije8H4QVnm7lo50bS7gJ44oAI-IShlxXLB-IEwG381FNQQdhAYW7EZ0Rdx6yqOU\ngs510GwvcHplXCa_efCCi9JOxRWekLH7T6E8j-j0ug0TW7ZHStafC1Xn4OLXU8e_t_trtW00U5q7\n9UsNTIR0lwkBequBcwS6XOrNGjAcr60Um3BxULggmjQzG_1bLvbOVtI885NwANGbC1Mbm1B5hfgZ\n0gFjYB3_ihS-2InjtrQZ-U-veeQ-61KLS2A7IP29ii6VUCMcyxqRX1At-KGzgFuKeyg1lku3EoTi\n4bc5osvLdmjOpAYYDiTSNUYAQBSrH5xXON4xTafenOrWyXjKpGRudNCF8UBEadjV7IWm8FsB2CWd\ndA4qDcQiObjjJEly0lab2j4c-yoBBaTQ2maiCGUkSmX4-myZWUJId4pNtf9SuHk6LeoKmrKeKr9v\n-942Yp8ESq3_0iykE8-rAgu8hcp-Ff4oxVrkpli43avF1q5efSAUexiT7M-GD5AP5W7R8pOXT0JA\nzRZatcvbRK9soBEoAXs04N8HUmF5FQ7wdPYBCcg8HoTp6itUcHmh0Nvih3Wgo31n_oMRFHERUBsk\nrsId-js90nfqtVo7z_GUXFgJ-0HCubuOhqbsvwRJPtPqZ1O8cKc60Mp5mwtGjHWuO-HYRwLUfz-I\n5nG4nuRia06V-TZ-MIuYPONq0YzmoS5x4Nca74XpFXKQXXNhmALHvj1j4EZnE3ixYSSbiKq_k7bx\nQJ9J0QWXYfzPZ5SkeBSEciqPhS_oUklg1IajsOppomgodT4fGdLxtuXCB76mdnOuEqbiC19ZFfdA\nTmmTJj-E4XgpBLVA5091eEb0gB5RBU0nUodwFFecsEMps7vT-9wzXxSUgxGW2FbbvF97w0CH97lz\npXzbYcoX24KuAdlyQQSCxXLObSFDna4uUh9XcGfPCR2_BvTffHGTm8c-k0rNY0n6JJsR_KwywUqp\nxjF80m6UT1ZyU86AMIqk9qMQSk4nT-h3U6JctnRM54SSt2cWUjjZViftgMlnYQ6gLF6h29xdeb8o\n705cq8_raXDEhjsbPo1tc_YBNegvL7i5pHL9gmZaXThCFGc6q7zansbSADNCBaUL5RZzjacz_oiu\n7FvVqhucweG2JV1w7NspBoLII4jUANwiGqtXT95RGS638WRPAKfpu0ormeOYaV1-SNEgwXhjykOs\nRzsGWd0lGY1148MivOZn3oHy6NbPN9_0FH-ytl6deCER5T0ZVr66SbdtLBxRrwepkktBBNfQ6RzI\nDMwPccCgzzjZ_926wshKNlP6keQlSqh5ytD7OaFaI65GHzqaVPiMe2d0elStpuU_ILyBP5P5RLgl\nwANL1Ej_kd-qLduaga-wX8NOoBC7qkI9THk8EPocAvkIYKcK2wKR6G_ksX8VvBytU1F4aoDyn-7W\nWh1_0S_U1Cp3V2dSYZW24FwkPzd2wX7taRiwCdzh7eODNRTOmuYbRDaz8b_tLO9FIw51qffrrnfO\nKjprGKsx6dWXH_i34IqMpE9-ZRRJi6wqmL4eF8IotRiGvjsnvHn8_6DXoW301Vw10FkMxWS5i0NR\n4ZZh5pFnXuzghiUqgwrBGIjc7GqPZEOAbAoDj-c_Sp1MseO_uJthfZ-czP8bpvbgOXNZ106ZlV6i\ny074AE2cDxpZKTcCA7cfKQvN3YCENCesaYAX9yQysxUBfPYXLaJcbHRkXTkKIVv56cuAG2eiwMuj\nPAVfXEvxCQmEBIVu2Y3qp7uKXW5QDiODXANFsVYebWjqKHLucBwU8lDWs6WsnIA62Ja1azTqc1wq\nVtaVYV7xWRRBOjeDGy3XVXSmsaWkS2z2obkoR3IPiwvq3r8yauMb1XLRvN71O0HU2hMgpq8di3CT\nkAhc8BGbqCbU-v378sm46-LtkZJyyse1GmWzMUS6R_oU1YsqTuTyC8LbfECOBCcYfvl3rekuT-l0\nBCno6ARJNbQ2YsV6lNnI03rvBwm463_PJZnBeYr_rPlbFyjHRzjiwEpgZ_HNf5tDu4EKPFSr6uB5\nG7M1-YZYHk2qEsBRIAnpYfWxkRHr8L_ZZ-dxApJeVi0aEnVJ2SurMQ8gDH7Ysdds1xnfsZSAGHMt\nGPj1vCmHvSQLwLYhO7kWvM2tV2BCjj0uiOe8qmj1TpilxJUG5DZNm8hvwoigSOw0i5kVUwJuuCqR\nzFtex0Ct5C8bzAPnlWCiax5CDbQYjvfbFwDchJLCHfKU0jyIh-Xlr6NRPpz835erYYeNYUx5JTks\n19UZb74T86r4Nvzkl-MJZX4WusSQ5pgLSzTbfZ9S0bMq3iY38A_HnN-_igEpQO3woQniM32tzUhv\nK3H59Phkc74mq5zVyuPwTAR77iWfVeF7GKqm9PiNF-geg7jpKXdRNsV7NP4Z_8zkUtl80y23Kytw\nYsTU0W70qizXw7C2td8volFKSiw2ZfU_v9KODsep9qgkSo1BDqvq-4VnHPyAlQ1YrPBd1_lyHQLp\no8t5e37j6qMaH4Fu_moWlX68enS11TGrLts2j2Abor9ASsZO1f3dNFmtpWvmWvYqTe7oD6jWBcqI\nHb6TGQv4nb3wFUCp1Ir3osJMyhK87Qe064Kwie6gFwli12NwmCU2A4faGA1W-EL2DPq9Cv8suq6I\nTrE0y7rGd3a5JphT7tkF7GMF-tJhn4K7LZ8i_AaocoD4FGj_kfHB6cY5ICwLihWy0mH7PXff3_Tx\nUNX3BMAtkKTWR23LngW0JQsRCaKcaAu7NnTRH7YPg5I82RjVT62mHmb9AialzytFhBttKmpQXx1w\nC4WejfLIWCAI_pgK4cTVkZlTzylc287KY_RtI6EZyUf36WUiilduIUemhR5xbiLssZfqW_xr7FQV\nxsvYrpy1xQzR5G9r_tc_rB5PyEJgWaGvPO9AcponivBdDIiKMt3baZ7MdCP_WOxEBl_OBpysIaL6\nX3jPI9t7Ec7yD8_j9HU5A8_yLJdlExqGAOEdCo36EGknZmKBfvoLEOp_hRjSFP1DVxrogCoo0qTT\nZGc-5_Wjldmu_Qu5DsKOw6nf5xrsIoNFBkLXXNEbksjxewqv8O1huPs5KnXsTyYnxIYr45ZWuTWa\ns1sc-PSYb475FTypSilqrLfnflFGTSLaS3617achNKmS8h8_48Pq81gZityaF9x4q0o_5ne7nw5f\nwrXGv51GpdTIx9AQNFhS9AWQ3PKeayFs0OWatSs5cxqVpQ==","version":2}"




```