import requests
from bs4 import BeautifulSoup


HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
}

url = "https://www.newmobilelife.com/wp-json/csco/v1/more-posts"

data = {"action": "csco_ajax_load_more", "page": 2, "posts_per_page": 30}

res = requests.post(url, headers=HEADERS, data=data)

print(type(res.json()))
