#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2024/2/2 20:41
# @Author  : wxss
# @File    : 3.thread.py
import _thread
import threading
import time


# 使用 _thread 创建线程
def exam__thread():
    def print_time(threadName, delay):
        count = 0
        while count < 5:
            time.sleep(delay)
            count += 1
            print(f"{threadName}: {time.ctime()}")

    try:
        # 多线程运行时，不会等待线程运行结束，直接返回 1，继续执行
        _thread.start_new_thread(print_time, ("Thread-1", 2))
        _thread.start_new_thread(print_time, ("Thread-2", 4))
    except _thread.error as e:
        print("Error: Can't start threads")
        print(e)

    # 确保程序返回 1 后不会直接结束，而是等待线程结束
    while 1:
        pass


def exam_threading():
    class myThread(threading.Thread):
        def __init__(self, threadID, name, delay):
            threading.Thread.__init__(self)
            self.threadID = threadID
            self.name = name
            self.delay = delay

        def run(self):
            print("开始线程：" + self.name)
            print_time(self.name, self.delay, 5)
            print("退出线程：" + self.name)

    def print_time(threadName, delay, counter):
        while counter:
            time.sleep(delay)
            print(f"{threadName}: {time.ctime()}")
            counter -= 1
        return

    # 创建线程
    thread1 = myThread(1, 'Thread-1', 1)
    thread2 = myThread(2, 'Thread-2', 2)

    # 开启线程
    thread1.start()
    thread2.start()
    thread1.join()
    thread2.join()
    print("退出主线程")


if __name__ == '__main__':
    exam_threading()
