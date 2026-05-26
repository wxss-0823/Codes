#!D:\Users\Anaconda\anaconda3\python.exe
# -*- coding: utf-8 -*-
# @Time    : 2026/3/23 11:21
# @Author  : Coffee
# @Project : ReferanceV3.py
# @File    : COMET4Points.py

import os

import re

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import csv
import warnings
import shutil

warnings.filterwarnings('ignore')

def find_closest(
    df:pd.DataFrame,
    points_tuple:tuple
) -> tuple:
  """
  寻找距离 COMET 检验点最近的点
  """
  Target = tuple()
  for Point in points_tuple:
    cap_idx = int(len(df["CAP"]) / 2)
    idx = np.nanargmin(abs(df["CAP"][:cap_idx] - Point))
    Target = Target + (idx,)
  return Target


def read_sn(
    file_dir
) -> list:
  """
  读取 CSV 中，BZH 退回电容 SN 信息
  """
  sn_list = list()
  with open(file_dir, 'r', encoding='utf-8') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
      sn_list.append(row[0])
  return sn_list

def find_target_pos_cap(
    cap_dataframe: pd.DataFrame,
    target_list: tuple,
    hint_str=""
) -> list:
  """
  寻找检验点位置处的容值
  """
  if hint_str:
    print(hint_str)
  for pos in target_list:
    returned_data.append(cap_dataframe.loc[pos, "CW"])
  for pos in target_list:
    returned_data.append(cap_dataframe.loc[pos, "CCW"])
  return returned_data

def check_limit(
    up_limit_list: list,
    dw_limit_list: list,
    check_list: list,
    pass_dict: dict
) -> dict :
  """
  检验是否超过上下限
  """
  check_status = True
  for row in check_list:
    for i in range(4):
      if dw_limit_list[i] <  row[0][i] < up_limit_list[i] and \
         dw_limit_list[i] <  row[0][i + 4] < up_limit_list[i]:
        check_status = True
      else:
        check_status = False
        break

    if check_status:
      # row = (returned_data, file, sn)
      if row[2] in pass_dict:
        pass_list = pass_dict[row[2]]
        pass_list.append(row[1])
        pass_dict[row[2]] = pass_list
      else:
        pass_list = [row[1]]
        pass_dict[row[2]] = pass_list
  return pass_dict

def result_plot(
    type_sn: str,
    inspect_std: tuple,
    deviation_list: list,
    figure_dir: str
) -> tuple :
  """
  绘制结果图像
  """
  up_lim = []
  dw_lim = []
  for point in inspect_std:
    if point < 100:
      up_lim.append(1)
      dw_lim.append(-1)
    else:
      up_lim.append(0.01 * point + 0.2) # 1% ± 0.2 PF
      dw_lim.append(-0.01 * point - 0.2) # 1% ± 0.2 PF

  idx_arr = inspect_std
  plt.figure(figsize=(5,5), dpi=100, facecolor="w")
  plt.title(type_sn)
  # for row_list in dev_list:
  for row_list in deviation_list:
    plt.plot(idx_arr, row_list[0][0:4])
    plt.plot(idx_arr, row_list[0][4:8])

  plt.plot(idx_arr, up_lim, 'r', linestyle='dashed', linewidth=2)
  plt.plot(idx_arr, dw_lim, 'r', linestyle='dashed', linewidth=2)
  os.makedirs(figure_dir, exist_ok=True)
  plt.savefig(os.path.join(figure_dir, type_sn))
  # plt.savefig(os.path.join(figure_dir, type_sn))
  # plt.show()
  return up_lim, dw_lim

iqc_dir = r"D:\Users\Wxss\01Project\01VVC\03Data\02IQC\0Variable"
fig_dir = os.path.join(iqc_dir, "Comet4点检测")
fail_ptn = r"(081900\d{2}-001).*(Failed)"
captest_ptn = r"Captest.*.xlsx"

os.makedirs(fig_dir, exist_ok=True)

# 电容型号及容值范围
cap_type_dict = {
  '08190001-001': (25, 250),
  '08190001-002': (25, 250),

  '08190003-001': (150, 1500),
  '08190003-002': (150, 1500),

  '08190006-001': (150, 1500),
  '08190006-002': (150, 1500),

  '08190010-001': (50, 500),
  '08190010-002': (50, 500),

  '08190043-001': (50, 500),

  '08190044-001': (100, 1000),
  '08190044-002': (100, 1000),

  '08190049-001': (5, 500),
}

# 明显异常电容列表
file_except_list = [
  "Captest_1972444_102525603224_500pF_2025_06_08_10_21_57.xlsx",
  "Captest_2000536_102565981011_500pF_2025_09_25_17_09_50.xlsx",
  "Captest_1976143_102565981028_500pF_2025_09_04_08_57_46.xlsx",
  "Captest_2113773_H4490245_250pF_2025_08_10_13_39_08.xlsx",
  "Captest_2114558_H4180098_250pF_2025_08_18_10_11_14.xlsx",
  "Captest_2114558_H4180098_250pF_2025_08_18_10_25_51.xlsx",
  "Captest_2144952_H5270442_250pF_2025_10_30_13_42_49.xlsx",
  "Captest_2148370_H5320081_250pF_2025_12_01_15_48_46.xlsx",
  "Captest_2166927_H4440616_250pF_2025_09_21_09_28_18.xlsx",
  "Captest_2167671_H5130500_250pF_2025_10_26_15_06_09.xlsx",
  "Captest_2198322_H5380374_250pF_2025_12_22_17_13_30.xlsx",
  "Captest_2202100_H5380480_250pF_2025_12_28_10_53_04.xlsx",
  "Captest_2203182_H5380058_250pF_2025_12_24_19_45_14.xlsx",
  "Captest_2095972_H4490278_500pF_2025_08_24_10_05_26.xlsx",
  "Captest_2114552_H4490262_250pF_2025_08_17_15_35_32.xlsx",
  "Captest_2142735_H5130418_250pF_2025_10_30_16_37_54.xlsx",
  "Captest_2156013_H5271523_1500pF_2025_12_07_16_04_48.xlsx",
  "Captest_2177702_H5351456_1500pF_2025_12_20_17_26_35.xlsx",
  "Captest_2206333_H5451205_1500pF_2026_01_19_17_08_55.xlsx",
]

sn_set = set()
sn_4points_dict = dict()
failed_dir_dict:dict[str, list[str]] = dict()
failed_dir_list:list[str] = list()

BZH_returned_cap_list = read_sn(r"D:\Users\WorkSpace\Pycharm\Auxiliary\ManualStatistic\Output\BZH退回电容0320.csv")

# for item in next(os.walk(iqc_dir))[1]:
for root_dir, items, _ in os.walk(iqc_dir):
  for item in items:
    if re.search(fail_ptn, item):
      matched_sn = re.search(fail_ptn, item).group(1)
      sn_set.add(matched_sn)
      if matched_sn in failed_dir_dict:
        failed_dir_list = failed_dir_dict[matched_sn]
      else:
        failed_dir_list = []
      # failed_dir_list.append(os.path.join(iqc_dir, item))
      failed_dir_list.append(os.path.join(root_dir, item))
      failed_dir_dict[matched_sn] = failed_dir_list


for sn in sn_set:
  (cmin, cmax) = cap_type_dict[sn]

  dc = (0.9 * cmax - (cmin + 0.1 * cmax))/3
  c1 = cmin + 0.1 * cmax
  c2 = cmin + 0.1 * cmax + dc
  c3 = cmin + 0.1 * cmax + 2 * dc
  c4 = cmin + 0.1 * cmax + 3 * dc

  points = (c1, c2, c3, c4)
  sn_4points_dict[sn] = points

cap_df = pd.DataFrame()
dev_list = list()
sub_list = list()
fail_num_dict = dict()
fail_num_list = list()
pass_num_dict = dict()

# BZH var
had_data_list = list()
had_data_dict = dict()
returned_pass_num_dict = dict()

for sn in failed_dir_dict:
  dev_list = []
  # BZH var
  returned_dev_list = []
  for failed_dir in failed_dir_dict[sn]:
    for root_dir, sub_dir, files in os.walk(failed_dir):
      for file in files:
        if re.match(captest_ptn, file, re.I):  # and file not in file_except_list
          if sn in fail_num_dict:
            fail_num_list = fail_num_dict[sn]
          else:
            fail_num_list = []
          fail_num_list.append(file)
          fail_num_dict[sn] = fail_num_list
          # print(f"Load: {file}")
          filename = os.path.join(root_dir, file)
          sub_list = []
          # BZH var
          returned_data = list()
          selected_sheet_name = ""
          SHEET_NAME_LIST = pd.ExcelFile(filename).sheet_names
          if "Sheet1" in SHEET_NAME_LIST:
            selected_sheet_name = "Sheet1"
          elif "sheet1" in SHEET_NAME_LIST:
            selected_sheet_name = "sheet1"
          cap_df = pd.read_excel(filename, sheet_name=selected_sheet_name, usecols=[0, 1, 2, 3])
          cap_df.columns = ["CAP", "Cvalue", "CW", "CCW"]
          if selected_sheet_name == "sheet1":
            cap_df = cap_df.drop(0)
            cap_df = cap_df.astype({
              "CAP": float,
              "Cvalue": float,
              "CW": float,
              "CCW": float
            })

          target = find_closest(cap_df, sn_4points_dict[sn])

          # 筛选 BZH 退回电容 SN
          if re.search(r"_(\d{7})_", file):
            cap_sn = re.search(r"_(\d{7})_", file).group(1)
            hint = f"BZH 退回电容 {sn}: {cap_sn}"

            if cap_sn in BZH_returned_cap_list:
              if sn in had_data_dict:
                had_data_list = had_data_dict[sn]
                if cap_sn not in had_data_list:
                  had_data_list.append(cap_sn)
                  had_data_dict[sn] = had_data_list
                  returned_data = find_target_pos_cap(cap_df, target, hint_str=hint)
                  # os.makedirs(os.path.join(r"C:\Users\w00025121\Desktop\temp", sn), exist_ok=True)
                  # shutil.copy(os.path.join(root_dir, file), os.path.join(r"C:\Users\w00025121\Desktop\temp", sn))
                  # shutil.copytree(root_dir, os.path.join(r"C:\Users\w00025121\Desktop\temp", sn), dirs_exist_ok=True)
              else:
                had_data_list = [cap_sn]
                had_data_dict[sn] = had_data_list
                returned_data = find_target_pos_cap(cap_df, target, hint_str=hint)
                # os.makedirs(os.path.join(r"C:\Users\w00025121\Desktop\temp", sn), exist_ok=True)
                # shutil.copy(os.path.join(root_dir, file), os.path.join(r"C:\Users\w00025121\Desktop\temp", sn))
                # shutil.copytree(root_dir, os.path.join(r"C:\Users\w00025121\Desktop\temp", sn), dirs_exist_ok=True)
              if returned_data:
                returned_dev_list.append((returned_data, file, sn))

          # 去除明显异常 SN
          if (cap_df.loc[target[-1], "CW"] < -200
              or cap_df.loc[target[-1], "CW"] > 200
              or cap_df.loc[target[-1], "CCW"] < -200
              or cap_df.loc[target[-1], "CCW"] > 200
              or cap_df.loc[target[0], "CW"] < -30
              or cap_df.loc[target[0], "CCW"] < -30
          ):
            # print(file)
            pass

          sub_list = find_target_pos_cap(cap_df, target)

          dev_list.append((sub_list, file, sn))

  fig_dir = r"D:\Users\Wxss\01Project\01VVC\03Data\02IQC\0Variable\BZH退回电容"
  up_limit, dw_limit = result_plot(sn, sn_4points_dict[sn], returned_dev_list, fig_dir)

  pass_num_dict = check_limit(up_limit, dw_limit, dev_list, pass_num_dict)

  # BZH 新标准下通过数量统计
  returned_pass_num_dict = check_limit(up_limit, dw_limit, returned_dev_list, returned_pass_num_dict)

# for sn in fail_num_dict:
#   print(f"{sn}: {len(pass_num_dict[sn])}/{len(fail_num_dict[sn])}")

for sn in returned_pass_num_dict:
  print(f"{sn}: {len(returned_pass_num_dict[sn])}/{len(had_data_dict[sn])}")
