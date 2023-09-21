---
title: jd的fp请求
date: 2023-09-21 21:09:01
tags: []
index_img: ../banner_images/banne_photo83.png
---

```javascript
function Q(t, e, n) {
	"string" != typeof t && (t = JSON.stringify(t));
	var r = n.sessionId  由login获取
	  , o = n.language   1
	  , i = n.tdat_code   99992
	  , a = n.host "//jcap.m.jd.com"
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
	  , g = G.getSensorInfo(c, e)
	  , v = {
		si: r,
		lang: o,
		tk: H(d + q(r.length, 4) + r + q(s.length, 4) + s + q(t.length, 6) + t + JSON.stringify(h) + K(p), i, l),
		ct: H(K(d % 19) + q(r.length, 4) + r + g + d, i, l),
		version: 2,
		client: f
	};
	return T.a.interfaceId = 268435460,
	T.a.interfaceName = "check",
	N({
		method: "post",
		url: "".concat(a).concat(u.check),
		data: v
	})
}

```