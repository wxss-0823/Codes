#!D:\Users\Anaconda\anaconda3\python.exe
# -*- coding: utf-8 -*-
# @Time    : 2026/1/20 18:15
# @Author  : Coffee
# @Project : Auxiliary
# @File    : XKLDataBatchRead.py

import os
import re
import time
from datetime import datetime
from os.path import exists

import CapReadXKLFunc as Stat
import TenTimesPowerOnOff as poo


def xkl_data_batch_read(
    dest_dir: str,
    figure_dir: str,
    handle_type: str
):
  """
  批量读取并处理数据
  """
  # 处理数据时间
  timestamp = time.time()
  date = datetime.fromtimestamp(timestamp)
  date_ptn = "%Y%m%d"
  date_fm = date.strftime(date_ptn)
  time_ptn = "%y%m%d-%H%M%S"
  time_fm = date.strftime(time_ptn) + '(' + os.path.split(dest_dir)[1] + ')'
  os.path.split(dest_dir)
  figure_dir = os.path.join(figure_dir, date_fm + handle_type)

  # os.makedirs(dstDir, exist_ok=True)
  os.makedirs(figure_dir, exist_ok=True)

  subDirs = next(os.walk(dest_dir))[1]
  subDirMP = r"\d{8}-\d{3}"

  for subDir in subDirs:
    if re.search(r"Failed", subDir):
      subDirs.remove(subDir)

  # Stat.stabilityXKLTest(dstDir, figDir)

  # Plot Every Capacity Figure
  i = 0
  for _ in range(len(subDirs)):
    if re.search(subDirMP, subDirs[i]) is None:
      subDirs.remove(subDirs[i])
    else:
      i += 1

  nLoop = len(subDirs)
  dstDirs = [dest_dir + '\\' + subDir for subDir in subDirs]
  figDirs = [figure_dir + '\\' + subDir for subDir in subDirs]

  # 确保目录存在
  for figure_dir in figDirs:
    os.makedirs(figure_dir, exist_ok=True)

  for i in range(nLoop):
    print(f"Reading: {dstDirs[i]}\nWriting: {figDirs[i]}")
    # Stat.capRead(dstDirs[i], figDirs[i])
    poo.getPowerOnOffData(dstDirs[i], figDirs[i], time_fm)
    # Stat.everyCapPlot(dstDirs[i], figDirs[i])


# dst_dir = r"C:\Users\w00025121\Desktop\temp - 副本"
# fig_dir = r"C:\Users\w00025121\Desktop\fig1"
root_dir = r"D:\Users\Wxss\01Project\01VVC\03Data\02IQC\0Variable\2026"
batch_dirs = [r"\20260428"]
fig_dir = r"D:\Users\Wxss\01Project\01VVC\03Data\02IQC\0Variable\FigureArchive"
hdl_type = ' power on off'
# hdl_type = ''

for batch_dir in batch_dirs:
  dst_dir = root_dir + batch_dir
  # dst_dir = r"C:\Users\w00025121\Desktop\new"
  xkl_data_batch_read(dst_dir, fig_dir, hdl_type)
