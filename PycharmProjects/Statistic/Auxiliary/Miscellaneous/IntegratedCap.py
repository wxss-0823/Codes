#!D:\Users\Anaconda\anaconda3\python.exe
# -*- coding: utf-8 -*-
# @Time    : 2026/9/1 9:17
# @Author  : Coffee
# @Project : Miscellaneous
# @File    : IntegratedCap.py

import os
import sys
import re
import io

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from numpy import ndarray
from openpyxl.drawing.image import Image
from openpyxl import load_workbook
from openpyxl import workbook
from pathlib import Path

from openpyxl.workbook import Workbook


def plotScatter(
    x_data: list | ndarray,
    y_data: list,
    fig_save_dir: str = r"D:/",
    sheet_name: str = "Sheet1",
    **kwargs
) -> bool:
  fig_title = kwargs.get("title")
  anchor_pos = kwargs.get("fig_anchor") if kwargs.get("fig_anchor") else "H2"
  # 设置中文字体
  plt.rcParams['font.sans-serif'] = ['Microsoft YaHei']
  plt.figure(figsize=(8, 6), dpi=300)
  plt.title(fig_title)
  plt.scatter(x_data, y_data)

  # 将图表保存到内存中的 BytesIO 对象
  img_buffer = io.BytesIO()
  plt.savefig(img_buffer, format='png', dpi=300, bbox_inches='tight')
  plt.close()

  # 将 BytesIO 转换为 openpyxl 可用的 Image 对象
  img_buffer.seek(0)  # 重置指针到开始位置
  img = Image(img_buffer)

  # 选择要插入图片的Sheet
  origin_wb = load_workbook(fig_save_dir)
  origin_ws = origin_wb[sheet_name]

  # 调整图片大小
  img.width = 400
  img.height = 300
  origin_ws.add_image(img, anchor_pos)  # 锚定图像

  origin_wb.save(fig_save_dir)
  print(f"Info: [{plotScatter.__name__}] insert figure {fig_title} done.")
  return True

def liveTest(
    file_dir: str,
    tar_dir: str,
    test_code: str="D1",
) -> bool:
  # 创建文件
  if not Path(tar_dir).exists():
    new_wb = Workbook()
    new_wb.save(tar_dir)

  # 需读取的列
  use_cols = ['StepDiscription', 'vvc_VvcCapPosition', 'vvc_ActualCapPosition', 'LCR_ActualCapacitancePicoF']
  if test_code == "D2":
    use_cols.append('Result')

  # 读取数据
  live_test_date = pd.read_csv(file_dir,
                               usecols=use_cols,
                               dtype={'StepDiscription': str,
                                      'vvc_VvcCapPosition': np.float32,
                                      'vvc_ActualCapPosition': np.float32,
                                      'LCR_ActualCapacitancePicoF': np.float64
                                      },
                               encoding='gbk'
                               )
  # 清除 NAN
  live_test_date = live_test_date.dropna(subset=['LCR_ActualCapacitancePicoF'])
  live_test_date = live_test_date.reset_index(drop=True)

  # 电容 SN
  comet_sn_pattern = r"pF-(\d{7})(-[^\\]*)?"
  cap_sn = re.search(comet_sn_pattern, file_dir).group(1)
  cap_suffix = re.search(comet_sn_pattern, file_dir).group(2)

  # 分类容值
  cap_test_set = set()
  cap_map_dict = {float: list()}

  # 筛选异常数据中心值
  # screening_center = {"1623844": [24.48, 69.42], "1623848": [25.27, 70.35], "1634816": [24.92, 69.96]}  # 250 pF
  # screening_center = {"1585902": [148.9, 419.7], "1595837": [150.8, 421.4], "1595846": [148.9, 409.8]}  # 1500 pF
  screening_center = {"1718641": [50, 140]}  # 500 pF

  # 筛选异常数值条件
  # screening_factor = {"D1": 1, "D2": 0.01, "D3": 0.001}  # 250 pF
  # screening_factor = {"D1": 1, "D2": 1, "D3": 0.02}  # 1500 pF
  screening_factor = {"D1": 1, "D2": 1, "D3": 1}  # 1500 pF

  # 描述信息匹配
  keyword_pattern = {"D1": r"\d+(?:\.\d+)?", "D2": r"\d+(?:\.\d+)?|上电等待初始化完成", "D3": r"\d+(?:\.\d+)?"}

  # 获取数据
  for i in range(len(live_test_date)):
    # 获取常规总数据
    # cap_type = np.float32((live_test_date['StepDiscription'][i]).split("%")[0])   # 不兼容 D2, D3
    cap_per_match = re.search(keyword_pattern[test_code], live_test_date['StepDiscription'][i])
    if not cap_per_match:
      continue
    cap_type = np.float32(cap_per_match.group(0)) if test_code != "D2" else cap_per_match.group(0)
    cap_setpos = live_test_date['vvc_VvcCapPosition'][i]
    # cap_actpos = live_test_date['vvc_ActualCapPosition'][i]
    cap_val = live_test_date['LCR_ActualCapacitancePicoF'][i]

    # 常规筛选条件
    # norm_condition = np.abs(cap_val - cap_actpos) > cap_actpos * screening_factor[test_code]
    # D2 特殊筛选条件
    d2_condition = live_test_date["Result"][i] == "fail" if test_code == "D2" else False
    # D3 特殊异常值筛选中心
    d3_center = screening_center[cap_sn]
    d3_cond1 = np.abs(cap_val - d3_center[0]) > d3_center[0] * screening_factor[test_code]
    d3_cond2 = np.abs(cap_val - d3_center[1]) > d3_center[1] * screening_factor[test_code]
    d3_condition = d3_cond1 and d3_cond2 if test_code == "D3" else False

    # 添加筛选后数值
    cap_test_set.add((cap_type, cap_setpos)) if not (d2_condition or d3_condition) else None
    # if norm_condition or d2_condition or d3_condition:
    if d2_condition or d3_condition:
      # 去除异常测试点
      continue
    elif cap_type in cap_map_dict:
      cap_map_dict[cap_type].append(cap_val)
    else:
      cap_map_dict[cap_type] = [cap_val]

  # 处理数据
  cap_per, cap_pos, cap_num, cap_mean, cap_std, cap_dev_avg_per = [], [], [], [], [], []
  summary_sheet = {
    "Percent(%)":   cap_per,            # 下发电容百分比
    "Cap(pF)":      cap_pos,            # 下发电容位置
    "Num":          cap_num,            # 测量该容值的总点数
    "LCR Mean(pF)": cap_mean,           # 回读电容均值
    "LCR Std(pF)":  cap_std,            # 回读电容标准差
    "DAV(%)":       cap_dev_avg_per     # 容值最值波动占均值比例
  }
  cap_test_set = sorted(cap_test_set)
  for cap in cap_test_set:
    cap_per.append(cap[0])
    cap_pos.append(cap[1])
    cap_num.append(len(cap_map_dict[cap[0]]))
    cap_mean.append(np.mean(cap_map_dict[cap[0]]))
    cap_std.append(np.std(cap_map_dict[cap[0]]))
    cap_dev_avg_per.append((np.max(np.array(cap_map_dict[cap[0]])) - np.min(np.array(cap_map_dict[cap[0]]))) / cap_mean[-1] * 100)

  # 写入处理结果至 EXCEL
  summary_pd = pd.DataFrame(summary_sheet)
  with pd.ExcelWriter(tar_dir, engine='openpyxl', mode='a', if_sheet_exists='replace')as writer:
    sheet_name = test_code + '-' + cap_sn + (cap_suffix if cap_suffix else "")
    summary_pd.to_excel(writer, sheet_name=sheet_name, index=False)
  # print(cap_map_dict)

  # 绘图锚点及通用绘图容值序列
  anchor_list = ["H1", "N1", "H18", "N18"]
  anchor_iter = iter(anchor_list)
  plot_list = {"D1": [0, 30, 60, 100], "D2": ["上电等待初始化完成"], "D3": [0, 20]}

  # DAV 超限的图像追加绘制
  DAV_LIM = 0.4
  for i in range(len(cap_dev_avg_per)):
    if cap_dev_avg_per[i] > DAV_LIM and (cap_per[i] not in plot_list[test_code]):
      plot_list[test_code].append(cap_per[i])
      anchor_list.append("A35")

  # 绘图并导入 EXCEL
  for per in plot_list[test_code]:
    set_cap = summary_sheet["Cap(pF)"][summary_sheet["Percent(%)"].index(per)]
    plotScatter(
      np.linspace(1, len(cap_map_dict[per]), len(cap_map_dict[per])),
      cap_map_dict[per],
      tar_dir,
      sheet_name,
      title=f"Set Position: {set_cap} pF",
      fig_anchor=next(anchor_iter)
    )
  plotScatter(
    np.linspace(1, len(cap_dev_avg_per), len(cap_dev_avg_per)),
    cap_dev_avg_per,
    tar_dir,
    sheet_name,
    title=f"DAV(%)",
    fig_anchor="T1"
  )

  print(f"Info: [{liveTest.__name__}] {sheet_name} data processed done.")

  return True




if __name__ == '__main__':
  ORIGINAL_FILE_DIR_250 = {
    "D1_DATA_LIST": [
      r"D:\Users\Share\实验室文件\4_VVC 集成电容验证\原始数据\D1-不下电重复性\250pF-1623848\VVC_VVC_CAP_不下电重复性测试_T001_20260819_200640.csv",
      r"D:\Users\Share\实验室文件\4_VVC 集成电容验证\原始数据\D1-不下电重复性\250pF-1623844\VVC_VVC_CAP_不下电重复性测试_T001_20260829_180509.csv",
      r"D:\Users\Share\实验室文件\4_VVC 集成电容验证\原始数据\D1-不下电重复性\250pF-1634816\VVC_VVC_CAP_不下电重复性测试_T001_20260814_172751.csv"
    ],
    "D2_DATA_LIST": [
      r"D:\Users\Share\实验室文件\4_VVC 集成电容验证\原始数据\D2-下电重复性\250pF-1623844\VVC_VVC_CAP_下电重复性测试_T002_20260830_121818.csv",
      r"D:\Users\Share\实验室文件\4_VVC 集成电容验证\原始数据\D2-下电重复性\250pF-1623848\VVC_VVC_CAP_下电重复性测试_T002_20260820_142112.csv",
      r"D:\Users\Share\实验室文件\4_VVC 集成电容验证\原始数据\D2-下电重复性\250pF-1634816\VVC_VVC_CAP_下电重复性测试_T002_20260815_183227.csv"
    ],
    "D3_DATA_LIST": [
      r"D:\Users\Share\实验室文件\4_VVC 集成电容验证\原始数据\D3-传动系统短稳定性\250pF-1623844\VVC_VVC_传动系统短稳定测试_T003_20260830_005953.csv",
      r"D:\Users\Share\实验室文件\4_VVC 集成电容验证\原始数据\D3-传动系统短稳定性\250pF-1623848\VVC_VVC_传动系统短稳定测试_T003_20260820_030117.csv",
      r"D:\Users\Share\实验室文件\4_VVC 集成电容验证\原始数据\D3-传动系统短稳定性\250pF-1634816\VVC_VVC_传动系统短稳定测试_T003_20260815_002451.csv"
    ]
  }

  ORIGINAL_FILE_DIR_1500 = {
    "D1_DATA_LIST": [
      r"D:\Users\Share\实验室文件\4_VVC 集成电容验证\原始数据\D1-不下电重复性\1500pF-1585902\VVC_VVC_CAP_不下电重复性测试_T001_20260722_121914.csv",
      r"D:\Users\Share\实验室文件\4_VVC 集成电容验证\原始数据\D1-不下电重复性\1500pF-1595837\VVC_VVC_CAP_不下电重复性测试_T001_20260831_172715.csv",
      r"D:\Users\Share\实验室文件\4_VVC 集成电容验证\原始数据\D1-不下电重复性\1500pF-1595846\VVC_VVC_CAP_不下电重复性测试_T001_20260902_222122.csv",
      r"D:\Users\Share\实验室文件\4_VVC 集成电容验证\原始数据\D1-不下电重复性\1500pF-1595846-复测\VVC_VVC_CAP_不下电重复性测试_T001_20260907_164519.csv"
    ],
    "D2_DATA_LIST": [
      r"D:\Users\Share\实验室文件\4_VVC 集成电容验证\原始数据\D2-下电重复性\1500pF-1585902\VVC_VVC_CAP_下电重复性测试_T002_20260902_101002.csv",
      r"D:\Users\Share\实验室文件\4_VVC 集成电容验证\原始数据\D2-下电重复性\1500pF-1595837\VVC_VVC_CAP_下电重复性测试_T002_20260901_115922.csv",
      r"D:\Users\Share\实验室文件\4_VVC 集成电容验证\原始数据\D2-下电重复性\1500pF-1595846\VVC_VVC_CAP_下电重复性测试_T002_20260905_180129.csv",
      r"D:\Users\Share\实验室文件\4_VVC 集成电容验证\原始数据\D2-下电重复性\1500pF-1595846-复测\VVC_VVC_CAP_下电重复性测试_T002_20260908_093209.csv"
    ],
    "D3_DATA_LIST": [
      r"D:\Users\Share\实验室文件\4_VVC 集成电容验证\原始数据\D3-传动系统短稳定性\1500pF-1585902\VVC_VVC_传动系统短稳定测试_T003_20260806_170206.csv",
      r"D:\Users\Share\实验室文件\4_VVC 集成电容验证\原始数据\D3-传动系统短稳定性\1500pF-1595837\VVC_VVC_传动系统短稳定测试_T003_20260901_001103.csv",
      r"D:\Users\Share\实验室文件\4_VVC 集成电容验证\原始数据\D3-传动系统短稳定性\1500pF-1595846\VVC_VVC_传动系统短稳定测试_T003_20260903_050659.csv",
      r"D:\Users\Share\实验室文件\4_VVC 集成电容验证\原始数据\D3-传动系统短稳定性\1500pF-1595846-复测\VVC_VVC_传动系统短稳定测试_T003_20260907_233048.csv"
    ]
  }

  ORIGINAL_FILE_DIR_500 = {
    "D1_DATA_LIST": [
      r"\\10.21.234.127\实验室文件\4_VVC 集成电容验证\COMET测试\D1-不下电重复性\500pF-1718641\VVC_VVC_CAP_不下电重复性测试_T001_20260912_192423.csv"
    ],
    "D2_DATA_LIST": [
      r"\\10.21.234.127\实验室文件\4_VVC 集成电容验证\COMET测试\D2-下电重复性\500pF-1718641\VVC_VVC_CAP_下电重复性测试_T002_20260913_123503.csv"
    ],
    "D3_DATA_LIST": [
      r"\\10.21.234.127\实验室文件\4_VVC 集成电容验证\COMET测试\D3-传动系统稳定性\500pF-1718641\VVC_VVC_传动系统短稳定测试_T003_20260913_021211.csv"
    ]
  }

  # output_dir = r"D:\Users\Share\实验室文件\4_VVC 集成电容验证\原始数据\汇总-500.xlsx"
  output_dir = r"\\10.21.234.127\实验室文件\4_VVC 集成电容验证\汇总-500.xlsx"

  for test_type_name, live_data_dir_list in ORIGINAL_FILE_DIR_500.items():
    test_type_code = re.search(r"[A-Z]\d", test_type_name).group(0)
    for live_data_dir in live_data_dir_list:
      liveTest(live_data_dir, output_dir, test_type_code)
