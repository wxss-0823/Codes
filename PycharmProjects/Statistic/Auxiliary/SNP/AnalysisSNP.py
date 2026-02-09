#!D:\Users\Anaconda\anaconda3\python.exe
# -*- coding: utf-8 -*-
# @Time    : 2026/1/22 16:45
# @Author  : Coffee
# @Project : Auxiliary
# @File    : AnalysisSNP.py

import os

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import skrf as rf
import scipy.io as sio

SN = '2506210102-2'
snps_dir = rf'D:\Users\Wxss\01Project\01VVC\00Project\C-CapDecoupledTest260108\O-电容步进映射\{SN}'
fig_dir = r'D:\Users\Wxss\01Project\01VVC\00Project\C-CapDecoupledTest260108\O-电容步进映射\fig'
xlsxName = os.path.join(fig_dir, 'SNP DATA.xlsx')
# snps_dir = r'D:\Users\Wxss\01Project\01VVC\00Data\C-CapDecoupledTest260108\阻抗步进\SNP\2506210102'
snps = os.listdir(snps_dir)
snp_dirs = [os.path.join(snps_dir, snp) for snp in snps]

file_name_time_list = [(snp_dir, os.path.getmtime(snp_dir)) for snp_dir in snp_dirs]
file_sorted_list = sorted(file_name_time_list, key=lambda x: x[1])

N = len(snps)

# 目标频点
# f = np.array('13.56e6').astype(float)
f_str = '40.68e6'
# f_str = '81.36e6'
# f_str = '122.04e6'
f = np.array(f_str).astype(float)
nf = (f / 100000).astype(int)
z0 = 50.0
# 复阻抗数据
n = np.array([2 * i + 1 for i in range(N)])
s11 = np.zeros(shape=N, dtype=np.complex128)
s11a = np.zeros(shape=N, dtype=np.float64)
z = np.zeros(shape=N, dtype=np.complex128)
c = np.zeros(shape=N, dtype=np.float64)
r = np.zeros(shape=N, dtype=np.float64)
deltaC = np.zeros(shape=N, dtype=np.float64)

i = 0
for meta_file in file_sorted_list:

  # 读取snp文件
  network = rf.Network(meta_file[0])  # 1端口网络

  # 查看基本信息
  # freq = network.frequency.f
  s11[i] = network.s[nf, 0, 0]

  s11a[i] = 10 * np.log10(np.abs(s11[i]))

  z[i] = z0 * (1 + s11[i]) / (1 - s11[i])

  r[i] = z.real[i] * 1000

  c[i] = -1 / (2 * np.pi * f * z.imag[i]) * np.power(10, 12)

  if i >= 1:
    deltaC[i - 1] = z.imag[i] - z.imag[i - 1]

  i += 1

table = {
  'n': n,
  'Z': z.imag,
  'C': c,
  'deltaC': deltaC,
  'S11': s11a,
  'R': r
}

pd_snp = pd.DataFrame(table)
with pd.ExcelWriter(xlsxName, engine='openpyxl', mode='a', if_sheet_exists='replace') as writer:
  pd_snp.to_excel(writer, sheet_name=SN, index=False)

plt.figure(figsize=(8, 8), dpi=100, facecolor="w")
plt.subplot(2, 2, 1)
plt.plot(n, s11a)
plt.title('S11(log)')
plt.subplot(2, 2, 2)
plt.plot(n, z.imag)
plt.title('Z(imag)')

# plt.figure(figsize=(6, 6), dpi=100, facecolor="w")
plt.subplot(2, 2, 3)
plt.plot(n, c)
plt.title('C(pF)')

# plt.figure(figsize=(6, 6), dpi=100, facecolor="w")
plt.subplot(2, 2, 4)
plt.scatter(n, deltaC)
plt.grid(True, alpha=0.3, linestyle='--')
plt.title(r'deltaZ($\Omega$)')
plt.savefig(os.path.join(fig_dir, f'{f_str}_SNP_{SN}.png'))
plt.show()

# plt.figure(figsize=(6, 6), dpi=100, facecolor="w")
# plt.scatter(n, r)
# plt.title(r'R(m$\Omega$)')
# plt.show()

plt.figure(figsize=(6, 6), dpi=100, facecolor="w")
plt.plot(r[800:1200])
plt.title(r'R(m$\Omega$)')
plt.show()

step = np.array([i for i in range(N*2)])
c_interpolation = np.zeros(shape=2*N, dtype=np.float64)
z_imag_interpolation = np.zeros(shape=2*N, dtype=np.float64)

for i in range(N-2):
  c_interpolation[2*i] = c[i]
  c_interpolation[2*i+1] = (c[i]+c[i+1])/2
  z_imag_interpolation[2*i] = z.imag[i]
  z_imag_interpolation[2*i+1] = (z.imag[i]+z.imag[i+1])/2

accu_c = {
  'Step': step,
  'C': c_interpolation,
  'Z': z_imag_interpolation
}


accu_c_pd = pd.DataFrame(accu_c)
accu_c_dir = os.path.join(fig_dir, f"{f_str}_accC.xlsx")
if os.path.exists(accu_c_dir):
  with pd.ExcelWriter(accu_c_dir, engine='openpyxl', mode='a', if_sheet_exists='replace') as writer:
    accu_c_pd.to_excel(writer, sheet_name=SN, index=False)
else:
  with pd.ExcelWriter(accu_c_dir, engine='openpyxl', mode='w') as writer:
    accu_c_pd.to_excel(writer, sheet_name=SN, index=False)

