#!D:\Users\Anaconda\anaconda3\python.exe
# -*- coding: utf-8 -*-
# @Time    : 2026/8/13 14:54
# @Author  : Coffee
# @Project : Pycharm
# @File    : SNPFunctions.py

import os

def sortSNPFile(
    root_file: str
) -> list:
  """
  root_file: SNP 文件根目录，及多个 SNP 文件的上一层路径
  """

  # 获取子文件
  snp_file_list = os.listdir(root_file)

  # 获取创建时间
  snp_mtime_list = [(snp_file_name, os.path.getmtime(os.path.join(root_file, snp_file_name))) for snp_file_name in snp_file_list]

  # 按创建时间排序
  snp_ctime_sorted = sorted(snp_mtime_list, key=lambda x: x[1])

  return snp_ctime_sorted
