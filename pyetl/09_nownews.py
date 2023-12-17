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
    print(news)
    print("===============")
