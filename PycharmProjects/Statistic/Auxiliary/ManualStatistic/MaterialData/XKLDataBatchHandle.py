#!D:\Users\Anaconda\anaconda3\python.exe
# -*- coding: utf-8 -*-
# @Time    : 2026/1/20 18:15
# @Author  : Coffee
# @Project : Auxiliary
# @File    : XKLDataBatchHandle.py

import os
import re
import time
from datetime import datetime
from os.path import exists

import CapReadXKLFunc as Stat
import TenTimesPowerOnOff as poo
import CapReadDataGLChuchangPro as COA


def xkl_data_batch_read(
    dest_dir: str,
    figure_dir: str,
    handle_type: str,
    version_type: str
):
  """
  批量读取并处理数据
  """
  # 处理数据时间
  timestamp = time.time()
  date = datetime.fromtimestamp(timestamp)
  date_ptn = "%Y%m%d"
  date_fm = date.strftime(date_ptn)
  date_data_ptn = r"\d{8}"
  time_ptn = "%y%m%d-%H%M%S"
  date_data = re.search(date_data_ptn, dest_dir).group(0)
  time_fm = date.strftime(time_ptn) + '(' + os.path.split(dest_dir)[1] + ')'
  output_dir = fr'D:\Users\WorkSpace\Pycharm\Auxiliary\ManualStatistic\Output\step_cap_error_{time_fm}.csv'
  if handle_type in ["POO", "", "SingleCap"]:
    data_type = "IQC"
    name_str_list = [date_fm, data_type + date_data, handle_type, version_type]
  else:
    data_type = "COA"
    name_str_list = [date_fm, data_type + date_data, "DoubleCheck"]

  figure_dir = os.path.join(figure_dir, "_".join([name for name in name_str_list if name != ""]))

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
    match handle_type:
      case '':
        Stat.capRead(dstDirs[i], figDirs[i])
      case 'COA':
        COA.CoaCapRead(dstDirs[i], figDirs[i], output_dir)
        # COA.DataStatistics(dstDirs[i])
      case 'POO':
        version_ptn = version_type if version_type != "ALL" else ""
        poo.getPowerOnOffData(dstDirs[i], figDirs[i], time_fm, version_ptn)
      case 'SingleCap':
        Stat.everyCapPlot(dstDirs[i], figDirs[i])
  # 判断文件夹不问空
  for figure_dir in figDirs:
    if not len(os.listdir(figure_dir)):
      os.rmdir(figure_dir)


if __name__ == "__main__":
  iqc_root_dir = r"D:\Users\Wxss\01Project\01VVC\03Data\02IQC\0Variable\2026"
  coa_root_dir = r"D:\Users\Wxss\01Project\01VVC\03Data\01COA"
  fig_dir = r"D:\Users\Wxss\01Project\01VVC\03Data\04FigureArchive"
  batch_dirs = [r"\20260806"]
  hdl_type: Literal["POO", "", "SingleCap", "COA"] = 'SingleCap'
  ver_type: Literal["AVO2", "AV03", ""] = ''

  for batch_dir in batch_dirs:
    dst_dir = coa_root_dir + batch_dir if hdl_type == 'COA' else iqc_root_dir + batch_dir
    xkl_data_batch_read(dst_dir, fig_dir, hdl_type, ver_type)
