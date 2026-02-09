#!D:\Users\Anaconda\anaconda3\python.exe
# -*- coding: utf-8 -*-
# @Time    : 2026/1/29 11:05
# @Author  : Coffee
# @Project : Auxiliary
# @File    : FindZeroJump.py


import os

import pandas as pd
import matplotlib.pyplot as plt

file_dir = r"D:\Users\Wxss\bin\WeLink\DownloadFiles\2506210105_3-30pf\Unknown_SN_硬件初始化_20260116_123341"
origin_find_zero_file = os.path.join(file_dir, "Unknown_SN_测试数据.xlsx")
error_info_file = os.path.join(file_dir, "error_info.xlsx")
cap_df = pd.DataFrame()
error_info = pd.DataFrame()
deltaC_tolerance = -0.3
df_index = 0

for i in range(100):
  sheet_name = f"硬件测试{i+1}_电容值"
  cap_df = pd.read_excel(origin_find_zero_file, sheet_name=sheet_name, usecols="A:B")
  cap_df.columns = ["TIME", "CAP"]
  (row, col) = cap_df.shape
  for j in range(row-1):
    deltaC = cap_df["CAP"][j+1] - cap_df["CAP"][j]
    if deltaC < deltaC_tolerance and 25 < cap_df["CAP"][j] < 27:

      error_info.loc[df_index, "sheet N"] = i+1
      error_info.loc[df_index, "time"] = cap_df["TIME"][j]
      error_info.loc[df_index, "CAP1"] = cap_df["CAP"][j]
      error_info.loc[df_index, "CAP2"] = cap_df["CAP"][j+1]
      error_info.loc[df_index, "deltaC"] = deltaC
      error_info.loc[df_index, "sheet row"] = j + 2
      df_index += 1
      break

# Sort with sheet N in ascending order
error_info.sort_values(by="sheet N")
with pd.ExcelWriter(error_info_file, engine='openpyxl', mode='a', if_sheet_exists='replace') as writer:
  error_info.to_excel(writer, sheet_name="accu", index=False, header=True)


plt.figure(figsize=(8,8), dpi=100, facecolor="white")
plt.subplot(2, 2, 1)
plt.title("100 Zero-Time(s)")
plt.scatter(error_info["sheet N"], error_info["time"])
plt.subplot(2, 2, 2)
plt.title("CAP Burst(pF)")
plt.scatter(error_info["sheet N"], error_info["CAP1"], label="CAP1")
plt.scatter(error_info["sheet N"], error_info["CAP2"], label="CAP2")
plt.legend(loc="best")
plt.subplot(2, 2, 3)
plt.title("Delta Cap(pF)")
plt.scatter(error_info["sheet N"], error_info["deltaC"])
plt.subplot(2, 2, 4)
plt.title("The Nth sheet row")
plt.scatter(error_info["sheet N"], error_info["sheet row"])
plt.savefig(os.path.join(file_dir, "error_info.png"))
plt.show()
