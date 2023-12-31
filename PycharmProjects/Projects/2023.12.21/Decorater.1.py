from typing import Callable


def deco(
        func: Callable[[], str]
) -> Callable[[], str]:
    print("this is a decorater.")

    def wrapper() -> str:
        txt = func()
        return "test successfully\n" + txt

    return wrapper


@deco
def eg1(

) -> str:
    print("running eg1 now.")
    return "eg1 successfully"


@deco
def eg2(

) -> str:
    print("running eg2 now.")
    return "eg2 successfully"


if __name__ == '__main__':
    # eg1与eg2都使用了装饰器函数，在调用eg1时，deco会执行两次，即使没有调用eg2
    # 输出会打印两次this is a decorater.
    eg = eg1
    print(eg())
    # eg2()
