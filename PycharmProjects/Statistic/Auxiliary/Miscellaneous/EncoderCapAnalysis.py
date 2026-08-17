#!D:\Users\Anaconda\anaconda3\python.exe
# -*- coding: utf-8 -*-
# @Time    : 2026/7/1 20:46
# @Author  : Coffee
# @Project : Pycharm
# @File    : EncoderCapAnalysis.py

import pandas as pd
import matplotlib.pyplot as plt
from scipy.constants import micro

micro_step = 256
pulse_threshold = 1.5

# pct5_file_path = r"C:\Users\w00025121\Desktop\COMET编码器电容竞分\RefCurve_2026-07-01_3_195243.Wfm.csv"
pct5_file_path = r"C:\Users\w00025121\Desktop\COMET编码器电容竞分\RefCurve_5%Range_2026-07-01_4_195536.Wfm.csv"
# pct5_file_path = r"C:\Users\w00025121\Desktop\COMET编码器电容竞分\RefCurve_1%Range_2026-07-02_1_084848.Wfm.csv"
pct5_df = pd.read_csv(
  pct5_file_path,
  delimiter=';',
  header=None
)
pct5_df.columns = ["Time", "Voltage"]
pct5_len = len(pct5_df["Time"])

trigger_flag = 0
pos_edge_num = 0
neg_edge_num = 0
pos_edge_t_list = []
micro_step_time_list = []
micro_step_freq_list = []
micro_step_freq_acc_list = []  # 单位：Hz/s
for i in range(pct5_len):
  if pct5_df["Voltage"][i] > pulse_threshold and trigger_flag == 0:
    trigger_flag = 1
    pos_edge_num += 1
    pos_edge_t_list.append(pct5_df["Time"][i])

  if pct5_df["Voltage"][i] < pulse_threshold and trigger_flag == 1:
    trigger_flag = 0
    neg_edge_num += 1

  if pos_edge_num - 1 % micro_step == 0:
    micro_step_time_list.append(pct5_df["Time"][i])

for i in range(len(pos_edge_t_list) - 1):
  micro_step_freq_list.append(1 / (pos_edge_t_list[i + 1] - pos_edge_t_list[i]))
  if len(micro_step_freq_list) >= 2:
    micro_step_freq_acc_list.append((micro_step_freq_list[i] - micro_step_freq_list[i - 1]) / (pos_edge_t_list[i] - pos_edge_t_list[i - 1]))
full_step_freq_list = micro_step_freq_list[::micro_step]
full_step_pos_edge_t_list = pos_edge_t_list[::micro_step]
full_step_freq_acc_list = []
for i in range(len(full_step_freq_list) - 1):
  full_step_freq_acc_list.append((full_step_freq_list[i + 1] - full_step_freq_list[i]) /
  (full_step_pos_edge_t_list[i + 1] - full_step_pos_edge_t_list[i]))
acceleration = sum(full_step_freq_acc_list[:5])/5
max_speed = max(full_step_freq_list)

plt.figure(figsize=(6, 6), dpi=100, facecolor="w")
plt.title('1% Range Adjust Pulse Frequency')
plt.scatter(full_step_pos_edge_t_list, full_step_freq_list, label=f"Max Speed: {max_speed:.3e} Hz")
plt.legend(loc="upper right")
plt.figure(figsize=(6, 6), dpi=100, facecolor="w")
plt.title('1% Range Adjust Pulse Acceleration')
plt.scatter(full_step_pos_edge_t_list[:-1], full_step_freq_acc_list, label=f"Acceleration: {acceleration:.3e} Hz/s")
plt.legend(loc="upper right")
plt.show()

print(f"Acceleration: {sum(full_step_freq_acc_list[:5])/5} Hz/s")
print(f"Max Speed: {max(full_step_freq_list)} Hz")

