import time
from typing import Callable


# 定义一个基础函数，这个函数可能很复杂，不希望直接改动这个函数，添加功能通过装饰器完成
# 其输入为一个可调用对象，返回一个可调用对象
def deco(
        callfunc: Callable[[], None]
) -> Callable[[], None]:
    print("进入了deco函数")

    def wrapper() -> None:
        print("进入了wrapper函数")
        startTime = time.time()
        callfunc()
        endTime = time.time()
        ms = (endTime - startTime) * 1000
        print("time is %d ms" % ms)

    return wrapper


# 通过@，表示为deco的装饰器函数，执行func()时，会直接将func作为参数传入deco，并执行
@deco
def func() -> None:
    print("进入了func函数")
    print("hello")
    time.sleep(1)
    print("world")


if __name__ == '__main__':
    # 调用func可以不使用参数，此时会直接进入deco
    # 装饰器不需要括号就可以运行
    f = func
    # 此时f为可调用对象
    print(f)
    # 这个括号用于调用wrapper函数
    f()
