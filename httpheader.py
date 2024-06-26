import requests as req
url = "http://mercury.picoctf.net:1270"
header = {
        "User-Agent":"PicoBrowser",
        "Date":"2018",
        "Referer":"mercury.picoctf.net:1270",
        "DNT":"0",
        "X-Forwarded-For": "31.3.152.55",
        "Accept-Language":"sv"
        }
res = req.get(url , headers=header)
print(res.text)
