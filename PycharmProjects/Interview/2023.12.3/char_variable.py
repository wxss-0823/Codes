# 字符串中含有变量
# 尝试打印10个数中前n项和
import matplotlib as plt
n = 90
sum_n = 0
for i in range(n):
    sum_n = sum_n + i
    # print("前{}项和为{}".format(i, sum_n))
    print(f"前{i}项和为{sum_n}")
