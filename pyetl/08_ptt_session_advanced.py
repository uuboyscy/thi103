import requests
from bs4 import BeautifulSoup

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
}

landing_page_url = "https://www.ptt.cc/ask/over18?from=%2Fbbs%2FGossiping%2Findex.html"
set_cookie_url = ""
ptt_gossiping_url = "https://www.ptt.cc/bbs/Gossiping/index.html"

data = {}

ss = requests.session()

print(ss.cookies)

ss.get(ptt_gossiping_url, headers=HEADERS)

print(ss.cookies)

res_landing_page = ss.get(landing_page_url, headers=HEADERS)
soup_landing_page = BeautifulSoup(res_landing_page.text, "html.parser")

# Get set_cookie_url
set_cookie_url = "https://www.ptt.cc" + soup_landing_page.find("form").get("action")

# Set payload data
input_tag = soup_landing_page.find("input")
button_tag = soup_landing_page.find("button")
data[input_tag.get("name")] = input_tag.get("value")
data[button_tag.get("name")] = button_tag.get("value")

print(ss.cookies)

ss.post(set_cookie_url, headers=HEADERS, data=data)

print(ss.cookies)

res = ss.get(ptt_gossiping_url, headers=HEADERS, data=data)

print(res.text)
# print(ss.cookies)
