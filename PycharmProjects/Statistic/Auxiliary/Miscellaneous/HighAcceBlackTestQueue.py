#!D:\Users\Anaconda\anaconda3\python.exe
# -*- coding: utf-8 -*-
# @Time    : 2026/9/17 9:36
# @Author  : Coffee
# @Project : Miscellaneous
# @File    : HighAcceBlackTestQueue.py

import re
from datetime import datetime

import seaborn as sns
from dtaidistance import dtw
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker


# 需要读取的列
# file_dir = r"C:\Users\w00025121\AppData\Roaming\WeLink\appdata\IM\4n4380e0ifp1@cff7b52b3\DownloadFiles\速度控制电容测试序列_50to500_20260917_094137.csv"
# file_dir = r"C:\Users\w00025121\AppData\Roaming\WeLink\appdata\IM\4n4380e0ifp1@cff7b52b3\DownloadFiles\速度控制电容测试序列_50to500_20260916_173632.csv"
file_dir = r"C:\Users\w00025121\AppData\Roaming\WeLink\appdata\IM\4n4380e0ifp1@cff7b52b3\DownloadFiles\速度控制电容测试序列_50to500_20260922_101440.csv"
use_cols = ["Time", "testCount", "StepDiscription", "LCR_ActualCapacitancePicoF"]
test_type = ["Acc2Max", "Acc2Min", "Dec2Max", "Dec2Min"]
figs = []
figs_title = []

# 读取数据
v_ctrl_df = pd.read_csv(file_dir,
                        usecols=use_cols,
                        dtype={"Time": str,
                               "LCR_ActualCapacitancePicoF": np.float64},
                        encoding="gbk",
                        low_memory=False
                        )

# 清除 NAN
v_ctrl_df = v_ctrl_df.dropna(subset=["LCR_ActualCapacitancePicoF"])
v_ctrl_df = v_ctrl_df.reset_index(drop=True)

# 每次循环容值序列
start_pos, stop_pos = 0, -1
acc2max_list, acc2min_list = [], []
dec2max_list, dec2min_list = [], []
acc2max_time, acc2min_time = [], []
dec2max_time, dec2min_time = [], []

for i in range(len(v_ctrl_df)):
  if m:= re.search(r"向最[大小]值递[增减]", v_ctrl_df["StepDiscription"][i]):
    match m.group(0):
      # 匹配加速到最大容值
      case "向最小值递增":
        start_pos = stop_pos + 1
        stop_pos = i
        acc2max_list.append(v_ctrl_df["LCR_ActualCapacitancePicoF"][start_pos:stop_pos].tolist())
        acc2max_time.append(v_ctrl_df["Time"][start_pos:stop_pos].tolist())
      # 匹配加速到最小容值
      case "向最大值递减":
        start_pos = stop_pos + 1
        stop_pos = i
        acc2min_list.append(v_ctrl_df["LCR_ActualCapacitancePicoF"][start_pos:stop_pos].tolist())
        acc2min_time.append(v_ctrl_df["Time"][start_pos:stop_pos].tolist())
      # 匹配减速到最大容值
      case "向最小值递减":
        start_pos = stop_pos + 1
        stop_pos = i
        dec2max_list.append(v_ctrl_df["LCR_ActualCapacitancePicoF"][start_pos:stop_pos].tolist())
        dec2max_time.append(v_ctrl_df["Time"][start_pos:stop_pos].tolist())
      # 匹配减速到最小容值
      case "向最大值递增":
        start_pos = stop_pos + 1
        stop_pos = i
        if stop_pos == 0:
          continue
        dec2min_list.append(v_ctrl_df["LCR_ActualCapacitancePicoF"][start_pos:stop_pos].tolist())
        dec2min_time.append(v_ctrl_df["Time"][start_pos:stop_pos].tolist())
  if i == len(v_ctrl_df) - 1:
    dec2min_list.append(v_ctrl_df["LCR_ActualCapacitancePicoF"][stop_pos+1:-1])
    dec2min_time.append(v_ctrl_df["Time"][stop_pos+1:-1].tolist())

# 处理时间
test_num = len(acc2max_list)
for i in range(test_num):
  for j in range(len(acc2max_time[i])):
    acc2max_time[i][j] = datetime.strptime(acc2max_time[i][j][::-1].replace(":", ".", 1)[::-1], "%Y-%m-%d %H:%M:%S.%f").timestamp()
  for j in range(len(acc2min_time[i])):
    acc2min_time[i][j] = datetime.strptime(acc2min_time[i][j][::-1].replace(":", ".", 1)[::-1], "%Y-%m-%d %H:%M:%S.%f").timestamp()
  for j in range(len(dec2max_time[i])):
    dec2max_time[i][j] = datetime.strptime(dec2max_time[i][j][::-1].replace(":", ".", 1)[::-1], "%Y-%m-%d %H:%M:%S.%f").timestamp()
  for j in range(len(dec2min_time[i])):
    dec2min_time[i][j] = datetime.strptime(dec2min_time[i][j][::-1].replace(":", ".", 1)[::-1], "%Y-%m-%d %H:%M:%S.%f").timestamp()

  # 转 numpy 数组（可选）
  acc2max_time[i] = np.array(acc2max_time[i], dtype=np.float64)
  acc2min_time[i] = np.array(acc2min_time[i], dtype=np.float64)
  dec2max_time[i] = np.array(dec2max_time[i], dtype=np.float64)
  dec2min_time[i] = np.array(dec2min_time[i], dtype=np.float64)

  # 计算相对时间
  acc2max_time[i] = acc2max_time[i] - acc2max_time[i][0]
  acc2min_time[i] = acc2min_time[i] - acc2min_time[i][0]
  dec2max_time[i] = dec2max_time[i] - dec2max_time[i][0]
  dec2min_time[i] = dec2min_time[i] - dec2min_time[i][0]

# 画图
fig, ax = plt.subplots(2, 2, figsize=(8, 8))
for i in range(test_num):
  ax[0, 0].plot(acc2max_time[i], acc2max_list[i])
  ax[0, 1].plot(acc2min_time[i], acc2min_list[i])
  ax[1, 0].plot(dec2max_time[i], dec2max_list[i])
  ax[1, 1].plot(dec2min_time[i], dec2min_list[i])

ax[0, 0].set_title(test_type[0])
ax[0, 1].set_title(test_type[1])
ax[1, 0].set_title(test_type[2])
ax[1, 1].set_title(test_type[3])
fig.tight_layout()
figs.append(fig)
figs_title.append("速度调整时间序列")
# plt.show()
plt.close()

# 数据处理
acc2max_df = pd.DataFrame()
acc2min_df = pd.DataFrame()
dec2max_df = pd.DataFrame()
dec2min_df = pd.DataFrame()
group_list = [acc2max_list, acc2min_list, dec2max_list, dec2min_list]
min_len = min(len(sub) for group in group_list for sub in group)

# 数据拼接
temp_dict = {"acc2max": {}, "acc2min": {}, "dec2max": {}, "dec2min": {}}
for i in range(test_num):
  temp_dict["acc2max"][f"Time.N{i}"] = acc2max_time[i][:min_len]
  temp_dict["acc2max"][f"Test.N{i}"] = acc2max_list[i][:min_len]
  temp_dict["acc2min"][f"Time.N{i}"] = acc2min_time[i][:min_len]
  temp_dict["acc2min"][f"Test.N{i}"] = acc2min_list[i][:min_len]
  temp_dict["dec2max"][f"Time.N{i}"] = dec2max_time[i][:min_len]
  temp_dict["dec2max"][f"Test.N{i}"] = dec2max_list[i][:min_len]
  temp_dict["dec2min"][f"Time.N{i}"] = dec2min_time[i][:min_len]
  temp_dict["dec2min"][f"Test.N{i}"] = dec2min_list[i][:min_len]

# 存入 DF
acc2max_df = pd.DataFrame(temp_dict["acc2max"])
acc2min_df = pd.DataFrame(temp_dict["acc2min"])
dec2max_df = pd.DataFrame(temp_dict["dec2max"])
dec2min_df = pd.DataFrame(temp_dict["dec2min"])
data_list = [acc2max_df, acc2min_df, dec2max_df, dec2min_df]

# 截断至相同行
acc2max_head_df = acc2max_df.filter(like="Test.N").head(min_len)
acc2min_head_df = acc2min_df.filter(like="Test.N").head(min_len)
dec2max_head_df = dec2max_df.filter(like="Test.N").head(min_len)
dec2min_head_df = dec2min_df.filter(like="Test.N").head(min_len)

# 直接补 NAN 计算 Pearson 相关系数
acc2max_corr = acc2max_head_df.corr()
acc2min_corr = acc2min_head_df.corr()
dec2max_corr = dec2max_head_df.corr()
dec2min_corr = dec2min_head_df.corr()
corr_list = [acc2max_corr, acc2min_corr, dec2max_corr, dec2min_corr]


# 绘制相关系数热力图
fig, ax = plt.subplots(2, 2, figsize=(8, 8))
ax = ax.flatten()
for i, a in enumerate(ax):
  mask = np.triu(np.ones_like(corr_list[i], dtype=bool), k=1)
  ax = sns.heatmap(corr_list[i], mask=mask, ax=a,
              # vmin=corr_list[i].min().min(),
              # vmax=corr_list[i].max().max(),
              cmap="coolwarm",
              square=True,
              cbar_kws={"shrink": 0.7},
              xticklabels=False, yticklabels=False)
  cbar = ax.collections[0].colorbar
  cbar.ax.yaxis.set_major_formatter(ticker.FormatStrFormatter("%.5f"))
  cbar.ax.yaxis.get_offset_text().set_visible(False)
  a.set_title(f"{test_type[i]} CORR HeatMap")
fig.tight_layout()
figs.append(fig)
figs_title.append("互相关系数热力图")
plt.close()
# plt.show()

# 动态时间规整----以第一次测试数据为基准
dists = {}
path = {}
for vtype in test_type:
  dists[vtype] = []
  path[vtype] = []

# 计算时间轴伸缩对齐时间----数据对齐总距离 d & 数据对齐路径 p
window = 2
for i, data in enumerate(data_list):
  base_v = np.asarray(data["Test.N0"])
  for j in range(test_num - 1):
    d = dtw.distance(
      base_v,
      np.asarray(data["Test.N" + str(j + 1)]),
      window=window
    )
    p = dtw.warping_path(
      base_v,
      np.asarray(data["Test.N" + str(j + 1)]),
      window=window
    )
    dists[test_type[i]].append(d)
    path[test_type[i]].append(p)

# 绘制 DTW 时间规整总距离
fig, ax = plt.subplots(2, 2, figsize=(8, 8))
ax = ax.flatten()
for i, a in enumerate(ax):
  a.scatter(np.linspace(1, len(dists[test_type[i]]), len(dists[test_type[i]])), dists[test_type[i]])
  a.set_title(f"{test_type[i]} DTW Num Distance")
fig.tight_layout()
figs.append(fig)
figs_title.append("动态时间规整——点数距离")
plt.close()
# plt.show()

# 绘制 DTW 时间规整后的时间差
fig, ax = plt.subplots(2, 2, figsize=(8, 8))
ax = ax.flatten()
time_dist = []
for i, a in enumerate(ax):
  data = data_list[i]
  base_t = np.asarray(data["Time.N0"])
  for n, p in enumerate(path[test_type[i]]):
    t_d = []
    t = []
    for j, k in p:
      t_d.append(base_t[j] - data[f"Time.N{n}"].iloc[k])
      t.append(base_t[j])
      # if t_d[-1] > 10:
      #   print(i, n, j, k, base_t[j], data[f"Time.N{n}"].iloc[k], t_d[-1])
      #   break
    a.plot(t, t_d)
  a.set_title(f"{test_type[i]} DTW Time Distance")
fig.tight_layout()
figs.append(fig)
figs_title.append("动态时间规整——时间距离")
plt.close()
# plt.show()

# # 保存图片
for i, fig in enumerate(figs):
  fig.savefig(rf"\\10.21.234.127\实验室文件\6_速度控制_20260909\黑盒测试\{figs_title[i]}.png")

# 对齐路径
# num_a = 0
# num_b = 198
# type_idx = 2
# data_df = data_list[type_idx]
# path = dtw.warping_path(data_df[f"Test.N{num_a}"], data_df[f"Test.N{num_b}"])
#
# plt.figure(figsize=(8, 8))
# plt.plot(data_df[f"Time.N{num_a}"], data_df[f"Test.N{num_a}"], label=f"{test_type[type_idx]}.N{num_a}")
# plt.plot(data_df[f"Time.N{num_b}"], data_df[f"Test.N{num_b}"], label=f"{test_type[type_idx]}.N{num_b}")
# for i, j in path:
#     plt.plot([data_df[f"Time.N{num_a}"][i], data_df[f"Time.N{num_b}"][j]], [data_df[f"Test.N{num_a}"][i], data_df[f"Test.N{num_b}"][j]],
#               color="gray", alpha=0.3)
# plt.legend()
# plt.show()

