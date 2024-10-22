from curl_cffi import requests

req = requests.get("https://hanime1.me", impersonate="chrome110")
print(req.text)
