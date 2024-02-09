#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2024/2/5 0:57
# @Author  : wxss
# @File    : scrape_novel.py
import requests
from bs4 import BeautifulSoup


def get_novel_chapters():
    root_url = 'http://www.89wx.cc/41/41060/'
    root_html = requests.get(root_url)
    soup = BeautifulSoup(root_html.text, "html.parser")
    data_list = []
    # 查找 "dd" 元素
    for dd in soup.findAll("dd"):
        part_url = dd.find('a')['href']
        data_list.append((f"http://www.89wx.cc{part_url}", dd.find("a").text))
    return data_list


def get_chapter_content(content_url):
    html = requests.get(content_url)
    soup = BeautifulSoup(html.text, "html.parser")
    return soup.find("div", attrs={"id": "content"}).text


data = get_novel_chapters()
for url in data[:10]:
    content = get_chapter_content(url[0])
    # replace 函数返回一个原字符串的拷贝，但不会更改原字符串
    pure_content = content.replace(u'\xa0', '')
    # win 系统默认新建的 txt 文件编码为 GBK，网页抓取的内容含有 &nbsp 即 \xa0
    # 无法直接写入，需要替换，此时编码模式不重要
    with open('novel.txt', 'a', encoding='utf-8') as f:
        f.write(f'{url[1]}\n')
        f.write(pure_content + '\n')
