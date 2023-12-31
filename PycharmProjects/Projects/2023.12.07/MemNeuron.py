import numpy as np
import matplotlib.pyplot as plt


class MemristorNeuron:
    def __init__(self, input_size):
        self.weights = np.random.randn(input_size)
        self.threshold = 0

    def activate(self, inputs):
        weighted_sum = np.dot(self.weights, inputs)
        output = self.threshold_function(weighted_sum)
        self.update_weights(inputs, output)
        return output

    def threshold_function(self, x):
        if x >= self.threshold:
            return 1
        else:
            return 0

    def update_weights(self, inputs, output):
        self.weights += inputs * (output - self.threshold)


# 创建一个基于忆阻器的神经元对象
neuron = MemristorNeuron(2)

# 创建输入数据
inputs = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])

# 创建输出数据
outputs = np.array([0, 1, 1, 0])

# 创建数组用于保存模拟结果
simulated_outputs = []

# 进行模拟
for i in range(len(inputs)):
    output = neuron.activate(inputs[i])
    simulated_outputs.append(output)

# 绘制模拟结果图表
plt.rcParams['font.sans-serif'] = [u'SimHei']
plt.rcParams['axes.unicode_minus'] = False
plt.plot(outputs, 'bo', label='实际输出')
plt.plot(simulated_outputs, 'r+', label='模拟输出')
plt.xlabel('样本序号')
plt.ylabel('输出值')
plt.title("模拟结果")
plt.legend()
plt.show()
