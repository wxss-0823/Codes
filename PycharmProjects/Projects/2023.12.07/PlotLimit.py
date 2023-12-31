import numpy as np
import matplotlib.pyplot as plt


x = np.linspace(-100, 100, 1000)
y = np.sin(x) / x
z = np.fft.fft(y, len(y))

# 画出x,y的函数图像
plt.plot(x, y, label=r'$\frac{\sin(x)}{x}$')
plt.axhline(0, color='black', linewidth=0.5)  # 绘制y轴
plt.axvline(0, color='black', linewidth=0.5)  # 绘制x轴
plt.legend()
plt.xlabel('x')
plt.ylabel('y')
plt.title('Graph of $\\lim_{x\\to0} \\frac{\\sin(x)}{x}$')
plt.grid(True)
plt.show()

# 画出z的函数图像
z = np.fft.fftshift(z)
z = np.abs(z)
plt.plot(z, label=r'$z=fft(y)$')
plt.axhline(0, color='black', linewidth=0.5)  # 绘制y轴
plt.axvline(0, color='black', linewidth=0.5)  # 绘制x轴
plt.legend()
plt.xlabel(f'{len(x)}')
plt.ylabel('z')
plt.title('Graph of $\\mathscr{DFT}(y)$')
plt.grid(True)
plt.show()
