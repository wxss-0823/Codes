#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2024/8/8 11:38
# @Author  : wxss
# @File    : GitPush.py
import os
import time


def GetTime() -> str:
    return time.strftime("%y-%m-%d %H:%M:%S", time.localtime())


# 提交信息
author = "wxss"
commit_time = GetTime()
commit_msg = f"\"{author}: {commit_time}\""


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
# 提交信息及文件
print("[CMD_3] " + commit_cmd)
os.system(commit_cmd)
# push 到远程库
print("[CMD_4] " + push_cmd)
os.system(push_cmd)
# 结束信息及退出
print("[End] finish uploading files to remote repository!\n")
print("Wait for 5s to exit...")
time.sleep(5)
