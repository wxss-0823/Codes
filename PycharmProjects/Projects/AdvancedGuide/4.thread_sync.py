#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2024/2/2 21:58
# @Author  : wxss
# @File    : 4.thread_sync.py
import threading
import time


class myThread(threading.Thread):
    def __init__(self, threadID, name, delay):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.delay = delay

    def run(self):
        print("开始线程：" + self.name)
        # 获取锁，用于线程同步
        threadLock.acquire()
        print_time(self.name, self.delay, 5)
        print("退出线程：" + self.name)
        # 释放锁，用于下一个线程
        threadLock.release()


threadLock = threading.Lock()


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
