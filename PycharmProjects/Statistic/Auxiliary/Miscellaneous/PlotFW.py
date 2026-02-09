#!D:\Users\Anaconda\anaconda3\python.exe
# -*- coding: utf-8 -*-
# @Time    : 2026/1/12 11:48
# @Author  : Coffee
# @Project : Auxiliary
# @File    : PlotFW.py


import matplotlib.pyplot as plt
import numpy as np


def plot_function(func_str, x_range=(1e6, 8e7), points=1000):
  """快速绘制任意函数"""
  x = np.linspace(x_range[0], x_range[1], points)

  # 安全地计算y值
  try:
    y = eval(func_str, {'f': x, 'np': np, 'sin': np.sin, 'cos': np.cos,
                        'tan': np.tan, 'exp': np.exp, 'log': np.log,
                        'sqrt': np.sqrt, 'pi': np.pi, 'square': np.square})

    plt.rcParams['font.sans-serif'] = ['Microsoft YaHei']  # 微软雅黑
    plt.rcParams['axes.unicode_minus'] = False

    plt.figure(figsize=(10, 6))
    plt.plot(x, y, 'b-', linewidth=2)
    plt.title(f'函数图像: y = {func_str}')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.grid(True, alpha=0.3)
    plt.axhline(y=0, color='k', linewidth=0.5)
    plt.axvline(x=0, color='k', linewidth=0.5)
    plt.show()

  except Exception as e:
    print(f"错误：{e}")
    print("请使用x作为变量，例如：'x**2 + 3*x + 2'")


# 使用示例
C = [29.6e-12, 85e-12, 30e-12, 55e-12, 30e-12]
L = [500e-9, 400e-9, 250e-9, 650e-9, 250e-9]
for i in range(len(C)):
  plot_function(f"2*pi*f*{L[i]} - 1/(2*pi*f*{C[i]})")
