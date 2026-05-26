#!D:\Users\Anaconda\anaconda3\python.exe
# -*- coding: utf-8 -*-
# @Time    : 2026/3/23 17:32
# @Author  : Coffee
# @Project : ReferanceV3.py
# @File    : SGReader.py

import os

import time
from datetime import datetime
import re
import matplotlib.pyplot as plt
import numpy as np


sg_dir = r"D:\Users\Share\实验室文件\3_VVC 寿命测试\高加速度测试_20260316\0.2Nm\SN_260302\20260511\SG"
sg_ptn = r"\d+"
sg_list = list()
timestamp = time.time()
dt = datetime.fromtimestamp(timestamp)
fmt = "%Y_%#m_%d-%H_%M_%S"
# 筛选日期
dt_ptn = dt.strftime("%Y_%#m_%d")
# dt_ptn = "2026_3_23"
fmt_dt = dt.strftime(fmt)


for root_dir, sub_dir, files in os.walk(sg_dir):
  plt.rcParams['font.sans-serif'] = ['SimHei']
  fig, ax = plt.subplots(figsize=(60, 30), dpi=100, facecolor="w")
  plt.title(r"3次SG测试", fontsize=60)
  fig_idx = 1
  for file in files:
    if file.endswith("DAT") and re.search(dt_ptn, file):
      file_path = os.path.join(sg_dir, file)
      with open(file_path, 'r', encoding="utf-8") as f:
        for line in f:
          if re.match(sg_ptn, line):
            sg_list.append(int(re.match(sg_ptn, line).group(0)))

      # half_pos = int(len(sg_list)/2)
      half_pos = 5000
      n_ticks = (6, 5)
      font_size = (40, 40)

      ax.set_xlim(0, half_pos)
      ax.set_ylim(-10, max(sg_list)+25)
      ax.scatter([i for i in range(half_pos)], sg_list[:half_pos], s=100, marker='.', label=f"第{fig_idx}次")

      y_min, y_max = ax.get_ylim()
      x_min, x_max = ax.get_xlim()
      x_ticks = np.linspace(x_min, x_max, n_ticks[0])
      y_ticks = np.linspace(y_min + 10, y_max, n_ticks[1])

      ax.set_xticks(x_ticks)
      ax.set_yticks(y_ticks)
      ax.set_xticklabels(ax.get_xticks(), fontsize=font_size[0])
      ax.set_yticklabels(ax.get_yticks(), fontsize=font_size[1])


      fig_idx += 1
      sg_list = []

  ax.legend(loc="upper right", fontsize=40)
  plt.savefig(os.path.join(sg_dir, f"3次SG测试_{fmt_dt}"))
  # plt.show()