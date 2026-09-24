#!D:\Users\Anaconda\anaconda3\python.exe
# -*- coding: utf-8 -*-
# @Time    : 2026/9/8 15:07
# @Author  : Coffee
# @Project : Miscellaneous
# @File    : SGReader_Raw.py


import os

import time
from datetime import datetime
import re
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import FindZeroPlot

sg_dir = r"\\10.21.234.127\实验室文件\7_滚珠电容_20260909\找零异常\origin"
# file_path = os.path.join(sg_dir, r"ReceivedTofile-COM34-2026_9_9_18-00-16.DAT")
file_path = os.path.join(sg_dir, r"ReceivedTofile-COM34-2026_9_9_18-00-16.DAT")
sg_ptn = r"^[0-9A-Fa-f]+$"  # 仅匹配HEX数
init_ptn = r"ECS_VVC_APP_CapMonitorInit"
sg_list = list()
multi_sg = dict()
sg_n = 0
timestamp = time.time()
dt = datetime.fromtimestamp(timestamp)
fmt = "%Y_%#m_%d-%H_%M_%S"
# 筛选日期
# dt_ptn = dt.strftime("%Y_%#m_%d").replace('-0', '-')
dt_ptn = "2026_6_13"

fmt_dt = dt.strftime(fmt)

# for root_dir, sub_dir, files in os.walk(sg_dir):
fig_idx = 1
peek_avg_list = []

# for file in next(os.walk(sg_dir))[1]:
#   if file.endswith("txt") or file.endswith("DAT"):
#     file_path = os.path.join(sg_dir, file)
with open(file_path, 'r', encoding="utf-8", errors="ignore") as f:
  for line_num, line in enumerate(f, 1):
    if re.search(init_ptn, line) and sg_list:
      # print(line_num)
      multi_sg[sg_n] = sg_list.copy()
      sg_list.clear()
      sg_n = sg_n + 1
    elif re.match(sg_ptn, line):
      # print(line)
      hex_data = re.match(sg_ptn, line).group(0)
      dec_data = int(hex_data, 16)
      bin_data = bin(dec_data)[2:].zfill(20)
      bin_data = bin_data[::-1]  # 反转bit序列
      dec_splt_data = int(bin_data[10:20], 2)
      sg_list.append(dec_splt_data)

# plt.rcParams['font.sans-serif'] = ['SimHei']
fig, ax = plt.subplots(figsize=(60, 30), dpi=300, facecolor="w")
plt.title(r"SG Test", fontsize=100)

# half_pos = int(len(sg_list) / 2)
half_pos = 6000
first_peek_len = 1000
n_ticks = (6, 5)
font_size = (50, 50)

# 设置坐标轴上下限
ax.set_xlim(0, half_pos)
ax.set_ylim(-10, max(sg_list) + 25)

# 绘制图像
for i in range(len(multi_sg)):
  y_list = multi_sg[i]
  x_list = np.linspace(0, len(y_list), len(y_list))
  sg = [i for i in y_list[1200:2001] if 0 <= i <= 120][:501]
  ax.scatter(x_list, y_list, s=300, marker='.', label=f"{fig_idx}")
  peek_avg_list.append(np.around(np.mean(sg), 2))
  fig_idx += 1

ax.legend(loc="upper right", fontsize=40)

# 计算坐标轴标签x
y_min, y_max = ax.get_ylim()
x_min, x_max = ax.get_xlim()
x_ticks = np.around(np.linspace(x_min, x_max, n_ticks[0]))
y_ticks = np.around(np.linspace(y_min + 10, y_max, n_ticks[1]))

# 设置坐标轴标签及字体大小
ax.set_xticks(x_ticks)
ax.set_yticks(y_ticks)
ax.set_xticklabels(ax.get_xticks(), fontsize=font_size[0])
ax.set_yticklabels(ax.get_yticks(), fontsize=font_size[1])

# 设置图像边框粗细
board_width = 4
ax.spines['top'].set_linewidth(board_width)  # 上边框
ax.spines['bottom'].set_linewidth(board_width)  # 下边框（x 轴）
ax.spines['left'].set_linewidth(board_width)  # 左边框（y 轴）
ax.spines['right'].set_linewidth(board_width)  # 右边框
plt.savefig(os.path.join(sg_dir, f"SG Test_{fmt_dt}"))
plt.close()

# 读取数据
preset_df = pd.read_excel(FindZeroPlot.file_path, sheet_name="测试结果汇总")
preset_list = preset_df.iloc[:, 2]
corr_matrix = np.corrcoef(preset_list[-1-len(peek_avg_list):-1], peek_avg_list)
print(f"SG & PRESET 相关系数：{corr_matrix[0, 1]}")
# 绘制左 Y 轴
fig, ax1 = plt.subplots(figsize=(10, 6), dpi=300, facecolor="w")
color1 = 'tab:blue'
ax1.set_ylabel('SG', color=color1)
ax1.plot(np.linspace(0, len(peek_avg_list), len(peek_avg_list)), peek_avg_list, '.-', color=color1, label="sg_avg")
ax1.tick_params(axis='y', labelcolor=color1)
# 绘制右 Y 图
color2 = 'tab:red'
ax2 = ax1.twinx()
ax2.set_ylabel('PRESET', color=color2)
ax2.plot(preset_df.iloc[:, 0], preset_list, '.-', color=color2, label="preset")
ax2.tick_params(axis='y', labelcolor=color2)

# 合并图例
lines1, labels1 = ax1.get_legend_handles_labels()
lines2, labels2 = ax2.get_legend_handles_labels()
plt.legend(lines1 + lines2, labels1 + labels2, loc="upper right")
# 保存图像
plt.title("SG AVG & PRESET")
plt.tight_layout()
plt.savefig(os.path.join(sg_dir, f"SG AVG & PRESET 垂直{fmt_dt}"))
plt.close()
