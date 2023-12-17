import requests

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
}

url = "https://www.ptt.cc/bbs/Gossiping/index.html"

ss = requests.session()

ss.cookies["over18"] = "1"

res = ss.get(url, headers=HEADERS)

print(res.text)
