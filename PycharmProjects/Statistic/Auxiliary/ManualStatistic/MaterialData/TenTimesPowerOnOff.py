#!D:\Users\Anaconda\anaconda3\python.exe
# -*- coding: utf-8 -*-
# @Time    : 2026/4/1 15:19
# @Author  : Coffee
# @Project : Pycharm
# @File    : TenTimesPowerOnOff.py

import os
import re
import time
from datetime import datetime
from os.path import exists
import pandas as pd
import matplotlib.pyplot as plt
from numpy.matlib import empty
from pandas.core.window.doc import kwargs_numeric_only

plt.rcParams['axes.unicode_minus'] = False
import numpy as np
import csv


def result_plot(
    fluctuation_list: list,
    capacity_list: list,
    figure_directory: str,
    output_directory: str,
    **kwargs
) -> bool :
  """
  绘制上下电波动及一致性图像
  fluctuation_list: 单电容最大波动
  capacity_list: 单电容上下电序列
  timestamp: 输出文件时间戳
  output: str
  """
  ## 解包
  sn = kwargs.get('sn', 'Unknown')
  sn_num = kwargs.get('sn_num', 0)
  risk_sn = kwargs.get('risk_sn', [])

  ## Check-如果没有数据，直接返回
  if len(fluctuation_list) == 0:
    return False

  ## Plot-上下电波动一致性
  plt.rcParams['font.sans-serif'] = ['SimHei']
  fig, ax = plt.subplots(figsize=(7, 7), dpi=300, facecolor="w")
  plt.title(f'{sn}-上下电波动一致性')
  num = np.array([i + 1 for i in range(len(fluctuation_list))])
  plt.scatter(num, fluctuation_list)
  ax.set_yticks(np.linspace(min(fluctuation_list), max(fluctuation_list), 5))
  ax.set_xticks(np.linspace(1, len(num), 5))
  plt.xlabel("数量")
  plt.ylabel("容值/pF")

  plt.savefig(os.path.join(figure_directory, f"{sn}-上下电波动一致性.png"))
  plt.close()

  ## Plot-上下电波动
  fig, ax = plt.subplots(figsize=(7, 7), dpi=100, facecolor="w")
  plt.title(f'{sn}-上下电波动')
  num = np.array([i + 1 for i in range(len(capacity_list[0]))])
  cap_min = 2000
  cap_max = 0
  for i in range(len(fluctuation_list)):
    plt.plot(num, capacity_list[i], 'o-', markersize=4)
    if min(capacity_list[i]) < cap_min:
      cap_min = min(capacity_list[i])
    if max(capacity_list[i]) > cap_max:
      cap_max = max(capacity_list[i])

  ax.set_yticks(np.linspace(cap_min, cap_max, 5))
  ax.set_xticks(num)
  plt.xlabel("第N次")
  plt.ylabel("容值/pF")
  plt.savefig(os.path.join(figure_directory, f"{sn}-上下电波动.png"))
  plt.close()

  ## 写入不合格产品编码
  with open(output_directory, 'a', newline='', encoding='utf-8') as csv_file:
    csv_writer = csv.writer(csv_file)
    # csv_writer.writerow(['SN', 'CAP SN', 'GAP', 'GAP LIM'])
    csv_writer.writerow(['统计总数：', sn, sn_num])
    csv_writer.writerows(risk_sn)

  return False

def getPowerOnOffData(
    batch_dir: str,
    figure_dir: str,
    time_stamp: str,
    ver_ptn: str
):
  sn = ""
  gap_list = []
  cap_list = []
  risk_sn = []
  sn_map = {}
  sn_num = 0

  # Drop First point
  drop_gap_list = []
  drop_cap_list = []
  drop_risk_sn = []

  for root, dirs, files in os.walk(batch_dir):
    for file in files:
      if file.endswith(".xlsx") and file[0] != '~' and re.search(ver_ptn, file):
        sn_num += 1
        file_name = os.path.join(root, file)
        df = pd.read_excel(file_name, sheet_name="sheet2", nrows=10)
        df.columns = ["C(pF)", "Spec-Min", "Spec-Max", "Result"]
        df = df.drop(0)

        gap_list.append(float(df["C(pF)"][8]))
        temp_list = []
        drop_temp_list = []
        for i in range(5):
          temp_list.append(float(df.iloc[i, 0]))
          if i != 4:
            drop_temp_list.append(float(df.iloc[i + 1, 0]))
        cap_list.append(temp_list)
        drop_cap_list.append(drop_temp_list)
        drop_gap_list.append(max(drop_temp_list) - min(drop_temp_list))

        sn = re.search(r"081900\d{2}-00[12]", file).group(0)
        lim_file_dir = r'D:\Users\WorkSpace\Pycharm\Auxiliary\ManualStatistic\MaterialData\find_zero_lim.csv'

        with open(lim_file_dir, 'r', encoding='utf-8') as csv_file:
          csv_reader = csv.reader(csv_file)
          for rows in csv_reader:
            row_splits = rows[0].split(' ')
            sn_map[row_splits[0]] = (row_splits[1], row_splits[2])

        gap_lim = float(sn_map[sn][1])
        cap_sn = ""
        try:
          if sn[-1] == "1":
            cap_sn = re.search(r"_(\d{7})_", file).group(1)
          elif sn[-1] == "2":
            cap_sn = re.search(r"_(GL\d+)_", file).group(1)
          else:
            print("SN Type Error.")
        except AttributeError as e:
          print(f"File: {file} has no sn pattern.")

        if gap_list[-1] > gap_lim:
          risk_sn.append((sn, cap_sn, gap_list[-1], gap_lim))

        if drop_gap_list[-1] > gap_lim:
          drop_risk_sn.append((sn, cap_sn, drop_gap_list[-1], gap_lim))

  output_dir = fr'D:\Users\WorkSpace\Pycharm\Auxiliary\ManualStatistic\Output\find_zero_error_{time_stamp}.csv'
  # result_plot(gap_list, cap_list, figure_dir, output_dir, sn=sn, sn_num=sn_num, risk_sn=risk_sn)
  result_plot(drop_gap_list, drop_cap_list, figure_dir, output_dir, sn=sn, sn_num=sn_num, risk_sn=drop_risk_sn)


