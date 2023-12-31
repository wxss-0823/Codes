import numpy as np
import matplotlib.pyplot as plt


# 定义级数和函数
def series_sum(x, n):
    return np.sum([x ** i for i in range(n + 1)], axis=0)


# 生成 x 值的数组
x = np.linspace(-10, 10, 1000)

# 绘制不同级数下的函数曲线
n_values = [1, 2, 3, 4, 10]  # 可根据需要修改级数的值
for n in n_values:
    y = series_sum(x, n)
    plt.plot(x, y, label=f"Sum of $x^{{{n}}}$")

# 设置图例、设置 x 和 y 轴的标签、设置图形的标题、显示网格
plt.legend()
plt.xlabel('x')
plt.ylabel('y')
plt.title('Sum of Series $x^n$')
plt.grid(True)
plt.show()
