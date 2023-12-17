import requests
from bs4 import BeautifulSoup

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
}


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
            article_url = a_element.get("href")
            print(a_element.text)

    next_link = soup.find("a", string="‹ 上頁")
    # return "https://www.ptt.cc" + next_link.get("href")
    return ("https://www.ptt.cc" + next_link.get("href")) if next_link else None


url = "https://www.ptt.cc/bbs/Stock/index.html"
next_page = get_stock(url)

page = 0
while page < 5:
    next_page = get_stock(next_page)

    page += 1
