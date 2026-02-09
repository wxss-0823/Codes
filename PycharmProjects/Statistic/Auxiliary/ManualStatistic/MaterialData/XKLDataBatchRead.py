#!D:\Users\Anaconda\anaconda3\python.exe
# -*- coding: utf-8 -*-
# @Time    : 2026/1/20 18:15
# @Author  : Coffee
# @Project : Auxiliary
# @File    : XKLDataBatchRead.py

import os
import re
from os.path import exists

from ManualStatistic.MaterialData.CapReadXKLFunc import capRead
from ManualStatistic.MaterialData.CapReadXKLFunc import everyCapPlot
import CapReadXKLFunc as Stat

dstDir = r"C:\Users\w00025121\Desktop\data"
figDir = r"C:\Users\w00025121\Desktop\fig"

os.makedirs(dstDir, exist_ok=True)
os.makedirs(figDir, exist_ok=True)

subDirs = next(os.walk(dstDir))[1]
subDirMP = r"\d{8}-\d{3}"

Stat.stabilityXKLTest(dstDir, figDir)






# Plot Every Capacity Figure
# i = 0
# for _ in range(len(subDirs)):
#   if re.search(subDirMP, subDirs[i]) is None:
#     subDirs.remove(subDirs[i])
#   else:
#     i += 1
#
# nLoop = len(subDirs)
# dstDirs = [dstDir + '\\' + subDir for subDir in subDirs]
# figDirs = [figDir + '\\' + subDir for subDir in subDirs]
#
# # 确保目录存在
# for figDir in figDirs:
#   os.makedirs(figDir, exist_ok=True)
#
# for i in range(nLoop):
#   print(f"Reading: {dstDirs[i]}\nWriting: {figDirs[i]}")
#   # capRead(dstDirs[i], figDirs[i])
#   everyCapPlot(dstDirs[i], figDirs[i])
