from bs4 import BeautifulSoup
import requests

content = requests.get("http://books.toscrape.com/").text
soup = BeautifulSoup(content, "html.parser")

# 获取价格
price_dict = []
price_kwargs = {
    "attrs": {"class": "price_color"}
}
all_prices = soup.findAll("p", **price_kwargs)
for items in all_prices:
    price_dict.append(items.string[2:])

# 获取书名
name_dict = []
all_titles = soup.findAll("h3")
for title in all_titles:
    all_links = title.findAll("a")
    for link in all_links:
        name_dict.append(link.string)

# 打印书名与价格
book_price = {}
for i in range(len(name_dict)):
    book_price[name_dict[i]] = price_dict[i]

for key, value in book_price.items():
    print(key + ": " + value)
