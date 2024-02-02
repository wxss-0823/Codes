import sys


# 创建一个迭代器类
class MyNumbers:
    def __iter__(self):
        self.number = 1
        return self

    def __next__(self):
        if self.number <= 20:
            x = self.number
            self.number += 1
            return x
        else:
            raise StopIteration


# 创建类的实例
my_class = MyNumbers()
# 创建迭代器
my_iter = iter(my_class)

# 调用 next 函数
for item in my_iter:
    print(item)


# 创建生成器
def fibonacci(n):   # 生成 n 位的斐波那契数列
    a, b, counter = 0, 1, 0
    while True:
        if counter > n:
            return
        yield a
        a, b = b, a + b
        counter += 1


f = fibonacci(10)   # f 是一个迭代器，由生成器返回生成

while True:
    try:
        print(next(f))
    except StopIteration:
        sys.exit()
