#!D:\Users\Anaconda\anaconda3\python.exe
# -*- coding: utf-8 -*-
# @Time    : 2026/1/16 14:04
# @Author  : Coffee
# @Project : Auxiliary
# @File    : CapReadXKLFunc.py


import os

import warnings
from tabnanny import check

from numpy.matlib import empty

warnings.filterwarnings('ignore', category=UserWarning, module='openpyxl')

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import re

from select import select


def capRead(
    destDir: str,  # 原始数据地址，要求：子文件夹为分型号的电容数据
    figureDir: str  # 图像存放地址，要求：必须存在该路径
) -> None:
  N = 100  # 100个测试点
  plt.close('all')
  dfs = pd.DataFrame()  # 5次容值采集
  dfCapAll = pd.DataFrame()  # 容值精度
  dfCap = pd.DataFrame()

  for rootDir, subDir, files in os.walk(destDir):
    for file in files:
      if file.endswith(".xlsx") and file[0] != '~':
        # print(file)
        fileName = os.path.join(rootDir, file)
        xls = pd.ExcelFile(fileName)

        # 容值精度采集
        sheetNames = xls.sheet_names
        sheetNameList = ['Sheet1', 'sheet1']
        selectedSheetName = ""
        for i, sheetName in enumerate(sheetNameList):
          if sheetName in sheetNames:
            selectedSheetName = sheetName
          if i == len(sheetNameList):
            raise ValueError("Sheet not found in the Excel file.")

        # Read: 100 行
        df = pd.read_excel(fileName, sheet_name=selectedSheetName, nrows=N)
        df["excel_name"] = file.replace(".xlsx", "")
        df = df.drop(0)  # 删除首行
        dfs = pd.concat([dfs, df])

        # Read: 全部行
        try:
          dfCap = pd.read_excel(fileName, sheet_name=selectedSheetName,
                                usecols=[0, 1, 2, 3, 4, 5, 6])  # 取全部 7 列的数据
        except pd.errors.ParserError:
          print(f"Data format error: {file}")
          continue

        dfCap = dfCap.drop(0)  # 删除首行
        dfCap.columns = ['A', 'B', 'C', 'D', 'E', 'F', 'G']  # 统一列名称
        dfCap = dfCap.astype(
          {'A': float, 'B': float, 'C': float,
           'D': float, 'E': float, 'F': float,
           'G': float})
        dfCap["excel_name"] = file.replace(".xlsx", "")

        # Old version tool: Delete last reverse rows
        # revRowLen = int(-len(dfCap['A']) / 2)
        # lastIndices = dfCap.index[-564:]
        # lastIndices = dfCap.index[revRowLen:]
        # dfCap = dfCap.drop(lastIndices)  # 删除最后反转的行

        dfCapAll = pd.concat([dfCapAll, dfCap])

  capId = dfCapAll[dfCapAll['A'] < 99].index

  dfCapAll.loc[:, 'CWCCW'] = abs(dfCapAll['G'] / dfCapAll['A'])  # CCW  CW 偏差 相对百分比模值
  dfCapAll.loc[:, 'CW'] = abs(dfCapAll['C'] / dfCapAll['A'])  # CCW  CW 偏差 相对百分比模值
  dfCapAll.loc[:, 'CCW'] = abs(dfCapAll['D'] / dfCapAll['A'])  # CCW  CW 偏差 相对百分比模值

  dfCapAll.loc[capId, 'CWCCW'] = abs(dfCapAll['G'].loc[capId])
  dfCapAll.loc[capId, 'CW'] = abs(dfCapAll['C'].loc[capId])
  dfCapAll.loc[capId, 'CCW'] = abs(dfCapAll['D'].loc[capId])

  ####################################################################################################
  # 容值采集数据分析，基础数据存在 df_cap_all 中
  # 容值采集上下限数据
  yLimitUpCap = np.zeros(round(dfCap['A'].size))
  yLimitDwCap = np.zeros(round(dfCap['A'].size))
  for k in range(0, round(dfCap['A'].size)):
    if (dfCap.iloc[k, 0]) < 100:
      yLimitUpCap[k] = 1.5
      yLimitDwCap[k] = -yLimitUpCap[k]
    else:
      yLimitUpCap[k] = dfCap.iloc[k, 0] * 0.015
      yLimitDwCap[k] = -yLimitUpCap[k]

  plt.figure(figsize=(6, 6), dpi=100, facecolor="w")
  plt.title('cap_dev CW&CCW')
  a = 0
  k = -1
  capAllLen = round(dfCapAll['A'].size)
  capLen = round(dfCap['A'].size)
  for i in range(capAllLen):  # 每一个测试文件，数据长度不一样，无法使用定长数据读数
    if dfCapAll.iloc[i, 0] > a:
      a = dfCapAll.iloc[i, 0]
      k = k + 1
    else:
      plt.plot(dfCapAll['A'][(i - k):i], dfCapAll['C'][(i - k):i])  # CW
      plt.plot(dfCapAll['A'][(i - k):i], dfCapAll['D'][(i - k):i])  # CCW
      a = 0
      k = -1
    if i == capAllLen - 1:
      plt.plot(dfCapAll['A'][(i - k):i], dfCapAll['C'][(i - k):i])  # CW
      plt.plot(dfCapAll['A'][(i - k):i], dfCapAll['D'][(i - k):i])  # CCW

  # 画上下限
  plt.plot(dfCap['A'][0:capLen], yLimitUpCap, 'b', linestyle='dashed')
  plt.plot(dfCap['A'][0:capLen], yLimitDwCap, 'b', linestyle='dashed')
  plt.savefig(os.path.join(figureDir, "cap_dev CW&CCW"))
  # plt.show()
  ####################################################################################################

  ####################################################################################################
  # 容值采集数据分析, 画 CWCCW 差值
  allCWCCWAveDev = []
  allCWCCWMaxDev = []
  allCapMaxDev = []

  plt.figure(figsize=(6, 6), dpi=100, facecolor="w")
  plt.title('CW-CCW')
  a = 0
  k = -1
  h = -1
  for i in range(capAllLen):  # 每一个测试文件，数据长度不一样，无法使用定长数据读数
    if dfCapAll.iloc[i, 0] > a:
      a = dfCapAll.iloc[i, 0]
      k = k + 1
      if dfCapAll.iloc[i, 0] > 100:
        h = h + 1
    else:
      plt.plot(dfCapAll['A'][(i - k):i], dfCapAll['G'][(i - k):i])
      allCWCCWAveDev.append(dfCapAll['CWCCW'][(i - h):i].mean())  # 统计 CW CCW 差值平均相对偏差
      allCWCCWMaxDev.append(dfCapAll['CWCCW'][(i - h):i].max())  # 统计 CW CCW 差值最大相对偏差

      CW_max = abs(dfCapAll['CW'][(i - h):i].max())
      CCW_max = abs(dfCapAll['CCW'][(i - h):i].max())
      allCapMaxDev.append(max(CW_max, CCW_max))

      a = 0
      k = -1
      h = -1
    if i == capAllLen - 1:
      plt.plot(dfCapAll['A'][(i - k):i], dfCapAll['G'][(i - k):i])
      allCWCCWAveDev.append(dfCapAll['CWCCW'][(i - h):i].mean())
      allCWCCWMaxDev.append(dfCapAll['CWCCW'][(i - h):i].max())

      CW_max = abs(dfCapAll['CW'][(i - h):i].max())
      CCW_max = abs(dfCapAll['CCW'][(i - h):i].max())
      allCapMaxDev.append(max(CW_max, CCW_max))

  # 画上下限
  plt.plot(dfCap['A'][0:capLen], yLimitUpCap, 'b', linestyle='dashed')
  plt.plot(dfCap['A'][0:capLen], yLimitDwCap, 'b', linestyle='dashed')
  plt.savefig(os.path.join(figureDir, "CW-CCW"))
  # plt.show()

  # 大于 100 pF 时，CW CCW 统计平均偏差
  plt.figure(figsize=(6, 6), dpi=100, facecolor="w")
  plt.title('All_CWCCW_AVG_DEV')
  plt.scatter(range(len(allCWCCWAveDev)), allCWCCWAveDev)
  plt.plot(range(len(allCWCCWAveDev)), np.ones(len(allCWCCWAveDev)) * 0.003, 'r', label='CW-CCW limit')
  plt.legend(loc='best')
  plt.savefig(os.path.join(figureDir, "All_CWCCW_AVG_DEV"))
  # plt.show()

  # 大于 100 pF 时，CW 和 CCW 统计最大偏差
  plt.figure(figsize=(6, 6), dpi=100, facecolor="w")
  plt.title('All_CAP_MAX_DEV')
  plt.scatter(range(len(allCapMaxDev)), allCapMaxDev)
  plt.plot(range(len(allCapMaxDev)), np.ones(len(allCapMaxDev)) * 0.01, 'r', label='CW and CCW limit')
  plt.legend(loc='best')
  plt.savefig(os.path.join(figureDir, "All_CAP_MAX_DEV"))
  # plt.show()
  ####################################################################################################

  # 统计最大偏差超 1% 的电容个数
  failedCapNum = 0
  failedCapNum1 = 0
  for i in range(len(allCapMaxDev)):
    if allCapMaxDev[i] > 0.01:
      failedCapNum += 1
    if allCapMaxDev[i] > 0.015:
      failedCapNum1 += 1

  print(f"The num of max capacity deviation exceeding 1.0%: {failedCapNum} in {len(allCapMaxDev) + 1} samples")
  print(f"The num of max capacity deviation exceeding 1.5%: {failedCapNum1} in {len(allCapMaxDev) + 1} samples")

def checkDeltaCap(
    cap_test_data: pd.DataFrame,
    cap_up_lim: [],
    cap_dw_lim: [],
    figure_dir: str
):
  # 作为容值变化上限的整步数量
  full_step_num = 2
  # 容值变化上限
  # cap_lim = (cap_test_data["A"].iloc[-1] - cap_test_data["A"].iloc[0]) / 2000 * full_step_num
  cap_lim = []
  for i in range(len(cap_test_data["A"])):
    if cap_test_data["A"].iloc[i] <= 100:
      cap_lim.append(cap_test_data["A"].iloc[i + 2] - cap_test_data["A"].iloc[i])
      # cap_lim.append(0.005 * 100)
    else:
      cap_lim.append(0.005 * (cap_test_data["A"].iloc[i] - 100) + cap_test_data["A"].iloc[2] - cap_test_data["A"].iloc[0])
  cw_jump_num = 0
  ccw_jump_num = 0

  jump_point = {"CW": [], "CCW": []}
  for i in range(len(cap_test_data["A"]) - 1):
    delta_cap = cap_test_data["A"].iloc[i + 1] - cap_test_data["A"].iloc[i]
    cap_test_data.loc[i + 1, "delta_CW"] = cap_test_data["C"].iloc[i + 1] - cap_test_data["C"].iloc[i] + delta_cap
    cap_test_data.loc[i + 1, "delta_CCW"] = cap_test_data["D"].iloc[i + 1] - cap_test_data["D"].iloc[i] + delta_cap

  for i in range(len(cap_test_data["delta_CW"])):
    if abs(cap_test_data["delta_CW"].iloc[i]) > cap_lim[i]:
      jump_point["CW"].append(((i, cap_test_data["C"].iloc[i]), (i + 1, cap_test_data["C"].iloc[i + 1])))
      cw_jump_num += 1
    if abs(cap_test_data["delta_CCW"].iloc[i]) > cap_lim[i]:
      jump_point["CCW"].append(((i, cap_test_data["D"].iloc[i]), (i + 1, cap_test_data["D"].iloc[i + 1])))
      ccw_jump_num += 1

  if jump_point["CW"] or jump_point["CCW"]:
    plt.figure(figsize=(6, 6), dpi=300, facecolor="w")
    plt.title(f'Jump Point Curve: {cap_test_data.iloc[0, 7]}')
    plt.plot(cap_test_data['A'], cap_test_data["C"], linewidth=0.5, label=f"CW: {cw_jump_num} points")
    plt.plot(cap_test_data['A'], cap_test_data["D"], linewidth=0.5, label=f"CCW: {ccw_jump_num} points")
    cw_color = "#FF6B6B"
    ccw_color = "#4ECDC4"
    for i in range(len(jump_point["CW"])):
      cw_jump_idx0 = jump_point["CW"][i][0][0] + 1
      cw_jump_idx1 = jump_point["CW"][i][1][0] + 1
      # plt.text(cap_test_data["A"][cw_jump_idx0], jump_point["CW"][i][0][1], f'P{i}-0', fontsize=8, color=cw_color)
      plt.scatter(cap_test_data["A"][cw_jump_idx0], cap_test_data["C"][cw_jump_idx0], s=2, color="red")
      # plt.text(cap_test_data["A"][cw_jump_idx1], jump_point["CW"][i][1][1], f'P{i}-1', fontsize=8, color=cw_color)
      plt.scatter(cap_test_data["A"][cw_jump_idx1], cap_test_data["C"][cw_jump_idx1], s=2, color="red")
    for i in range(len(jump_point["CCW"])):
      cw_jump_idx0 = jump_point["CCW"][i][0][0] + 1
      cw_jump_idx1 = jump_point["CCW"][i][1][0] + 1
      # plt.text(cap_test_data["A"][cw_jump_idx0], jump_point["CCW"][i][0][1], f'P{i}-0', fontsize=8, color=ccw_color)
      plt.scatter(cap_test_data["A"][cw_jump_idx0], cap_test_data["D"][cw_jump_idx0], s=2, color="red")
      # plt.text(cap_test_data["A"][cw_jump_idx1], jump_point["CCW"][i][1][1], f'P{i}-1', fontsize=8, color=ccw_color)
      plt.scatter(cap_test_data["A"][cw_jump_idx1], cap_test_data["D"][cw_jump_idx1], s=2, color="red")

    plt.plot(cap_test_data['A'], cap_up_lim, 'b', linestyle='dashed')
    plt.plot(cap_test_data['A'], cap_dw_lim, 'b', linestyle='dashed')
    plt.legend(loc='best')
    plt.savefig(os.path.join(figure_dir, f"JumpPointCurve_{cap_test_data.iloc[0, 7]}.png"))
    plt.close()
    # plt.show()

def everyCapPlot(
    destDir: str,  # 原始数据地址，要求：子文件夹为分型号的电容数据
    figureDir: str  # 图像存放地址，要求：必须存在该路径
) -> None:
  plt.close('all')
  dfCapAll = pd.DataFrame()  # 容值精度
  dfCap = pd.DataFrame()
  SN: str = ''

  for rootDir, subDir, files in os.walk(destDir):
    matchesSN = [r'0819\d{4}-\d{3}_\d{7}', r'0819\d{4}-\d{3}_GL\d{12}']
    for file in files:
      if file.endswith(".xlsx") and file[0] != '~':
        # 匹配电容型号信息
        try:
          for pattern in matchesSN:
            if re.search(pattern, file):
              SN = re.search(pattern, file).group(0)
        except AttributeError:
          print('There is no SN matching result for pattern.')

        # print(file)
        fileName = os.path.join(rootDir, file)
        xls = pd.ExcelFile(fileName)

        # 容值精度采集
        sheetNames = xls.sheet_names
        sheetNameList = ['Sheet1', 'sheet1']
        selectedSheetName = ""
        for i, sheetName in enumerate(sheetNameList):
          if sheetName in sheetNames:
            selectedSheetName = sheetName
          if i == len(sheetNameList):
            raise ValueError("Sheet not found in the Excel file.")

        # Read: 全部行
        dfCap = pd.read_excel(fileName, sheet_name=selectedSheetName,
                              usecols=[0, 1, 2, 3, 4, 5, 6])  # 取全部 7 列的数据\
        dfCap = dfCap.drop(0)  # 删除首行
        dfCap.columns = ['A', 'B', 'C', 'D', 'E', 'F', 'G']  # 统一列名称
        dfCap = dfCap.astype(
          {'A': float, 'B': float, 'C': float,
           'D': float, 'E': float, 'F': float,
           'G': float})
        dfCap['SN'] = SN  # 将 SN 数据写入表格

        # Old version tool: Delete last reverse rows
        # revRowLen = int(-len(dfCap['A']) / 2)
        # lastIndices = dfCap.index[revRowLen:]
        # dfCap = dfCap.drop(lastIndices)  # 删除最后反转的行

        dfCapAll = pd.concat([dfCapAll, dfCap])

  capId = dfCapAll[dfCapAll['A'] < 99].index

  dfCapAll.loc[:, 'CWCCW'] = abs(dfCapAll['G'] / dfCapAll['A'])  # CCW  CW 偏差 相对百分比模值
  dfCapAll.loc[capId, 'CWCCW'] = abs(dfCapAll['G'].loc[capId])
  dfCapAll = dfCapAll.dropna(subset=['SN'])  # 删除 SN 中的空行

  # 容值上下限范围
  yLimitUpCap = np.zeros(round(dfCap['A'].size))
  yLimitDwCap = np.zeros(round(dfCap['A'].size))
  for k in range(0, round(dfCap['A'].size)):
    if (dfCap.iloc[k, 0]) < 100:
      yLimitUpCap[k] = 1
      yLimitDwCap[k] = -yLimitUpCap[k]
    else:
      yLimitUpCap[k] = dfCap.iloc[k, 0] * 0.01
      yLimitDwCap[k] = -yLimitUpCap[k]

  capAllLen = round(dfCapAll['A'].size)
  capLen = round(dfCap['A'].size)

  # 容值采集数据分析, 画 CWCCW 差值
  a = 0
  k = 0
  h = -1
  for i in range(capAllLen):  # 每一个测试文件，数据长度不一样，无法使用定长数据读数
    if dfCapAll.iloc[i, 0] > a:
      a = dfCapAll.iloc[i, 0]
      k = k + 1
      if dfCapAll.iloc[i, 0] > 100:
        h = h + 1
    else:
      # plt.figure(figsize=(6, 6), dpi=100, facecolor="w")
      # plt.title('CW-CCW')
      # plt.plot(dfCapAll['A'][(i - k):i], dfCapAll['G'][(i - k):i], label=f"SN{dfCapAll.iloc[i-k, 7]}")
      # plt.legend(loc='best')
      #
      # # 画上下限
      # plt.plot(dfCap['A'][0:capLen], yLimitUpCap, 'b', linestyle='dashed')
      # plt.plot(dfCap['A'][0:capLen], yLimitDwCap, 'b', linestyle='dashed')
      # plt.savefig(os.path.join(figureDir, f"CW-CCW{dfCapAll.iloc[i-k, 7]}"))

      # 检查容值步进变化量
      if i == k:
        checkDeltaCap(dfCapAll.iloc[(i - k):i], yLimitUpCap, yLimitDwCap, figureDir)
      else:
        checkDeltaCap(dfCapAll.iloc[(i - k - 1):i], yLimitUpCap, yLimitDwCap, figureDir)

      a = 0
      k = 0
      h = -1
    # if i == capAllLen - 1:
    #   # plt.figure(figsize=(6, 6), dpi=100, facecolor="w")
    #   # plt.title('CW-CCW')
    #   # plt.plot(dfCapAll['A'][(i - k):i], dfCapAll['G'][(i - k):i], label=f"SN{dfCapAll.iloc[i-k, 7]}")
    #   # plt.legend(loc='best')
    #   #
    #   # # 画上下限
    #   # plt.plot(dfCap['A'][0:capLen], yLimitUpCap, 'b', linestyle='dashed')
    #   # plt.plot(dfCap['A'][0:capLen], yLimitDwCap, 'b', linestyle='dashed')
    #   # plt.savefig(os.path.join(figureDir, f"CW-CCW{dfCapAll.iloc[i-k, 7]}"))
    #   checkDeltaCap(dfCapAll.iloc[(i - k):i], yLimitUpCap, yLimitDwCap)


def stabilityXKLTest(
    destDir: str,  # 原始数据地址，要求：子文件夹为分型号的电容数据
    figureDir: str  # 图像存放地址，要求：必须存在该路径
) -> None:
  dfCapAll = pd.DataFrame()  # 容值精度
  dfCap = pd.DataFrame()
  dev_CWCCW = pd.DataFrame()
  j = 0
  all_times = 0
  times_pattern = r"(\d+)次"

  for rootDir, subDir, files in os.walk(destDir):
    for file in files:
      if file.endswith(".xlsx") and file[0] != '~':
        times_list = re.findall(times_pattern, file)
        for times in times_list:
          all_times += int(times)
        print(f"Load: {file}")
        fileName = os.path.join(rootDir, file)

        # Read: 全部行
        dfCap = pd.read_excel(fileName, sheet_name='Sheet1', usecols=[0, 1, 2, 3, 4, 5, 6])  # 取全部 7 列的数据
        dfCap.columns = ['A', 'B', 'C', 'D', 'E', 'F', 'G']  # 统一列名称
        dev_CWCCW.loc[j, 'Times'] = all_times
        dev_CWCCW.loc[j, 'CW Mean Dev'] = dfCap['C'].mean()
        dev_CWCCW.loc[j, 'CCW Mean Dev'] = dfCap['D'].mean()
        CW_max_idx = abs(dfCap['C'] / dfCap['A']).idxmax()
        dev_CWCCW.loc[j, 'CW Max Dev'] = dfCap['C'][CW_max_idx] / dfCap['A'][CW_max_idx]
        CCW_max_idx = abs(dfCap['D'] / dfCap['A']).idxmax()
        dev_CWCCW.loc[j, 'CCW Max Dev'] = dfCap['D'][CCW_max_idx] / dfCap['A'][CCW_max_idx]

        # dfCap = dfCap.drop(0) # 删除首行
        dfCapAll = pd.concat([dfCapAll, dfCap])

      j += 1
      all_times = 0

  # 容值采集数据分析，基础数据存在 df_cap_all 中
  plt.figure(figsize=(6, 6), dpi=100, facecolor="w")
  plt.title('cap_dev CW&CCW')
  a = 0
  k = 0
  capAllLen = round(dfCapAll['A'].size)
  capLen = round(dfCap['A'].size)


  for i in range(capAllLen):  # 每一个测试文件，数据长度不一样，无法使用定长数据读数
    if dfCapAll.iloc[i, 0] > a:
      a = dfCapAll.iloc[i, 0]
      k = k + 1
    else:
      plt.plot(dfCapAll['A'][(i - k):i], dfCapAll['C'][(i - k):i])  # CW
      plt.plot(dfCapAll['A'][(i - k):i], dfCapAll['D'][(i - k):i])  # CCW
      a = 0
      k = 0
    if i == capAllLen - 1:
      plt.plot(dfCapAll['A'][(i - k):i], dfCapAll['C'][(i - k):i])  # CW
      plt.plot(dfCapAll['A'][(i - k):i], dfCapAll['D'][(i - k):i])  # CCW

  # 画上下限
  plt.plot(dfCap['A'][0:capLen], dfCap['E'][0:capLen], 'b', linestyle='dashed')
  plt.plot(dfCap['A'][0:capLen], dfCap['F'][0:capLen], 'b', linestyle='dashed')
  plt.savefig(os.path.join(figureDir, "cap_dev CW&CCW"))
  # plt.show()

  # Plot CW-CCW
  plt.figure(figsize=(6, 6), dpi=100, facecolor="w")
  plt.title('CW-CCW')
  for i in range(capAllLen):  # 每一个测试文件，数据长度不一样，无法使用定长数据读数
    if dfCapAll.iloc[i, 0] > a:
      a = dfCapAll.iloc[i, 0]
      k = k + 1
    else:
      plt.plot(dfCapAll['A'][(i - k):i], dfCapAll['G'][(i - k):i])  # CW-CCW
      a = 0
      k = 0
    if i == capAllLen - 1:
      plt.plot(dfCapAll['A'][(i - k):i], dfCapAll['G'][(i - k):i])  # CW-CCW

  # 画上下限
  plt.plot(dfCap['A'][0:capLen], dfCap['E'][0:capLen], 'b', linestyle='dashed')
  plt.plot(dfCap['A'][0:capLen], dfCap['F'][0:capLen], 'b', linestyle='dashed')
  plt.savefig(os.path.join(figureDir, "CW-CCW"))
  # plt.show()

  # Plot CW&CCW statistic deviation
  plt.figure(figsize=(8, 8), dpi=100, facecolor="w")
  plt.subplot(2, 1, 1)
  plt.title('CW&CCW Mean Dev')
  plt.scatter(dev_CWCCW['Times'], dev_CWCCW['CW Mean Dev'], label='CW')
  plt.scatter(dev_CWCCW['Times'], dev_CWCCW['CCW Mean Dev'], label='CCW')
  plt.legend(loc="best")
  plt.subplot(2, 1, 2)
  plt.title('CW&CCW Max Dev')
  plt.scatter(dev_CWCCW['Times'], dev_CWCCW['CW Max Dev'], label='CW')
  plt.scatter(dev_CWCCW['Times'], dev_CWCCW['CCW Max Dev'], label='CCW')
  plt.legend(loc="best")
  plt.savefig(os.path.join(figureDir, "CW&CCW Stat Dev"))
  # plt.show()


def stabilityGLTest(
    destDir: str,  # 原始数据地址，要求：子文件夹为分型号的电容数据
    figureDir: str  # 图像存放地址，要求：必须存在该路径
) -> None:
  dfCWCCW = pd.DataFrame()  # 容值精度
  dev_CWCCW = pd.DataFrame()
  all_times = 220
  delta_times = 5
  N = int(all_times / delta_times + 1)
  j = 0

  for rootDir, subDir, files in os.walk(destDir):
    for file in files:
      if file.endswith(".xlsx") and file[0] != '~':
        print(f"Load: {file}")
        fileName = os.path.join(rootDir, file)

        # Read: 全部行
        dfCap = pd.read_excel(fileName, sheet_name='图对比')  # 取全部 7 列的数据

        times_array = np.array([i*delta_times for i in range(N)])

        # Plot Capacity Deviation CCW&CW
        plt.figure(figsize=(6, 6), dpi=100, facecolor="w")
        plt.title('cap-dev CW&CCW')
        for times in times_array:
          plt.plot(dfCap["Cap"], dfCap[f"CW标准差{times}W"])
          plt.plot(dfCap["Cap"], dfCap[f"CCW标准差{times}W"])
          dfCWCCW[f"CW-CCW{times}W"] = dfCap[f"CW标准差{times}W"] - dfCap[f"CCW标准差{times}W"]
          dev_CWCCW.loc[j, 'Times'] = times*10000
          dev_CWCCW.loc[j, 'CW Mean Dev'] = dfCap[f"CW标准差{times}W"].mean()
          dev_CWCCW.loc[j, 'CCW Mean Dev'] = dfCap[f"CCW标准差{times}W"].mean()
          CW_max_idx = abs(dfCap[f"CW标准差{times}W"]/dfCap["Cap"]).idxmax()
          dev_CWCCW.loc[j, 'CW Max Dev'] = dfCap[f"CW标准差{times}W"][CW_max_idx] / dfCap["Cap"][CW_max_idx]
          CCW_max_idx = abs(dfCap[f"CCW标准差{times}W"]/dfCap["Cap"]).idxmax()
          dev_CWCCW.loc[j, 'CCW Max Dev'] = dfCap[f"CCW标准差{times}W"][CCW_max_idx] / dfCap["Cap"][CCW_max_idx]
          j += 1

        plt.plot(dfCap["Cap"], dfCap["正限值（1%）"], 'b', linestyle='dashed')
        plt.plot(dfCap["Cap"], dfCap["负限值（1%）"], 'b', linestyle='dashed')
        plt.savefig(os.path.join(figureDir, "cap_dev CW&CCW"))
        # plt.show()

        # Plot CW-CCW deviation
        plt.figure(figsize=(6, 6), dpi=100, facecolor="w")
        plt.title('CW-CCW')
        for times in times_array:
          plt.plot(dfCap["Cap"], dfCWCCW[f"CW-CCW{times}W"])

        plt.plot(dfCap["Cap"], dfCap["正限值（1%）"], 'b', linestyle='dashed')
        plt.plot(dfCap["Cap"], dfCap["负限值（1%）"], 'b', linestyle='dashed')
        plt.savefig(os.path.join(figureDir, "CW-CCW"))
        # plt.show()

        # Plot statistic deviation
        plt.figure(figsize=(8, 8), dpi=100, facecolor="w")
        plt.subplot(2, 1, 1)
        plt.title('CW&CCW Mean Dev')
        plt.scatter(dev_CWCCW['Times'], dev_CWCCW['CW Mean Dev'], label='CW')
        plt.scatter(dev_CWCCW['Times'], dev_CWCCW['CCW Mean Dev'], label='CCW')
        plt.legend(loc="best")
        plt.subplot(2, 1, 2)
        plt.title('CW&CCW Max Dev')
        plt.scatter(dev_CWCCW['Times'], dev_CWCCW['CW Max Dev'], label='CW')
        plt.scatter(dev_CWCCW['Times'], dev_CWCCW['CCW Max Dev'], label='CCW')
        plt.legend(loc="best")
        plt.savefig(os.path.join(figureDir, "CW&CCW Stat Dev"))
        # plt.show()
