---
title: 第一步 jcapsid
date: 2023-09-21 10:06:38
tags: []
index_img: ../banner_images/banne_photo78.png
---

```python
curl 'https://plogin.m.jd.com/cgi-bin/mm/new_login_entrance?lang=chs&appid=300&returnurl=https:%2F%2Fwq.jd.com%2Fpassport%2FLoginRedirect%3Fstate%3D3349177940%26returnurl%3Dhttps%253A%252F%252Fhome.m.jd.com%252FmyJd%252Fhome.action&source=wq_passport&risk_jd\[eid\]=&risk_jd\[fp\]=b8ca252e09666b8b4f51be6a51759e49' \
  -H 'authority: plogin.m.jd.com' \
  -H 'accept: application/json, text/plain, */*' \
  -H 'accept-language: zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6' \
  -H 'cache-control: no-cache' \
  -H 'content-type: application/x-www-form-urlencoded' \
  -H 'cookie: shshshfpb=AAl4W4raKEl6iuVm8JfmlUxMQtLXmSxaVKFNjQAAAAAA' \
  -H 'dnt: 1' \
  -H 'pragma: no-cache' \
  -H 'referer: https://plogin.m.jd.com/login/login?appid=300&returnurl=https%3A%2F%2Fwq.jd.com%2Fpassport%2FLoginRedirect%3Fstate%3D3349177940%26returnurl%3Dhttps%253A%252F%252Fhome.m.jd.com%252FmyJd%252Fhome.action&source=wq_passport' \
  -H 'sec-ch-ua: "Microsoft Edge";v="117", "Not;A=Brand";v="8", "Chromium";v="117"' \
  -H 'sec-ch-ua-mobile: ?0' \
  -H 'sec-ch-ua-platform: "Windows"' \
  -H 'sec-fetch-dest: empty' \
  -H 'sec-fetch-mode: cors' \
  -H 'sec-fetch-site: same-origin' \
  -H 'user-agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36 Edg/117.0.2045.31' \
  --compressed


请求参数（均不变）
1. lang: chs
2. appid: 300
3. returnurl:https://wq.jd.com/passport/LoginRedirect?state=3349177940&returnurl=https%3A%2F%2Fhome.m.jd.com%2FmyJd%2Fhome.action
4. source: wq_passport
5. risk_jd[eid]:
6. risk_jd[fp]:b8ca252e09666b8b4f51be6a51759e49 
下面的st是有这个请求（s_token数据）得到的
响应值 = {
   "country_code_switch" : true,
   "enable_smslogin" : true,
   "enable_usernamelogin" : true,
   "err_code" : 0,
   "err_msg" : "",
   "jcap_domain" : "jcap.m.jd.com",
   "kepler" : false,
   "kpkey_switch" : false,
   "logoUrl" : "",
   "mobile" : "",
   "need_auth" : true,
   "onekeylog_switch" : false,
   "only_login" : true,
   "qblog_switch" : false,
   "rsa_modulus" : "BA393683B1CD20CE149344349E9C8E1AA9517CC9260AF69E7F467187C7B1AE5C0563A2391673FCCF0F211E1F776FF079C1F580E8FA6AD2DA2BCCD0B4EE49866BAE61BE5A7AF1A3DF18FD2EEF969372DB745007BE87CB8FC484C359B38F9B07066D0E761DF36F691721544A6C714472088B658BDB1B652870036F3BCDA2CE8E09",
   "s_token" : "h3z59cv4",
   "show_applelogin" : false,
   "show_checkbox" : false,
   "show_jdpaylogin" : false,
   "show_otherlogin" : true,
   "show_title" : true,
   "show_wxlogin" : false,
   "tpl" : "",
   "unmodified_name" : ""
}



```


```javascript

generateUuid: function() {
            for (var h = "xxxxxxxx-xxxx-4xxx-yxxx-xxxxxxxxxxxx".split(""), k = 0, a = h.length; k < a; k++)
                switch (h[k]) {
                case "x":
                    h[k] = t.floor(16 * t.random()).toString(16);
                    break;
                case "y":
                    h[k] = (t.floor(4 * t.random()) + 8).toString(16)
                }
            return h.join("")
}


mac: function(v) {
            for (var x = -1, w = 0, A = v.length; w < A; w++)
                x = x >>> 8 ^ t[(x ^ v.charCodeAt(w)) & 255];
            return (x ^ -1) >>> 0
}


parse: function(h) {
            for (var k = h.length, a = [], b = 0; b < k; b++)
                a[b >>> 2] |= (h.charCodeAt(b) & 255) << 24 - b % 4 * 8;
            return new A.init(a,k)
}

jd_shadow__ = function() {
    try {
        var t = JDDSecCryptoJS
          , u = [];
        u.push("plogin.m.jd.com/login/login");
        var v = t.lib.UUID.generateUuid(); //a2accc18-4cec-4b8b-a5e3-e57f937095341695298313786
        u.push(v);
        var x = (new Date).getTime();  //1695298281088
        u.push(x);
        //u.join("") = "plogin.m.jd.com/login/logina2accc18-4cec-4b8b-a5e3-e57f937095341695298313786"
        var w = t.SHA1(u.join("")).toString().toUpperCase();
        u = [];
        u.push("JD3");
        u.push(w);
        var A = (new JDDMAC).mac(u.join(""));
        u.push(A);
        var y = t.enc.Hex.parse("30313233343536373839616263646566")
          , n = t.enc.Hex.parse("4c5751554935255042304e6458323365")
          , f = u.join("");
        return t.AES.encrypt(t.enc.Utf8.parse(f), n, {
            mode: t.mode.CBC,
            padding: t.pad.Pkcs7,
            iv: y
        }).ciphertext.toString(t.enc.Base32)
    } catch (e) {}
}()
```


```
token参数生成是请求
curl 'https://payrisk.jd.com/m.html' \
  -H 'Accept: */*' \
  -H 'Accept-Language: zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6' \
  -H 'Cache-Control: no-cache' \
  -H 'Connection: keep-alive' \
  -H 'Cookie: mba_muid=1695299601792779320572; __jd_ref_cls=MLoginRegister_SMSReceiveCode' \
  -H 'DNT: 1' \
  -H 'Pragma: no-cache' \
  -H 'Referer: https://plogin.m.jd.com/' \
  -H 'Sec-Fetch-Dest: script' \
  -H 'Sec-Fetch-Mode: no-cors' \
  -H 'Sec-Fetch-Site: same-site' \
  -H 'User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36 Edg/117.0.2045.31' \
  -H 'sec-ch-ua: "Microsoft Edge";v="117", "Not;A=Brand";v="8", "Chromium";v="117"' \
  -H 'sec-ch-ua-mobile: ?0' \
  -H 'sec-ch-ua-platform: "Windows"' \
  --compressed

响应数据为：var jd_risk_token_id = 'PP3UPD2FJQD77FCZGVGHJMUHMTHR77WWPY7GKN4AEA3472SKA4HFIE75PFQ53DLUGRYRSZP65ZHKQ';

```




```
jstub参数生成位置 ：103个字符
```
![](../images/Pasted%20image%2020230921173349.png)
```python

data = { 'st': '7wq6lt1n', 'mod': 'smslogin', 'username_phone': '13411111111', 'risk_jd[eid]': '', 'risk_jd[fp]': 'b8ca252e09666b8b4f51be6a51759e49', 'risk_jd[sdkToken]': '', 'risk_jd[token]': 'V6X43Y32UMGDJNWARM6TTAB22CLIWQGHNXJ5SB4YUFN3AFF3VBAEYBY4TYAED3IAO2ZFAJXV7SGE2', 'risk_jd[jstub]': 'AOZ7XUKWP64WZJBHOXV3N3JE2H27L3KDVKONU6YXZBCGCB6TSAFWDT6JNSM7UNX3A5PPR44VYRN6RMYC3LSUNCE2IQZ4V5CQJRAJ5XI', 'risk_jd[fpstep]': 'nb1695261896170', }








mod = 固定 解决
username_phone = 手机号 解决
st = 会变 （时间戳） s_token 解决
risk_jd[eid] = 会变 可为空 解决
risk_jd[token]  = 会变  
risk_jd[jstub]  = 会变  解决
risk_jd[fpstep]  = 会变  nb+时间戳 解决
risk_jd[fp] = 上面的fp参数 解决

```


#### 返回 jcap_sid == si给第二步