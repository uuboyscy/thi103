import pprint

import requests
import json

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
}

url = "https://www.nownews.com/nn-client/api/v1/cat/entertainment/?pid=6324000"

res = requests.get(url, headers=HEADERS)

json_data = json.loads(res.text)

# pprint.pprint(json_data)

for news in json_data.get("data").get("newsList"):
    img_url = news["imageUrl"]
    res_img = requests.get(img_url, headers=HEADERS)

    with open(f"nownews_img/{news['id']}.webp", "wb") as f:
        f.write(res_img.content)

    # print(news)
    print("===============")
