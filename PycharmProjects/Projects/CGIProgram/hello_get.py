#!D:\Users\Anaconda\anaconda3\python.exe
# -*- coding: utf-8 -*-
# @Time    : 2024/11/3 13:56
# @Author  : wxss
# @File    : hello_get.py

# CGI 处理模块
import cgi, cgitb

# 创建 FiledStorage 的实例化
form = cgi.FieldStorage()

# 获取数据
site_name = form.getvalue('name')
site_url  = form.getvalue('url')

print("Content-type:text/html")
print()
print('<html>')
print('<head>')
print('<mata charset="utf-8">')
print('</head>')
print('<body>')
print(f'<h2>{site_name}官网：{site_url}</h2>')
print('</body>')
print('</html>')