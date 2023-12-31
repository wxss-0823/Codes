# 画出数学上的级数
import matplotlib.pyplot as plt
import math


# 阶乘计算函数
def factorial(num):
    for k in range(num):
        if k == 1 or k == 0:
            y = 1
            return y
        else:
            y = k * (k-1)
            if k != 2:
                continue
            else:
                return y


# 通项公式生成函数
def general_term(x):
    y = 3**x / factorial(x)
    return y


# 级数项数&和函数初始化
n = 100
series_sum = 0
series = []
for i in range(n):
    item = general_term(i + 1)
    series_sum = series_sum + item
    series.append(series_sum)

# 画图
fig = plt.figure(num=1, figsize=(8, 6))
plt.plot(series)
plt.show()
