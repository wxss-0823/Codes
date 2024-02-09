import requests

head = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"}
url = "http://books.toscrape.com/"
response = requests.get(url, headers=head)
if response.ok:
    print(response.text)
else:
    print("爬取失败！")
