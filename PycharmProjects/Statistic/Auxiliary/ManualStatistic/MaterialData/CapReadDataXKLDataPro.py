#!D:\Users\Anaconda\anaconda3\python.exe
# -*- coding: utf-8 -*-
# @Time    : 2026/1/16 14:04
# @Author  : Coffee
# @Project : Auxiliary
# @File    : CapReadDataXKLDataPro.py


import os

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


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
      if file.endswith(".xlsx"):
        print(file)
        fileName = os.path.join(rootDir, file)
        xls = pd.ExcelFile(fileName)

        # 容值精度采集
        sheetNames = xls.sheet_names
        if 'Sheet1' in sheetNames:
          selectedSheetName = 'Sheet1'
        else:
          raise ValueError("Date not found in the Excel file.")

        # Read: 100 行
        df = pd.read_excel(fileName, sheet_name=selectedSheetName, nrows=N)
        df["excel_name"] = file.replace(".xlsx", "")
        dfs = pd.concat([dfs, df])

        # Read: 全部行
        dfCap = pd.read_excel(fileName, sheet_name=selectedSheetName,
                              usecols=[0, 1, 2, 3, 4, 5, 6])  # 取全部 7 列的数据
        dfCap.columns = ['A', 'B', 'C', 'D', 'E', 'F', 'G']  # 统一列名称
        dfCap["excel_name"] = file.replace(".xlsx", "")
        # df_cap = df_cap.drop(0) # 删除首行
        revRowLen = int(-len(dfCap['A']) / 2)
        # lastIndices = dfCap.index[-564:]
        lastIndices = dfCap.index[revRowLen:]
        dfCap = dfCap.drop(lastIndices)  # 删除最后反转的行
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
      yLimitUpCap[k] = 1
      yLimitDwCap[k] = -yLimitUpCap[k]
    else:
      yLimitUpCap[k] = dfCap.iloc[k, 0] * 0.01
      yLimitDwCap[k] = -yLimitUpCap[k]

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
  plt.plot(dfCap['A'][0:capLen], yLimitUpCap, 'b', linestyle='dashed')
  plt.plot(dfCap['A'][0:capLen], yLimitDwCap, 'b', linestyle='dashed')
  plt.savefig(os.path.join(figureDir, "cap_dev CW&CCW"))
  ####################################################################################################

  ####################################################################################################
  # 容值采集数据分析, 画 CWCCW 差值
  allCWCCWAveDev = []
  allCWCCWMaxDev = []
  allCapMaxDev = []

  plt.figure(figsize=(6, 6), dpi=100, facecolor="w")
  plt.title('CW-CCW')
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
      plt.plot(dfCapAll['A'][(i - k):i], dfCapAll['G'][(i - k):i])
      allCWCCWAveDev.append(dfCapAll['CWCCW'][(i - h):i].mean())  # 统计 CW CCW 差值平均相对偏差
      allCWCCWMaxDev.append(dfCapAll['CWCCW'][(i - h):i].max())  # 统计 CW CCW 差值最大相对偏差

      CW_max = abs(dfCapAll['CW'][(i - h):i].max())
      CCW_max = abs(dfCapAll['CCW'][(i - h):i].max())
      allCapMaxDev.append(max(CW_max, CCW_max))

      a = 0
      k = 0
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

  # 大于 100 pF 时，CW CCW 统计平均偏差
  plt.figure(figsize=(6, 6), dpi=100, facecolor="w")
  plt.title('All_CWCCW_AV_DEV')
  plt.scatter(range(len(allCWCCWAveDev)), allCWCCWAveDev)
  plt.plot(range(len(allCWCCWAveDev)), np.ones(len(allCWCCWAveDev)) * 0.003, 'r', label='CW-CCW limit')
  plt.legend(loc='best')
  plt.savefig(os.path.join(figureDir, "All_CWCCW_AV_DEV"))

  # 大于 100 pF 时，CW 和 CCW 统计最大偏差
  plt.figure(figsize=(6, 6), dpi=100, facecolor="w")
  plt.title('All_CAP_MAX_DEV')
  plt.scatter(range(len(allCapMaxDev)), allCapMaxDev)
  plt.plot(range(len(allCapMaxDev)), np.ones(len(allCapMaxDev)) * 0.01, 'r', label='CW and CCW limit')
  plt.legend(loc='best')
  plt.savefig(os.path.join(figureDir, "All_CAP_MAX_DEV"))
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
