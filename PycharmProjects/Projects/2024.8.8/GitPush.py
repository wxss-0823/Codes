#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2024/8/8 11:38
# @Author  : wxss
# @File    : GitPush.py
import os
import time


def GetTime() -> str:
    return time.strftime("%a %b %d %H:%M:%S %Y", time.localtime())


# 提交信息
author = "wxss"
update_msg = input("Please input the update message: ")
if update_msg == "exit" or "q" or "quit":
    os.system("exit\n")
commit_time = GetTime()
commit_msg = f"\"{author}: {update_msg} On {commit_time}\""


# 命令集
check_cmd = "git status"
storage_cmd = "git add --all"
commit_cmd = "git commit -m " + commit_msg
push_cmd = "git push -u origin master"

# 终端信息及执行
print("[Begin] Execute git automatic upload...")
# 查询 git 状态
print("[CMD_1] " + check_cmd)
os.system(check_cmd)
# 存储文件
print("[CMD_2] " + storage_cmd)
os.system(storage_cmd)

def switch(case) -> int :
    if case == "q" or "exit" or "quit" :
        print("Wait for 5s to exit...")
        time.sleep(5)
        return 0
    elif case == "r" :
        return 2
    else :
        switch(input("Please input correct command: "))

def input_exit() -> None :
    if input("Please input q/quit/exit to exit: ") == "q" or "quit" or "exit" :
        os.system("exit\n")
    else :
        input_exit()

while True :
    try :
        # 提交信息及文件
        print("[CMD_3] " + commit_cmd)
        os.system(commit_cmd)
        # push 到远程库
        print("[CMD_4] " + push_cmd)
        if not os.system(push_cmd) :
            # 结束信息及退出
            print("[End] finish uploading files to remote repository!\n")
            input_exit()
            break
        else :
            raise Exception("Git failed!")
    except Exception as e :
        if switch(input("Please input q/quit/exit to exit, or input r to retry: ")) == 0 :
            print(f"[End] {e}")
            break
        else :
            pass