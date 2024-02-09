#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2024/2/7 3:08
# @Author  : wxss
# @File    : variable.py

# 这个函数用于测试必选参数、元组参数和关键字参数
# 后两种参数并没有限制数量，但是表明了输入形式
def func(must_v, *optional_v, **kw_v):
    print(must_v)
    # * 在 python 中为解包符，用于解包元组
    print(optional_v, *optional_v)
    # ** 在 python 中也为解包符，用于解包字典
    print(kw_v)


def init_func(Bool=True, intValue=0, doubleValue=10.0):
    print(Bool, intValue, doubleValue)


optionals = ('one', 1, "three")
kwargs = {"ones": 1, "two": 2, "three": 3}
# 调用函数
# 不带 * 传递参数，此时相当于传入两个可选参数，一个为元组，一个为字典
func("following: ", optionals, kwargs)
# 带 * 传递参数，分别传递了可选和关键字
func("following: ", *optionals, **kwargs)
# 解包后的字典相当于输入了几组键值对，元组相当于值
func("following: ", 'one', 1, "three", one=1, two=2, three=3)

# 参数还可以为有初值的参数
init_func()
# 传入参数，可以按顺序，也可以不按顺序通过关键字识别
init_func(intValue=10)
# 还可以传入元组
input_tuple = (True, 5, 12.3)
init_func(*input_tuple)
