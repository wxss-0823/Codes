#!D:\Users\Anaconda\anaconda3\python.exe
# -*- coding: utf-8 -*-
# @Time    : 2026/1/12 11:06
# @Author  : Coffee
# @Project : Auxiliary
# @File    : CalcTuningF.py


from cmath import sqrt
from typing import List

from numpy import pi

# 计算谐振频率
C: List[complex] = [29.6e-12, 85e-12, 30e-12, 55e-12, 30e-12]
L: List[complex] = [500e-9, 400e-9, 250e-9, 650e-9, 250e-9]
f_resonant: List[complex] = [0 for _ in range(len(C))]

for i in range(len(C)):
  f_resonant[i] = 1 / sqrt(C[i] * L[i])
  print(f"Resonant Frequency: {"{:.3e}".format(f_resonant[i])}")

# 计算特定频率下阻抗
f = 2e6
Z: List[complex] = [0 for _ in range(len(C))]

for i in range(len(C)):
  Z[i] = 1j * (2 * pi * f * L[i] - 1 / (2 * pi * f * C[i]))
  print(f"Z[i]: {"{:.3e}".format(Z[i])}")

zc = 1 / (2 * pi * 2e6 * 13e-12)
zl = 2 * pi * 2e6 * 2000e-9
print(zc)
print(zl)
