from typing import List

import requests
from bs4 import BeautifulSoup

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
}


class ArticleInfo:

    def __init__(self, article_title: str, article_url: str) -> None:
        self.article_title = article_title
        self.article_url = article_url


class PttIndexInfo:

    def __init__(self, next_link: str, article_info_list: List[ArticleInfo]) -> None:
        self.next_link = next_link
        self.article_info_list = article_info_list


def extract_article(article_url: str) -> str:
    response = requests.get(article_url, headers=HEADERS)
    soup = BeautifulSoup(response.text, "html.parser")
    main_content_tag = soup.find("div", id="main-content")
    
    for tag in ["div", "span", "a"]:
        for extract_tag in main_content_tag.find_all(tag):
            extract_tag.extract()
    
    return main_content_tag.text


def get_stock(url: str) -> PttIndexInfo:
    response = requests.get(url, headers=HEADERS)
    html = response.text

    soup = BeautifulSoup(html, "html.parser")

    # [find] find_all -> return list[Tag] ; find -> return Tag
    div_elements = soup.find_all("div", class_="title")

    article_info_list = []
    for div_element in div_elements:
        a_element = div_element.find("a")
        if a_element and "公告" not in a_element.string and "閒聊" not in a_element.string:
            article_title = a_element.text
            article_url = "https://www.ptt.cc" + a_element.get("href")
            article_info_list.append(
                (article_title, article_url)
            )

    next_link = soup.find("a", string="‹ 上頁")

    return PttIndexInfo(
        ("https://www.ptt.cc" + next_link.get("href")) if next_link else None,
        article_info_list,
    )


if __name__ == "__main__":
    article_url = "https://www.ptt.cc/bbs/joke/M.1702623731.A.B52.html"
    print(extract_article(article_url=article_url))