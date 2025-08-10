#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2024/2/2 2:13
# @Author  : wxss
# @File    : 8.namespace.py

def outer():
  # 外部的 num
  num = None

  def inner():
    # 定义为非内部的 num，会读取外部 num 的值
    nonlocal num
    print(num)
    num = 100

  inner()
  print(num)


outer()
