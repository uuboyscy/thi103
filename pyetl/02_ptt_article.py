import os
import time

import requests
from bs4 import BeautifulSoup

from crawler_utils import extract_article, HEADERS

folder_name = "ptt_article"
if not os.path.exists(folder_name):
    os.mkdir(folder_name)


def get_stock(url):
    response = requests.get(url, headers=HEADERS)
    html = response.text

    soup = BeautifulSoup(html, "html.parser")

    # [find] find_all -> return list[Tag] ; find -> return Tag
    div_elements = soup.find_all("div", class_="title")
    div_elements = soup.findAll("div", class_="title")
    # div_elements = soup.find_all("div", {"class": "title"})

    # [select] select -> return list[Tag] ; select_one -> return Tag
    div_elements = soup.select("div.title")
    div_elements = soup.select('div[class="title"]')
    # div_elements = soup.select_one("div.title")

    for div_element in div_elements:
        a_element = div_element.find("a")
        if a_element and "公告" not in a_element.string and "閒聊" not in a_element.string:
            article_title = a_element.text
            article_url = "https://www.ptt.cc" + a_element.get("href")

            # Extrac article content string
            article_content_str = extract_article(article_url)

            for abnormal_word in [":", "?", "$", "@", "/"]:
                article_title = article_title.replace(abnormal_word, "")

            with open(f"{folder_name}/{article_title}_{time.time_ns()}.txt", "w", encoding="utf=8") as f:
                f.write(article_content_str)

            print(article_title)

    next_link = soup.find("a", string="‹ 上頁")
    return ("https://www.ptt.cc" + next_link.get("href")) if next_link else None


url = "https://www.ptt.cc/bbs/Stock/index.html"
next_page = get_stock(url)

page = 0
while page < 5:
    next_page = get_stock(next_page)

    page += 1