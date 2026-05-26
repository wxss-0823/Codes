#!D:\Users\Anaconda\anaconda3\python.exe
# -*- coding: utf-8 -*-
# @Time    : 2025/12/30 15:18
# @Author  : wxss
# @File    : Cap_cate_data_IQC.py

import os
import re
import shutil
from typing import List

cateDataDir = r"D:\Users\Wxss\01Project\01VVC\03Data\自测数据\GL IQC\20260309\真空电容测试数据12.1-3.3-2"
capList: List[str] = []
typeList: List[str] = []

# main
# 用于 IQC 数据分类
capPattern = r"\d+pF"
typePtn = r"081900\d{2}-00[12]"
for currentDir, subDirs, files in os.walk(cateDataDir):
  for subdir in subDirs:
    # print(subdir)
    try:
      capValue = re.search(capPattern, subdir).group(0)
      capFileDir = os.path.join(currentDir, capValue)
      currFileDir = os.path.join(currentDir, subdir)

      if capValue not in capList:
        capList.append(capValue)

      if currentDir.rsplit('\\', 1)[-1] != capValue\
          and currFileDir.rsplit('\\', 1)[-1] != capValue:
        os.makedirs(capFileDir, exist_ok=True)
        shutil.move(currFileDir, capFileDir)
        print(f"From: {currentDir}\nTo: {capFileDir}\n")

    except AttributeError as e:
      # print(f"Info: The dir \"{subdir}\" doesn't have capacity value.\n")

      try:
        typeValue = re.search(typePtn, subdir).group(0)
        typeFileDir = os.path.join(currentDir, typeValue)
        currFileDir = os.path.join(currentDir, subdir)

        if typeValue not in typeList:
          typeList.append(typeValue)

        if currentDir.rsplit('\\', 1)[-1] != typeValue\
            and currFileDir.rsplit('\\', 1)[-1] != typeValue:
          os.makedirs(typeFileDir, exist_ok=True)
          shutil.move(currFileDir, typeFileDir)
          print(f"From: {currentDir}\nTo: {typeFileDir}\n")

      except AttributeError as e:
        print(f"Info: The dir \"{subdir}\" doesn't have type&cap value.\n")

      continue

  # Clear cap list
  capList.clear()
  typeList.clear()