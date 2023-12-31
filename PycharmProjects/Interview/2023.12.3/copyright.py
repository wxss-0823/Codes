import matplotlib.pyplot as plt
import numpy as np

# 水印
C = ""
shuiyin = [112, 114, 105, 110, 116, 40, 39, 20316, 32773, 65306, 29579, 38177, 32988, 33308, 39, 41]
for i in range(0, 16):
    C = C + chr(shuiyin[i])
eval(C)

# 画图格式
plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来指定默认字体 SimHei为黑体
plt.rcParams['axes.unicode_minus'] = False

# 画图函数
x = np.linspace(-1, 1, 50)  # 从(-1,1)均匀取50个点
y = 2 * x

# 坐标设置
plt.plot(x, y)
# 水印
A = [20316, 32773, 58, 119, 120, 115, 115]
B = ""
for i in range(0, 7):
    B = B + chr(A[i])
plt.title(B)
plt.show()
