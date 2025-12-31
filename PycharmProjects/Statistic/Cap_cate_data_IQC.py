#!D:\Users\Anaconda\anaconda3\python.exe
# -*- coding: utf-8 -*-
# @Time    : 2025/12/30 15:18
# @Author  : wxss
# @File    : Cap_cate_data_IQC.py

import os
import re
import shutil
from typing import List

cateDataDir = r"C:\Users\w00025121\Desktop\8-12分类"
capList: List[str] = []

# main
capPattern = r"\d+pF"
for currentDir, subdirs, files in os.walk(cateDataDir):
  for subdir in subdirs:
    # print(subdir)
    try:
      capValue = re.search(capPattern, subdir).group(0)
      capFileDir = os.path.join(currentDir, capValue)
      currFileDir = os.path.join(currentDir, subdir)

      if capValue not in capList:
        capList.append(capValue)
        if not os.path.exists(capFileDir):
          os.mkdir(capFileDir)

      shutil.move(currFileDir, capFileDir)
      print(f"From: {currentDir}\nTo: {capFileDir}")
    except AttributeError as e:
      print(f"The dir \"{subdir}\" doesn't have capacity value.\n")
      continue

  # Clear cap list
  capList.clear()
