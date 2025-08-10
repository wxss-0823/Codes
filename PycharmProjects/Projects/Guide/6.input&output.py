#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2024/2/1 23:11
# @Author  : wxss
# @File    : 6.input&output.py
import pickle
import pprint


# repr 会自动转义特殊字符
print(str("wxss\n2024"))
print(repr("wxss\n2024"))

# repr 输出表
for i in range(1, 11):
  # rjust 方法，字符靠右，左边填充空格
  print(repr(i).rjust(2), repr(i * i).rjust(3), end=" ")
  print(repr(i * i * i).rjust(4))

# str.format() 输出表
for i in range(1, 11):
  print("{0:2d} {1:3d} {2:4d}".format(i, i * i, i * i * i))

# pickle 实例
output = open("6.data.txt", "wb")
data = {
  "a": [1, 2.0, 3, 4+6j],
  "b": ('string', u'Unicode string'),
  "c": None
}

self_ref_list = [1, 2, 3]
self_ref_list.append(self_ref_list)

# Pickle dictionary using protocol 0
pickle.dump(data, output)

# Pickle dictionary using the highest protocol available
pickle.dump(self_ref_list, output, -1)

output.close()

pkl_file = open("6.data.txt", "rb")
# 重构对象
data1 = pickle.load(pkl_file)
pprint.pprint(data1)

data2 = pickle.load(pkl_file)
pprint.pprint(data2)
