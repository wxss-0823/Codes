#!D:\Users\Anaconda\anaconda3\python.exe
# -*- coding: utf-8 -*-
# @Time    : 2026/5/6 10:16
# @Author  : Coffee
# @Project : Pycharm
# @File    : BatchArchived.py


import zipfile
import os
import re


root_dir = r"C:\Users\w00025121\Desktop\新建文件夹\XXX交付件COA 260509"
sub_dirs = next(os.walk(root_dir))[1]
filename_ptn = r"\d{8} 08190\d{3}-00[1-2]"
date_sn_set = set()

for sub_dir in sub_dirs:
  if re.search(filename_ptn, sub_dir):
    date_sn_set.add(re.search(filename_ptn, sub_dir).group(0))

for date_sn in date_sn_set:
  for sub_dir in sub_dirs:
    if re.search(date_sn, sub_dir):
      # IQC name
      # zip_path = os.path.join(root_dir, date_sn+".zip")
      # COA name
      zip_path = os.path.join(root_dir, date_sn+"交付件COA.zip")
      mode: Literal["r", "w", "x", "a"] = "a" if os.path.exists(zip_path) else "w"
      with zipfile.ZipFile(zip_path, mode, zipfile.ZIP_DEFLATED) as zip_file:
        for root, dirs, files in os.walk(os.path.join(root_dir, sub_dir)):
          for file in files:
            file_path = os.path.join(root, file)
            archived_name = os.path.relpath(file_path, start=root_dir)
            zip_file.write(file_path, archived_name)