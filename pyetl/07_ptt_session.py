import requests

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
}

landing_page_url = "https://www.ptt.cc/ask/over18?from=%2Fbbs%2FGossiping%2Findex.html"
set_cookie_url = "https://www.ptt.cc/ask/over18"
ptt_gossiping_url = "https://www.ptt.cc/bbs/Gossiping/index.html"

data = {
    "from": "/bbs/Gossiping/index.html",
    "yes": "yes",
}

ss = requests.session()

print(ss.cookies)

ss.get(ptt_gossiping_url, headers=HEADERS)

print(ss.cookies)

ss.get(landing_page_url, headers=HEADERS)

print(ss.cookies)

ss.post(set_cookie_url, headers=HEADERS, data=data)

print(ss.cookies)

res = ss.get(ptt_gossiping_url, headers=HEADERS, data=data)

# print(res.text)
print(ss.cookies)
