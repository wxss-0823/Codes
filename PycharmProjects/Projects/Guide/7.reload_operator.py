#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2024/2/2 1:52
# @Author  : wxss
# @File    : 7.reload_operator.py

class Vector:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __str__(self):
        return f"Vector({self.a}, {self.b})"

    def __add__(self, other):
        return Vector(self.a + other.a, self.b + other.b)


v1 = Vector(1, 2)
v2 = Vector(2, 3)
print(v1 + v2)