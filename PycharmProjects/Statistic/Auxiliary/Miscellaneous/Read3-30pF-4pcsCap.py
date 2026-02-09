#!D:\Users\Anaconda\anaconda3\python.exe
# -*- coding: utf-8 -*-
# @Time    : 2026/1/28 19:35
# @Author  : Coffee
# @Project : Auxiliary
# @File    : Read3-30pF-4pcsCap.py


import os

import pandas as pd
import scipy.io as sio
import numpy as np

file_dir = r"D:\Users\Wxss\01Project\01VVC\00Project\C-CapDecoupledTest260108\容值步进\30pF-4pcs"
write_dir = r"all_cap.xlsx"
xlsx_list: list[str] = []

# Get xlsx file directory
for root, dirs, files in os.walk(file_dir):
  for file in files:
    if file.endswith(".xlsx") and not file.startswith("~"):
      xlsx_list.append(os.path.join(root, file))

cap_df = pd.DataFrame()
cap_all_df = pd.DataFrame()
i = 0
for file in xlsx_list:
  cap_df = pd.read_excel(file, sheet_name="sheet1", usecols="B")
  cap_df.columns = ["C(pF)"]
  cap_df["C(pF)"] = pd.to_numeric(cap_df["C(pF)"], errors='coerce')
  cap_df = cap_df.drop([0, 1])
  cap_all_df.loc[:, i] = cap_df
  i += 1

# with pd.ExcelWriter(write_dir, engine='openpyxl', mode='a', if_sheet_exists='replace') as writer:
#   cap_all_df.to_excel(writer, sheet_name="all_cap", index=True)

all_cap = np.array(cap_all_df)
cap_mat = {"all_cap": all_cap}
sio.savemat("all_cap.mat", cap_mat)
