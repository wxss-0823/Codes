#!D:\Users\Anaconda\anaconda3\python.exe
# -*- coding: utf-8 -*-
# @Time    : 2026/1/12 11:06
# @Author  : Coffee
# @Project : Auxiliary
# @File    : CalcTuningF.py


import os

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

N = 100  # 100个测试点
dataDir = r'D:\Users\Wxss\00工作\0_实习期\1_实践\0_电容项目\1_电容测试数据\来料数据\2026-1-8马达发货初始数据\08190049-001容值精度C曲线1.6'

plt.close('all')
dfs = pd.DataFrame()  # 5次容值采集
dfCapAll = pd.DataFrame()  # 容值精度
dfStepAll = pd.DataFrame()  # 步进

# 读取 Excel 原始数据
df = pd.DataFrame()
dfCap = pd.DataFrame()
dfStep = pd.DataFrame()
for rootDir, subDir, files in os.walk(dataDir):
  for file in files:
    if file.endswith(".xlsx") and file[0] != 'C':
      print("Load: " + file)
      fileName = os.path.join(rootDir, file)
      xls = pd.ExcelFile(fileName)
      sheetNames = xls.sheet_names
      selectedSheetName = ''

      # Read: 5次容值采集
      sheetNameList = ['5次马拉松容值采集', '5次容值采点', '5次容值采集']
      for i, sheetName in enumerate(sheetNames):
        if sheetName in sheetNameList:
          selectedSheetName = sheetName
          break
        if i == len(sheetNames) - 1:
          raise ValueError("Data not found in the Excel file.")
      df = pd.read_excel(fileName, sheet_name=selectedSheetName, usecols=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12], nrows=N)
      df["excel_name"] = file.replace(".xlsx", "")
      dfs = pd.concat([dfs, df])

      # Read: 容值精度采集
      sheetNameList = ['容值精度采集', '容值精度采集 (2)', '容值CCWCW采集', '容值CCWCW采集1', '容值测试']
      for i, sheetName in enumerate(sheetNames):
        if sheetName in sheetNameList:
          selectedSheetName = sheetName
          break
        if i == len(sheetNames) - 1:
          raise ValueError("Data not found in the Excel file.")
      dfCap = pd.read_excel(fileName, sheet_name=selectedSheetName, usecols=[0, 1, 2])  # 不同文件，列名称不同，取前三列
      dfCap.columns = ['A', 'B', 'C']  # 统一列名称
      dfCap["excel_name"] = file.replace(".xlsx", "")
      dfCap = dfCap.drop(0)  # 删除首行
      lastTwoIndices = dfCap.index[-2:]
      dfCap = dfCap.drop(lastTwoIndices)  # 删除最后两行
      dfCapAll = pd.concat([dfCapAll, dfCap])

      # Read: 步进采集
      sheetNameList = ['步进CCWCW采集', '步进精度采集', '步进精度采集1', '步进测试']
      for i, sheetName in enumerate(sheetNames):
        if sheetName in sheetNameList:
          selectedSheetName = sheetName
          break
        if i == len(sheetNames) - 1:
          raise ValueError("Data not found in the Excel file.")
      dfStep = pd.read_excel(fileName, sheet_name=selectedSheetName, usecols=[0, 1, 2])
      dfStep.columns = ['A', 'B', 'C']
      dfStep['CW(pF)'] = np.nan  # 正转步进差
      dfStep['CCW(pF)'] = np.nan  # 反转步进差
      dfStep["excel_name"] = file.replace(".xlsx", "")
      dfStep = dfStep.drop(0)  # 删除首行
      dfStep.loc[:, 'B'] = dfStep['B'] / 10
      dfStep.loc[:, 'C'] = dfStep['C'] / 10

      # Calc: 正转/反转下，每一次步进，电容的变化量
      for i in range(1, dfStep.index[-1]):
        dfStep.loc[i, 'CW(pF)'] = dfStep.loc[i + 1, 'B'] - dfStep.loc[i, 'B']
        dfStep.loc[i, 'CCW(pF)'] = dfStep.loc[i + 1, 'C'] - dfStep.loc[i, 'C']
      lastOneIndices = dfStep.index[-1:]
      dfStep = dfStep.drop(lastOneIndices)  # 删除最后一行
      dfStepAll = pd.concat([dfStepAll, dfStep])
      dfStepAll = dfStepAll.dropna(subset=['A'])  # 步进测试存在NAN，删除A列中，包含NAN的行

# Calc: Full-step 为每一步进后的理论容值，差值为测试值和理论值的差异
for i in range(5):
  dfsCWCol = f'CW{i + 1}(pF)'
  dfsCCWCol = f'CCW{i + 1}(pF)'
  dfs.loc[:, dfsCWCol] = dfs[dfsCWCol] - dfs['Full-step']
  dfs.loc[:, dfsCCWCol] = dfs[dfsCCWCol] - dfs['Full-step']

dfs.loc[:, 'CW5K(pF)'] = dfs['CW5K(pF)'] - dfs['Full-step']
dfs.loc[:, 'CCW5K(pF)'] = dfs['CCW5K(pF)'] - dfs['Full-step']

# Calc: 容值测量绝对误差
dfCapAll.loc[:, 'B'] = dfCapAll['B'] - dfCapAll['A']  # CW 测试值与理论值偏差
dfCapAll.loc[:, 'C'] = dfCapAll['C'] - dfCapAll['A']  # CCW 测试值与理论值偏差
dfCapAll.loc[:, 'CWCCW(pF)'] = dfCapAll['B'] - dfCapAll['C']  # CW-CCW 的偏差，正反转容值的绝对偏差

# Calc: 容值测量相对偏差，CW 相对误差；CCW 相对误差；CW-CCW 相对误差
dfCapAll.loc[:, 'CWCCW'] = abs(dfCapAll['CWCCW(pF)'] / dfCapAll['A'])  # CCW-CW 的相对百分比偏差
dfCapAll.loc[:, 'CW'] = abs(dfCapAll['B'] / dfCapAll['A'])  # CW 的相对百分比偏差
dfCapAll.loc[:, 'CCW'] = abs(dfCapAll['C'] / dfCapAll['A'])  # CCW 的相对百分比偏差

# Set: 前 100 个数取模
capId = dfCapAll[dfCapAll['A'] < 99].index
dfCapAll.loc[capId, 'CWCCW'] = abs(dfCapAll.loc[capId, 'CWCCW(pF)'])
dfCapAll.loc[capId, 'CW'] = abs(dfCapAll.loc[capId, 'B'])
dfCapAll.loc[capId, 'CCW'] = abs(dfCapAll.loc[capId, 'C'])

##################################################################################################################
# Calc: “5 次重复测试” 数据分析，基础数据存在 dfs 中
# 最大偏差统计，存在 ALL_5TIMES_AV_DEV 里面，第一列为CW(5次测试中，100个点最大值-最下值  的平均值)，第二列为CCW,
ALL_5TIMES_AV_DEV = []
rowNum = N * int(dfs['Full-step'].size / df['Full-step'].size)
dev5 = pd.DataFrame(index=range(rowNum), columns=range(2))
g = 1
for k in range(rowNum):
  dev5.iloc[k, 0] = max(dfs.iloc[k, 1], dfs.iloc[k, 3], dfs.iloc[k, 5], dfs.iloc[k, 7], dfs.iloc[k, 9]) - min(
    dfs.iloc[k, 1], dfs.iloc[k, 3], dfs.iloc[k, 5], dfs.iloc[k, 7], dfs.iloc[k, 9])  # CW 5次测试值中最大值 - 最下值
  dev5.iloc[k, 1] = max(dfs.iloc[k, 2], dfs.iloc[k, 4], dfs.iloc[k, 6], dfs.iloc[k, 8], dfs.iloc[k, 10]) - min(
    dfs.iloc[k, 2], dfs.iloc[k, 4], dfs.iloc[k, 6], dfs.iloc[k, 8], dfs.iloc[k, 10])  # CCW 5次测试值中最大值 - 最下值
  if k % 99 == 0 and k != 0:
    devAvgCWCCW = dev5.loc[(g - 1) * N:(g * N - 1), [0, 1]].mean()  # 单个样品，CW 平均最大偏差和 CCW 平均最大偏差
    devAvgMax = max(devAvgCWCCW[0], devAvgCWCCW[1])
    g = g + 1
    ALL_5TIMES_AV_DEV.append(devAvgMax)  # 所有样品平均最大偏差统计数据存在 ALL_5TIMES_AV_DEV

# 5 次平均一致性 统计数据画图
CWRowNum = dfStep['CW(pF)'].size
all5TimeLen = len(ALL_5TIMES_AV_DEV)
twoStepValue = dfStep.loc[(round(1 / 4 * CWRowNum)):(round(3 / 4 * CWRowNum)), 'CW(pF)'].mean()  # 最后一个样品，步进数据 1/4 - 3/4 线性区域的平均值
plt.figure(figsize=(6, 6), dpi=100, facecolor="w")
plt.title('ALL_5TIMES_AV_DEV')
plt.scatter(range(all5TimeLen), ALL_5TIMES_AV_DEV)
plt.plot(range(all5TimeLen), np.ones(all5TimeLen) * twoStepValue, 'r', label='two steps limit')
plt.legend(loc="best")
plt.show()

# 定义上下限：小于 100 pF，1；大于 100 pF，1 + 0.01*C
yLimitUp = np.zeros(N)
yLimitDw = np.zeros(N)
for k in range(0, N):
  if (df.iloc[k, 1]) < 100:
    yLimitUp[k] = 1
    yLimitDw[k] = -yLimitUp[k]
  else:
    yLimitUp[k] = df.iloc[k, 1] * 0.01
    yLimitDw[k] = -yLimitUp[k]

# Plot: 画每一个电容 5 次重复测试的图像
for i in range(round(dfs['Full-step'].size / df['Full-step'].size)):
  plt.figure(figsize=(6, 6), dpi=100, facecolor="w")
  plt.plot(dfs['Full-step'][(N * i):(N * i + N)], dfs['CW1(pF)'][(N * i):(N * i + N)], label=dfs.iloc[(N * i), 13])  # label = file name
  plt.plot(dfs['Full-step'][(N * i):(N * i + N)], dfs['CW2(pF)'][(N * i):(N * i + N)], label=ALL_5TIMES_AV_DEV[i])  # 5 times avg cap
  plt.plot(dfs['Full-step'][(N * i):(N * i + N)], dfs['CW3(pF)'][(N * i):(N * i + N)])
  plt.plot(dfs['Full-step'][(N * i):(N * i + N)], dfs['CW4(pF)'][(N * i):(N * i + N)])
  plt.plot(dfs['Full-step'][(N * i):(N * i + N)], dfs['CW5(pF)'][(N * i):(N * i + N)])
  plt.plot(dfs['Full-step'][(N * i):(N * i + N)], dfs['CW5K(pF)'][(N * i):(N * i + N)], 'r', linestyle='dashed')

  # 画上下限
  plt.plot(dfs['Full-step'][(N * i):(N * i + N)], yLimitUp, 'b', linestyle='dashed')
  plt.plot(dfs['Full-step'][(N * i):(N * i + N)], yLimitDw, 'b', linestyle='dashed')
  plt.legend(loc="best")
  plt.show()
##################################################################################################################


##################################################################################################################
# Calc: 容值采集数据分析，基础数据存在 df_cap_all 中
# 容值采集上下限数据
capLen = round(dfCap.size / 4)
capAllLen = round(dfCapAll['A'].size)
yLimitUpCap = np.zeros(capLen)
yLimitDwCap = np.zeros(capLen)
for k in range(capLen):
  if (dfCap.iloc[k, 1]) < 100:
    yLimitUpCap[k] = 1
    yLimitDwCap[k] = -yLimitUpCap[k]
  else:
    yLimitUpCap[k] = dfCap.iloc[k, 1] * 0.01
    yLimitDwCap[k] = -yLimitUpCap[k]

plt.figure(figsize=(6, 6), dpi=100, facecolor="w")
plt.title('cap_dev CW&CCW')
# 用于获取当前理想容值
CapRT = 0
k = 0
for i in range(capAllLen):  # 每一个测试文件，数据长度不一样，无法使用定长数据读数
  if dfCapAll.iloc[i, 0] > CapRT:
    CapRT = dfCapAll.iloc[i, 0]
    k = k + 1
  else:
    plt.plot(dfCapAll['A'][(i - k):i], dfCapAll['B'][(i - k):i])  # CW
    plt.plot(dfCapAll['A'][(i - k):i], dfCapAll['C'][(i - k):i])  # CCW
    CapRT = 0
    k = 0
  if i == capAllLen - 1:
    plt.plot(dfCapAll['A'][(i - k):i], dfCapAll['B'][(i - k):i])  # CW
    plt.plot(dfCapAll['A'][(i - k):i], dfCapAll['C'][(i - k):i])  # CCW
# 画上下限
plt.plot(dfCap['A'][0:capLen], yLimitUpCap, 'b', linestyle='dashed')
plt.plot(dfCap['A'][0:capLen], yLimitDwCap, 'b', linestyle='dashed')
##################################################################################################################


##################################################################################################################
# Calc: 容值采集数据分析, 画 CW 与 CCW 的差值
All_CWCCW_AV_DEV = []
All_CWCCW_MAX_DEV = []
All_CAP_MAX_DEV = []
plt.figure(figsize=(6, 6), dpi=100, facecolor="w")
plt.title('CW-CCW')
CapRT = 0
k = 0
h = -1
for i in range(capAllLen):  # 每一个测试文件，数据长度不一样，无法使用定长数据读数
  if dfCapAll.iloc[i, 0] > CapRT:
    CapRT = dfCapAll.iloc[i, 0]
    k = k + 1
    if dfCapAll.iloc[i, 0] > 100:
      h = h + 1
  else:
    plt.plot(dfCapAll['A'][(i - k):i], dfCapAll['CWCCW(pF)'][(i - k):i])
    All_CWCCW_AV_DEV.append(dfCapAll['CWCCW'][(i - h):i].mean())  # 统计 CW 与 CCW 差值的平均相对偏差
    All_CWCCW_MAX_DEV.append(dfCapAll['CWCCW'][(i - h):i].max())  # 统计 CW 与 CCW 差值的最大相对偏差

    CW_max = abs(dfCapAll['CW'][(i - h):i].max())  # 统计 CW 的最大相对偏差
    CCW_max = abs(dfCapAll['CCW'][(i - h):i].max())  # 统计 CCW 的最大相对偏差
    All_CAP_MAX_DEV.append(max(CW_max, CCW_max))  # 记录 CW 和 CCW 中最大的相对偏差

    CapRT = 0
    k = 0
    h = -1
  if i == capAllLen - 1:
    plt.plot(dfCapAll['A'][(i - k):i], dfCapAll['CWCCW(pF)'][(i - k):i])
    All_CWCCW_AV_DEV.append(dfCapAll['CWCCW'][(i - h):i].mean())
    All_CWCCW_MAX_DEV.append(dfCapAll['CWCCW'][(i - h):i].max())

    CW_max = abs(dfCapAll['CW'][(i - h):i].max())
    CCW_max = abs(dfCapAll['CCW'][(i - h):i].max())
    All_CAP_MAX_DEV.append(max(CW_max, CCW_max))
## 画上下限
plt.plot(dfCap['A'][0:capLen], yLimitUpCap, 'b', linestyle='dashed')
plt.plot(dfCap['A'][0:capLen], yLimitDwCap, 'b', linestyle='dashed')
##################################################################################################################


##################################################################################################################
# 大于 100 pF 时，CW 和 CCW 统计平均偏差
allCWCCWAvLen = len(All_CWCCW_AV_DEV)
plt.figure(figsize=(6, 6), dpi=100, facecolor="w")
plt.title('All_CWCCW_AV_DEV')
plt.scatter(range(allCWCCWAvLen), All_CWCCW_AV_DEV)
plt.plot(range(allCWCCWAvLen), np.ones(allCWCCWAvLen) * 0.003, 'r', label='CW-CCW limit')
plt.legend(loc="best")
plt.show()
##################################################################################################################


##################################################################################################################
# 大于 100 pF 时，CW 和 CCW 统计最大偏差
allCapMaxLen = len(All_CAP_MAX_DEV)
plt.figure(figsize=(6, 6), dpi=100, facecolor="w")
plt.title('All_CAP_MAX_DEV')
plt.scatter(range(allCapMaxLen), All_CAP_MAX_DEV)
plt.plot(range(allCapMaxLen), np.ones(allCapMaxLen) * 0.01, 'r', label='CW and CCW limit')
plt.legend(loc="best")
plt.show()
##################################################################################################################


##################################################################################################################
All_CW_STEP_AVG = []
All_CW_STEP_STD = []
All_CCW_STEP_AVG = []
All_CCW_STEP_STD = []
dfStepAllLen = round(dfStepAll.size / 6)
CapRT = 0
k = 0

plt.figure(figsize=(6, 6), dpi=100, facecolor="w")
plt.title('Step_Dev CW&CCW')
# Plot: 容值步进变化量
for i in range(dfStepAllLen):  # 每一个测试文件，数据长度不一样，无法使用定长数据读数
  if dfStepAll.iloc[i, 0] > CapRT:
    CapRT = dfStepAll.iloc[i, 0]
    k = k + 1
  else:
    plt.plot(dfStepAll['A'][(i - k):i], dfStepAll['CW(pF)'][(i - k):i])  # CW
    plt.plot(dfStepAll['A'][(i - k):i], dfStepAll['CCW(pF)'][(i - k):i])  # CCW
    All_CW_STEP_AVG.append(dfStepAll['CW(pF)'][(i - k):i].mean())  # 统计时去掉前10个点
    All_CCW_STEP_AVG.append(dfStepAll['CCW(pF)'][(i - k):i].mean())
    All_CW_STEP_STD.append(dfStepAll['CW(pF)'][(i - k):i].std())  # 统计时去掉前10个点
    All_CCW_STEP_STD.append(dfStepAll['CCW(pF)'][(i - k):i].std())
    CapRT = 0
    k = 0
  if i == dfStepAllLen - 1:
    plt.plot(dfStepAll['A'][(i - k):i], dfStepAll['CW(pF)'][(i - k):i])  # CW
    plt.plot(dfStepAll['A'][(i - k):i], dfStepAll['CCW(pF)'][(i - k):i])  # CCW
    All_CW_STEP_AVG.append(dfStepAll['CW(pF)'][(i - k):i].mean())
    All_CCW_STEP_AVG.append(dfStepAll['CCW(pF)'][(i - k):i].mean())
    All_CW_STEP_STD.append(dfStepAll['CW(pF)'][(i - k):i].std())  # 统计时去掉前10个点
    All_CCW_STEP_STD.append(dfStepAll['CCW(pF)'][(i - k):i].std())

# CW 和 CCW  步进统计，均值与标准差
allCWStepAvgLen = len(All_CW_STEP_AVG)
plt.figure(figsize=(6, 6), dpi=100, facecolor="w")
plt.title('Step_AVG & Step_STD_DEV')
plt.scatter(range(allCWStepAvgLen), All_CW_STEP_AVG, label='CW AVG_DEV')
plt.scatter(range(allCWStepAvgLen), All_CW_STEP_STD, label='CW STD_DEV')
plt.legend(loc="best")
plt.show()
##################################################################################################################
