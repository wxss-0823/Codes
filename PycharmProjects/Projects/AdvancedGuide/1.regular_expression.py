#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2024/2/2 13:26
# @Author  : wxss
# @File    : 1.regular_expression.py

import re


def reMatch():
    # 从头匹配字符串
    print(re.match("www", "www.Runoob.com").span())
    # 不从头开始
    print(re.match("com", "www.Runoob.com"))

    # group & groups 实例
    line = "Cats are smarter than dogs"

    # .* 表示匹配除换行符（\n、\r）之外的任何单个或多个字符串
    # .*? 表示”非贪婪“模式，只保存第一个匹配到的字符串
    matchObj = re.match(r'(.*) are (.*?) .*', line, re.M | re.I)

    if matchObj:
        print("matchObj.group(): ", matchObj.group())
        print("matchObj.group(1): ", matchObj.group(1))
        print("matchObj.group(2): ", matchObj.group(2))
        print("matchObj.group(1, 2): ", matchObj.group(1, 2))
        print("matchObj.groups(): ", matchObj.groups())
    else:
        print("No match!")

    return


def reSearch():
    # 从头开始匹配字符串
    print(re.search("www", "www.Runoob.com").span())
    # 不从头开始
    print(re.search("com", "www.Runoob.com").span())

    # group & groups 实例
    line = 'Cats are smarter than dogs'

    # .* 表示匹配除换行符（\n、\r）之外的任何单个或多个字符串
    # .*? 表示”非贪婪“模式，只保存第一个匹配到的字符串
    searchObj = re.search(r'(.*) are (.*?) .*', line, re.M | re.I)

    if searchObj:
        print("matchObj.g(): ", searchObj.group())
        print("matchObj.group(1): ", searchObj.group(1))
        print("matchObj.group(2): ", searchObj.group(2))
        print("matchObj.group(1, 2): ", searchObj.group(1, 2))
        print("matchObj.groups(): ", searchObj.groups())
    else:
        print("No match!")

    return


def reSub():
    phone = '132-3959-3967 # 这是我的电话号码'

    # 删除注释
    num = re.sub(r'#.*$', '', phone)
    print('电话号码：', num)

    # 移除非数字的内容
    num = re.sub(r'\D', "", phone)
    print('电话号码：', num)

    # repl 参数是一个函数
    # 将匹配到的数字乘以 2
    def double(matched):
        value = int(matched.group('value'))
        return str(value * 2)

    s = 'A23G4HFD567'
    # 将字符串分组处理并命名为 value
    print(re.sub(r'(?P<value>\d+)', double, s))
    return


def reCompile():
    pattern = re.compile(r'\d+')
    m = pattern.match('one12twothree34four', 3)
    print(m.span())

    pattern1 = re.compile(r'([a-z]+) ([a-z]+) ([a-z]+) ([a-z]+)', re.I) # re.I 表示忽略大小写
    m = pattern1.match("Hello World Wide Web!")
    print(m.groups())
    return


def reFindall():
    # 单个匹配模式，返回列表
    result1 = re.findall(r'\d+', 'runoob 123 google 456')

    pattern = re.compile(r'\d+')
    result2 = pattern.findall('runoob 123 google 456')
    result3 = pattern.findall('runoob 123 google 456', 0, 10)

    print(result1)
    print(result2)
    print(result3)

    # 多个匹配模式，返回元组列表
    result = re.findall(r'(\w+)=(\d+)', 'set width=20 and height=10')
    print(result)

    return


def reFinditer():
    iterable = re.finditer(r'\d+', '12a32bc43jf3')
    print(next(iterable).group())
    for item in iterable:
        print(item.group())


if __name__ == '__main__':
    reFinditer()
