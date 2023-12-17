import requests

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
}

cookies = {"over18": "1"}

url = "https://www.ptt.cc/bbs/Gossiping/index.html"

res = requests.get(url, headers=HEADERS, cookies=cookies)

print(res.text)
