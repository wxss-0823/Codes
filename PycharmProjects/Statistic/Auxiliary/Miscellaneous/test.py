#!D:\Users\Anaconda\anaconda3\python.exe
# -*- coding: utf-8 -*-
# @Time    : 2026/9/2 10:03
# @Author  : Coffee
# @Project : Miscellaneous
# @File    : test.py


import os
import sys
import re
import io

import pandas as pd
import numpy as np
from narwhals import concat

# 读取数据
file_dir = r"C:\Users\w00025121\Desktop\temp"
tar_dir = r"C:\Users\w00025121\Desktop\temp\VVC_VVC_CAP_下电重复性测试_T002_20260902_101002.csv"
poo_data = pd.DataFrame()
live_test_data = pd.DataFrame()
for dir in next(os.walk(file_dir))[2]:
  print(dir)
  poo_data = pd.read_csv(os.path.join(file_dir, dir), encoding='gbk')
  # 清除 NAN
  poo_data = poo_data.dropna(subset=['LCR_ActualCapacitancePicoF'])
  poo_data = poo_data.reset_index(drop=True)
  live_test_data = pd.concat([live_test_data, poo_data])

live_test_data.to_csv(tar_dir, index=False, encoding='gbk')

