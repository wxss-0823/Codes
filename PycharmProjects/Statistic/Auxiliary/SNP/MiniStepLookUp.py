#!D:\Users\Anaconda\anaconda3\python.exe
# -*- coding: utf-8 -*-
# @Time    : 2026/2/9 15:25
# @Author  : Coffee
# @Project : Auxiliary
# @File    : MiniStepLookUp.py


import os

import pandas as pd
import numpy as np
from matplotlib import pyplot as plt


full_step_file = r"D:\Users\Wxss\01Project\01VVC\00Project\C-整步测试260108\C-电容步进映射\fig\40.68e6_accC.xlsx"
mini_step_file = r"D:\Users\Wxss\01Project\01VVC\00Project\O-微步测试260205\fig\40.68e6_accC.xlsx"

full_step_df = pd.read_excel(full_step_file, sheet_name="table", usecols="A:H")
cols = full_step_df["Step1"].size
temp_z = np.zeros(shape=cols, dtype=np.float64)

for i in range(0, cols):
  for j in range(0, cols-1):
    if full_step_df["Z2（Golden）"][j] > full_step_df["Z1（Test）"][i] > full_step_df["Z2（Golden）"][j+1]:
      full_step_df.loc[i, "实际全步"] = ((full_step_df["Z1（Test）"][i] - full_step_df["Z2（Golden）"][j+1]) /
        (full_step_df["Z2（Golden）"][j] - full_step_df["Z2（Golden）"][j+1]) +
        full_step_df["Step2"][i])
      break
    elif full_step_df["Z2（Golden）"][j] < full_step_df["Z1（Test）"][i] < full_step_df["Z2（Golden）"][j+1]:
      full_step_df.loc[i, "实际全步"] = ((full_step_df["Z1（Test）"][i] - full_step_df["Z2（Golden）"][j+1]) /
        (full_step_df["Z2（Golden）"][j] - full_step_df["Z2（Golden）"][j+1]) +
        full_step_df["Step2"][i])
      break

full_step_df["实际微步"] = full_step_df["实际全步"] * 16
full_step_df["下发微步"] = round(full_step_df["实际微步"])

mini_step_df = pd.read_excel(mini_step_file, sheet_name="绝对步进表", usecols="A:D")
test_init_full_step = 454
for i in range(0, cols):
  try:
    mini_idx = full_step_df["下发微步"][i] - test_init_full_step * 16
    full_step_df.loc[i, "LOOK UP"] = mini_step_df["Z"][int(mini_idx)]
  except KeyError:
    print("Test Capacitor range is limited.")
    break

full_step_df["LOOK DIFF AFTER INTERLOPATION"] = full_step_df["Z2（Golden）"] - full_step_df["LOOK UP"]
full_step_df["LOOK DIFF BEFORE INTERLOPATION"] = full_step_df["Z2（Golden）"] - full_step_df["Z1（Test）"]
plt_len = full_step_df["LOOK DIFF AFTER INTERLOPATION"].count()

full_step_df.loc[0, "Statistic After"] = full_step_df["LOOK DIFF AFTER INTERLOPATION"].mean()
full_step_df.loc[1, "Statistic After"] = full_step_df["LOOK DIFF AFTER INTERLOPATION"].std()
full_step_df.loc[0, "Statistic Before"] = full_step_df["LOOK DIFF BEFORE INTERLOPATION"][0:plt_len].mean()
full_step_df.loc[1, "Statistic Before"] = full_step_df["LOOK DIFF BEFORE INTERLOPATION"][0:plt_len].std()

plt.figure(figsize=(6, 6), dpi=100, facecolor="w")
plt.subplot(2, 1, 1)
# plt.title("LOOK DIFF BEFORE INTERLOPATION")
plt.xlabel("Step")
plt.ylabel("DIFF BEFORE")
plt.scatter(full_step_df["下发微步"][0:plt_len], full_step_df["LOOK DIFF BEFORE INTERLOPATION"][0:plt_len])
plt.subplot(2, 1, 2)
# plt.title("LOOK DIFF AFTER INTERLOPATION")
plt.xlabel("Step")
plt.ylabel("DIFF AFTER")
plt.scatter(full_step_df["下发微步"], full_step_df["LOOK DIFF AFTER INTERLOPATION"])
plt.savefig(os.path.join(r"D:\Users\Wxss\01Project\01VVC\00Project\C-整步测试260108\C-电容步进映射\fig", "DIFF FIG.png"), dpi=100)
plt.show()


with pd.ExcelWriter(full_step_file, mode="a", engine="openpyxl", if_sheet_exists="replace") as writer:
  full_step_df.to_excel(writer, sheet_name="table1", index=False)