import os
import time

from crawler_utils import extract_article, get_stock

folder_name = "ptt_article"
if not os.path.exists(folder_name):
    os.mkdir(folder_name)


url = "https://www.ptt.cc/bbs/Stock/index.html"
next_page = get_stock(url)
print(next_page.next_link)

page = 0
while page < 5:
    next_page = get_stock(next_page.next_link)
    print(next_page.next_link)
    for article_info in next_page.article_info_list:
        print(article_info.article_title)
        print(article_info.article_url)
        # Extrac article content string
        article_content_str = extract_article(article_info.article_url)

        for abnormal_word in [":", "?", "$", "@", "/"]:
            article_title = article_title.replace(abnormal_word, "")

        with open(f"{folder_name}/{article_title}_{time.time_ns()}.txt", "w", encoding="utf=8") as f:
            f.write(article_content_str)

    page += 1