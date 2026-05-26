#!D:\Users\Anaconda\anaconda3\python.exe
# -*- coding: utf-8 -*-
# @Time    : 2026/3/23 9:19
# @Author  : Coffee
# @Project : ReferanceV3.py
# @File    : MaxStep.py


import os

import re
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


coa_dir = r"D:\Users\Wxss\01Project\01VVC\03Data\来料数据"
fig_dir = os.path.join(coa_dir, "最大步进")
os.makedirs(fig_dir, exist_ok=True)
sn_ptn = r"081900\d{2}-00\d{1}"
reMatch1212 = r"kVp"
tarFilePTN = r"\d.*.xlsx"
MesFilePTN = r"上下电|COA"
sub_dir_dict = {}
max_step_dict = {}

dfStep = pd.DataFrame()
current_max = 0
current_idx = 0
max_list = []
up_limit_list = []

for item in next(os.walk(coa_dir))[1]:
  if re.search(sn_ptn, item):
    sn = re.search(sn_ptn, item).group(0)
    origin_value = sub_dir_dict.get(sn)
    if isinstance(origin_value, list):
      origin_value.append(os.path.join(coa_dir, item))
      current_value = origin_value
    else:
      current_value = [os.path.join(coa_dir, item)]
    sub_dir_dict[sn] = current_value

for key in sub_dir_dict:
  for sub_dir in sub_dir_dict[key]:
    for root_dir, sub_dir1, files in os.walk(sub_dir):
      for file in files:
        if (file[:2] == 'C-'
            and re.search(MesFilePTN, file) is None):
          print(f"Load: {key} " + file)
          fileName = os.path.join(root_dir, file)
          xls = pd.ExcelFile(fileName)
          sheetNames = xls.sheet_names
          selectedSheetName = ''

          # Read: 步进采集
          sheetNameList = ['sheet1', 'Sheet1', 'C-curve-info-B193-4-2403090404-', 'C-curve-info-B2432402240101-1-1']
          for i, sheetName in enumerate(sheetNames):
            if sheetName in sheetNameList:
              selectedSheetName = sheetName
              dfStep = pd.read_excel(fileName, sheet_name=selectedSheetName, usecols=[1])
              dfStep["excel_name"] = file.replace(".xlsx", "")
              dfStep = dfStep.drop([0, 1])  # 删除首行
              break

          max_list = np.append(max_list, dfStep.iloc[-1, 0])
          temp_max = np.nanmax(dfStep.iloc[:, 0])
          temp_idx = np.nanargmax(dfStep.iloc[:, 0])
          if temp_max > current_max and isinstance(temp_max, int):

            current_max = temp_max
            current_idx = dfStep.loc[temp_idx, "excel_name"]

  plt.figure(figsize=(5,5), dpi=100, facecolor="w")
  plt.title(key)
  plt.scatter([i + 1 for i in range(len(max_list))], max_list)
  max_avg = np.nanmean(max_list)
  max_std = np.nanstd(max_list)
  up_limit = max_avg + 3 * max_std
  dw_limit = max_avg - 3 * max_std
  plt.axhline(y=up_limit, color='r', linestyle="-", linewidth=2, label=np.int32(up_limit))
  plt.axhline(y=dw_limit, color='r', linestyle="-", linewidth=2)
  plt.savefig(os.path.join(fig_dir, key))
  # plt.show()


  up_limit_list = np.append(up_limit_list, np.ceil(up_limit))
  max_step_dict[key] = (current_max, current_idx)
  current_idx = 0
  current_max = 0
  max_list = []

for key in max_step_dict:
  print(key, max_step_dict[key])

# for limit in up_limit_list:
#   print(limit)
