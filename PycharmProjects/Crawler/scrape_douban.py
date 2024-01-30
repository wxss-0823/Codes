from bs4 import BeautifulSoup
import requests


header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                  "AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/121.0.0.0 "
                  "Safari/537.36 "
                  "Edg/121.0.0.0"
}
title_list = []

for start_num in range(0, 250, 25):
    response = requests.get(f"https://movie.douban.com/top250?start={start_num}&filter=", headers=header)
    html = response.text
    soup = BeautifulSoup(html, "html.parser")
    title_kwargs = {
        "attrs": {"class": "title"}
    }
    all_titles = soup.findAll("span", **title_kwargs)
    for title in all_titles:
        title_string = title.string
        if "/" not in title_string:
            title_list.append(title_string)

# for items in title_list:
#     print(f"{title_list.index(items) + 1}: {items}")

with open("doubanTOP250.txt", "w") as f:
    for i in range(len(title_list)):
        f.write(f"{i + 1}: {title_list[i]}\n")


