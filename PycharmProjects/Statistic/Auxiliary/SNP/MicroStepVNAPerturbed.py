#!D:\Users\Anaconda\anaconda3\python.exe
# -*- coding: utf-8 -*-
# @Time    : 2026/2/24 15:36
# @Author  : Coffee
# @Project : Auxiliary
# @File    : MicroStepVNAPerturbed.py

import os

import pandas as pd
import skrf as srf
import numpy as np
import matplotlib.pyplot as plt
import re

def microStepVNAPerturbed(
    micro_step,
    file_name,
    save_dir,
    file_dir,
    start_step = 0,
    f = 40.68e6,
):
  s_df = pd.DataFrame()
  z_df = pd.DataFrame()
  z0 = 50.0
  i = 1
  nf = int(f / 100e3)
  match_ptn = rf"{micro_step}"
  for root, dirs, files in os.walk(file_dir):
      for file in files:
        if file.endswith(".s1p") and re.search(match_ptn, file):
          network = srf.Network(os.path.join(root, file))
          freq = network.frequency.f[start_step:]
          s11 = network.s[start_step:, 0, 0]

          s_df.loc[:, 0] = freq
          s_df.loc[:, i] = np.abs(s11)
          z_df.loc[:, 0] = freq
          z_df.loc[:, i] = (z0 * (1 + s11) / (1 - s11)).imag
          i = i + 1

  xlsx_file_dir = os.path.join(save_dir, "MicroStepVNAPerturbed.xlsx")
  with pd.ExcelWriter(xlsx_file_dir, engine='openpyxl', mode='a', if_sheet_exists='replace') as writer:
    s_df.to_excel(writer, sheet_name=f'{file_name}-{micro_step}-s11', index=False)
    z_df.to_excel(writer, sheet_name=f'{file_name}-{micro_step}-z', index=False)

  fig, axes = plt.subplots(2, 2, figsize=(8, 8))
  ax1 = axes[0, 0]
  for i in range(s_df.shape[1]-1):
    ax1.plot(s_df.loc[:, 0], s_df.loc[:, i+1])
  ax1.set_title('S11(mag)')
  ax1.grid(True)
  ax1.ticklabel_format(style='sci', axis='both', scilimits=(0, 0))

  ax2 = axes[0, 1]
  for i in range(s_df.shape[1]-1):
    ax2.plot(z_df.loc[:, 0], z_df.loc[:, i+1])
  ax2.set_title(r'Imag Z($\Omega$)')
  ax2.grid(True)
  ax2.ticklabel_format(style='sci', axis='both', scilimits=(0, 0))

  abs_diff_dev = np.array([])
  rel_diff_dev = np.array([])
  for i in range(s_df.shape[0]):
    row = z_df.iloc[i, 1:]
    abs_diff_dev = np.append(abs_diff_dev, max(row)-min(row))
    rel_diff_dev = np.append(rel_diff_dev, (max(row)-min(row))/abs(max(row)))

  n = np.array([i for i in range(len(abs_diff_dev))])
  ax3 = axes[1, 0]
  ax3.scatter(n, abs_diff_dev)
  xi = nf - start_step
  yi = abs_diff_dev[xi]
  ax3.plot(xi, yi, 'ro', markersize=3)
  ax3.annotate(f"({xi}, {yi:.2f})",
               xy=(xi, yi),
               xytext=(5, 5),
               textcoords='offset points',
               fontsize=8)
  ax3.set_title('Absolute Difference')
  ax3.grid(True)
  ax3.ticklabel_format(style='sci', axis='both', scilimits=(0, 0))
  ax4 = axes[1, 1]
  ax4.scatter(n, rel_diff_dev)
  xi = nf - start_step
  yi = rel_diff_dev[xi]
  ax4.plot(xi, yi, 'ro', markersize=3)
  ax4.annotate(f"({xi}, {yi*100:.2f}%)",
               xy=(xi, yi),
               xytext=(5, 5),
               textcoords='offset points',
               fontsize=8)
  ax4.set_title('Relative Difference')
  ax4.grid(True)
  ax4.ticklabel_format(style='sci', axis='both', scilimits=(0, 0))
  plt.savefig(os.path.join(save_dir, f"{file_name}-{micro_step}-MicroStepVNAPerturbed.png"))
  plt.show()

  dev_df = pd.DataFrame()
  dev_df.loc[:, "Absolute Difference"] = abs_diff_dev
  dev_df.loc[:, "Relative Difference"] = rel_diff_dev
  with pd.ExcelWriter(xlsx_file_dir, engine='openpyxl', mode='a', if_sheet_exists='replace') as writer:
    dev_df.to_excel(writer, sheet_name=f'{file_name}-{micro_step}-Diff Dev', index=False)


if __name__ == '__main__':
  meta_steps = [7300, 10000, 12000]
  meta_files = ["稳定性测试", "重复性测试", "自身扰动（设置步进）"]
  start = 0
  saves = r"D:\Users\Wxss\01Project\01VVC\00Project\O-微步测试260205\仪表干扰测试"


  for meta_step in meta_steps:
    for meta_file in meta_files:
      files_dir = os.path.join(saves, rf"2506210101\{meta_file}\{meta_step}")
      microStepVNAPerturbed(meta_step, meta_file, saves, files_dir, start_step=start)


