#!D:\Users\Anaconda\anaconda3\python.exe
# -*- coding: utf-8 -*-
# @Time    : 2026/1/26 10:19
# @Author  : Coffee
# @Project : Auxiliary
# @File    : ESR-F.py


import os

import matplotlib.pyplot as plt
import numpy as np
import scipy.io as sio
import skrf as rf

SN = '2506210102-2'
snps_dir = rf'D:\Users\Wxss\01Project\01VVC\00Project\C-CapDecoupledTest260108\O-电容步进映射\{SN}'
fig_dir = r'D:\Users\Wxss\01Project\01VVC\00Project\O-电容步进映射\fig'
xlsxName = os.path.join(fig_dir, 'SNP DATA.xlsx')
# snps_dir = r'D:\Users\Wxss\01Project\01VVC\00Data\C-CapDecoupledTest260108\阻抗步进\SNP\2506210102'
snps = os.listdir(snps_dir)
snp_dirs = [os.path.join(snps_dir, snp) for snp in snps]

file_name_time_list = [(snp_dir, os.path.getmtime(snp_dir)) for snp_dir in snp_dirs]
file_sorted_list = sorted(file_name_time_list, key=lambda x: x[1])

z0 = 50.0
plt.figure(figsize=(6, 6), dpi=100, facecolor="w")

R = np.zeros((len(snp_dirs), 2000))

i = 0
for meta_file in file_sorted_list:

  # 读取snp文件
  network = rf.Network(meta_file[0])  # 1端口网络
  # network = rf.Network(file_sorted_list[0][0])  # 1端口网络

  # 查看基本信息
  freq = network.frequency.f

  s11 = network.s[:, 0, 0]

  z = z0 * (1 + s11) / (1 - s11)

  r = z.real

  R[i,:] = r
  i += 1

  plt.plot(freq[251:], r[251:])
  plt.title('R')

plt.show()

# Export
R_mat = np.array(R)
R_dict = {"R": R_mat}
sio.savemat("R.mat", R_dict)
