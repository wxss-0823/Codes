#!D:\Users\Anaconda\anaconda3\python.exe
# -*- coding: utf-8 -*-
# @Time    : 2024/11/3 13:46
# @Author  : wxss
# @File    : hello_environ.py

import os

print("Content-type:text/html")
print()
print('<html>')
print('<head>')
print('<mata charset="utf-8">')
print('</head>')
print('<body>')
print('<b>Environment Variables</b><br>')
print('<ul>')
for key in os.environ.keys():
    print(f"<li><span style='color:green'>{key}</span>: {os.environ[key]}</li>")
print('</ul>')
print('</body>')
print('</html>')