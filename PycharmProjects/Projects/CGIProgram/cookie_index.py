#!D:\Users\Anaconda\anaconda3\python.exe
# -*- coding: utf-8 -*-
# @Time    : 2024/11/3 15:51
# @Author  : wxss
# @File    : cookie_index.py

# 导入模块
import os
import http.cookies

print("Content-type: text/html")
print()

print("""
<html>
<head>
<meta charset="utf-8">
<title>Cookie Index</title>
</head>
</html>
<body>
<h1>Loading cookie info</h1>
""")

if 'HTTP_COOKIE' in os.environ:
    cookie_string = os.environ.get('HTTP_COOKIE')
    c = http.cookies.SimpleCookie()
    c.load(cookie_string)

    try:
        data = c['name'].value
        print(f"cookie data: {data} <br>")
    except KeyError:
        print("cookie is not set or out")

print("""
</body>
</html>
""")