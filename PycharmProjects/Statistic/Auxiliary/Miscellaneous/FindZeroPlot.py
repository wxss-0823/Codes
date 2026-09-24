#!D:\Users\Anaconda\anaconda3\python.exe
# -*- coding: utf-8 -*-
# @Time    : 2026/9/9 19:01
# @Author  : Coffee
# @Project : Miscellaneous
# @File    : FindZeroPlot.py
from os.path import exists

import pandas as pd
import matplotlib.pyplot as plt
import re
import numpy as np

# 读取整个Excel文件
# file_path = r"\\10.21.234.127\实验室文件\6_快速电容_20260909\找零异常\origin\2511031505复测500次-TH2840_水平测试数据.xlsx"
# file_path = r"C:\Users\w00025121\AppData\Roaming\WeLink\appdata\IM\4n4380e0ifp1@cff7b52b3\DownloadFiles\2511031510复测_测试数据.xlsx"
# file_path = r"\\10.21.234.127\实验室文件\7_滚珠电容_20260909\找零异常\origin\2511031505复测500次-TH2838_垂直测试数据.xlsx"
file_path = r"\\10.21.234.127\实验室文件\7_滚珠电容_20260909\找零异常\origin\2511031505_TH2840_增加找零电流_测试数据.xlsx"
find_zero_file = pd.ExcelFile(file_path)
sheet_names = find_zero_file.sheet_names
read_sheet_list = []

# 筛选 sheet 文件名
sheet_name_ptn = r"硬件测试\d+_电容值"
for sheet_name in sheet_names:
  if re.match(sheet_name_ptn, sheet_name):
    read_sheet_list.append(sheet_name)

data_dict = pd.read_excel(find_zero_file, sheet_name=read_sheet_list)
data_all_df = pd.DataFrame()

idx = 0
columns_to_concat = []

for sheet_name in read_sheet_list:
  df = data_dict[sheet_name]
  if idx == 0:
    columns_to_concat.append(df.iloc[:, 0].rename(f"时间/s"))
    idx +=1
  columns_to_concat.append(df.iloc[:, 1].rename(f"找零测试{idx}/pF"))
  idx += 1
data_all_df = pd.concat(columns_to_concat, axis=1)

with pd.ExcelWriter(r"\\10.21.234.127\实验室文件\7_滚珠电容_20260909\找零异常\找零数据合并.xlsx", engine='openpyxl', mode='a',
                    if_sheet_exists='replace') as writer:
  data_all_df.to_excel(writer, sheet_name='垂直合并-增大电流', index=False)

find_zero_file.close()

t = data_all_df.iloc[:, 0]

mech_zero = []
fig, axes = plt.subplots(figsize=(16, 8), dpi=300)
for i in range(1, len(data_all_df.columns)):
  y = data_all_df.iloc[:, i]
  plt.plot(t, y, linewidth=2)
  mech_zero.append(np.min(y))

plt.xlabel("Sample/s")
plt.ylabel('Cap/pF')
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig(r"\\10.21.234.127\实验室文件\7_滚珠电容_20260909\找零异常\origin\TH2840-垂直-增大电流.png")
plt.close()
# plt.show()

fig, axes = plt.subplots(figsize=(16, 8), dpi=300)
plt.plot(mech_zero)
plt.show()
