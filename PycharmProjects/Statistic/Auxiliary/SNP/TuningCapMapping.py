#!D:\Users\Anaconda\anaconda3\python.exe
# -*- coding: utf-8 -*-
# @Time    : 2026/2/3 16:21
# @Author  : Coffee
# @Project : Auxiliary
# @File    : TuningCapMapping.py

import os

import pandas as pd
import numpy as np
import math
import scipy.io as sio
from numpy.ma.core import shape

file_dir = r"D:\Users\Wxss\bin\WeLink\DownloadFiles\谐波调控验证数据处理.xlsx"

process_data = pd.DataFrame()
origin_data_pd = pd.read_excel(file_dir, sheet_name='C3-Zin', usecols='A:E')

origin_data_pd.columns = ['A', 'B', 'C', 'D', 'E']
origin_data_pd = origin_data_pd.drop([0])
origin_data_pd = origin_data_pd.dropna(subset=['A', 'B', 'D', 'E'])

row = origin_data_pd['A'].size
step01 = np.zeros(shape=row, dtype=np.float64)
Z01 = np.zeros(shape=row, dtype=np.float64)

for i in range(1, row):
  step01[i-1] = origin_data_pd['A'][i]
  Z01[i-1] = origin_data_pd['B'][i]

row = origin_data_pd['D'].size
step02 = np.zeros(shape=row, dtype=np.float64)
Z02 = np.zeros(shape=row, dtype=np.float64)

for i in range(1, row):
  step02[i-1] = origin_data_pd['D'][i]
  Z02[i-1] = origin_data_pd['E'][i]


step_begin = 450
step_end = 700
sample_num = step_end - step_begin + 1
cap_begin = 4.5
cap_end = 7
step = np.array([i for i in range(step_begin, step_end)])

upper_percent_table = np.round([100/(sample_num-1) * i for i in range(sample_num)], 4)
cap_table = np.round([(cap_end - cap_begin)/(sample_num-1) * i + cap_begin for i in range(sample_num)], 4)
golden_step_table = np.round([(step_end - step_begin)/(sample_num-1) * i + step_begin for i in range(sample_num)], 4)

init_delta_z = abs(Z02[0] - Z01)
index_delta_z = np.zeros(shape=(1, step01.size), dtype=np.float64)

curvature = 1

for i in range(step01.size):
  for j in range(1, step02.size):
    if abs(Z02[j] - Z01[i]) < init_delta_z[i]:
      init_delta_z[i] = abs(Z02[j] - Z01[i])
      index_delta_z[0][i] = j
      curvature =

    elif abs(j - index_delta_z[0][0]) >= 5:
      init_delta_z[i] = abs(Z02[0] - Z01[i])
      index_delta_z[0][i] = 0
    else:
      break


print(index_delta_z)










process_data['Step01'] = step01
process_data['Z01'] = Z01
process_data['Step02'] = step02
process_data['Z02'] = Z02

sio.savemat('process_data.mat', mdict={'process_data': process_data})







