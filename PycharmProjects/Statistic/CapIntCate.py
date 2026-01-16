#!D:\Users\Anaconda\anaconda3\python.exe
# -*- coding: utf-8 -*-
# @Time    : 2025/12/30 17:33
# @Author  : wxss
# @File    : CapIntCate.py

import os
import re
import shutil
from typing import List

import pandas as pd


def capIntCate(
    sourceDir: str) -> None:
  filePattern = r"Captest\w+\.xlsx"
  capTypeList: List[str] = []
  for currentDir, subdirs, files in os.walk(sourceDir):
    if "pf" not in currentDir:
      for file in files:
        if re.match(filePattern, file):
          capXlsxFile = pd.read_excel(os.path.join(currentDir, file))
          capType = capXlsxFile.iat[0, 0]

          # Remove test's father dir
          fatherDir = re.sub(r"Cap_test\w+", "", currentDir)
          # Remove failed's father dir
          fatherDir = re.sub(r"Fail_", "", fatherDir)
          capTypeDir = os.path.join(fatherDir, str(capType) + "pf")
          fileDir = os.path.join(currentDir)

          # Move file to corresponding directory
          if capType not in capTypeList:
            capTypeList.append(capType)
            try:
              os.mkdir(capTypeDir)
            except FileExistsError:
              pass

          shutil.move(fileDir, capTypeDir)
          print(f"From: {fileDir}\nTo  : {capTypeDir}")

        elif file.endswith(".png"):
          continue
        else:
          print(f"Fail to move directory: {currentDir}")

    capTypeList.clear()


def rmLeakageData(
    sourceDir: str,
    tempDir: str) -> None:
  for currentDir, subdirs, files in os.walk(sourceDir):
    for file in files:
      if file.endswith(".xlsx"):
        excelData = pd.read_excel(os.path.join(currentDir, file))
        if excelData.shape[1] < 6:
          shutil.move(currentDir, tempDir)