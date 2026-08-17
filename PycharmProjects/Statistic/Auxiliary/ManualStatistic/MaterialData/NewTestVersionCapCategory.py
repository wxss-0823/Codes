#!D:\Users\Anaconda\anaconda3\python.exe
# -*- coding: utf-8 -*-
# @Time    : 2026/3/30 20:16
# @Author  : Coffee
# @Project : Pycharm
# @File    : NewTestVersionCapCategory.py


import os
import shutil
import re
import time
from datetime import datetime
import csv
from functools import reduce

iqc_data_dir_list = list()
iqc_data_dir_list.append(r"D:\Users\Wxss\bin\WeLink\DownloadFiles\7月测试数据\7月测试数据\7月测真空电容试数据\测试设备1")
iqc_data_dir_list.append(r"D:\Users\Wxss\bin\WeLink\DownloadFiles\7月测试数据\7月测试数据\7月测真空电容试数据\测试设备2")
iqc_data_dir_list.append(r"D:\Users\Wxss\bin\WeLink\DownloadFiles\7月测试数据\7月测试数据\7月测真空电容试数据\测试设备3")

sn_map = dict(tuple())
sn_ptn = r"0819\d{4}-00[12]"
state_ptn = (r"Fail", r"Pass", r"Log")
cate_set = set()
log_n = 1

# 处理数据时间
timestamp = time.time()
date = datetime.fromtimestamp(timestamp)
date_ptn = "%Y%m%d"
year_ptn = "%Y"
date_fm = date.strftime(date_ptn)
year_fm = date.strftime(year_ptn)


def deleteSlash():
  with open('cap_type.csv', 'r+', encoding='utf-8') as f:
    content = f.read()
    content = content.replace('/', '')
    content = content.replace('\t', ' ')
    f.seek(0)
    f.write(content)
    f.truncate()


# deleteSlash()

with open(r'./cap_type.csv', 'r', encoding='utf-8') as csvfile:
  reader = csv.reader(csvfile)
  for row in reader:
    row_split = row[0].split(' ')
    cate_set.add(row_split[0])
    sn_map[row_split[1]] = (row_split[0], row_split[2])

for iqc_data_dir in iqc_data_dir_list:
  sub_dir_list = next(os.walk(iqc_data_dir))[1]
  for cate in cate_set:
    if cate in sub_dir_list:
      sub_dir_list.remove(cate)
  for sub_dir in sub_dir_list:
    try:
      log_dir_name = os.path.join(f"{sn_map['0'][0]}", f"{date_fm}")
      log_dir = os.path.join(iqc_data_dir, log_dir_name)
      log_n_name = sub_dir + "-" + str(log_n)
      unknown_dir_name = os.path.join(f"{sn_map['x'][0]}", f"{date_fm}")
      unknown_dir = os.path.join(iqc_data_dir, unknown_dir_name)
      if re.search(sn_ptn, sub_dir):
        sn = re.search(sn_ptn, sub_dir).group(0)
        sub_route = os.path.join(iqc_data_dir, sub_dir)
        pass_dir_name = os.path.join(f"{sn_map[sn][0]}", f"{date_fm}", f"{date_fm} {sn} {sn_map[sn][1]}")
        fail_dir_name = os.path.join(f"{sn_map[sn][0]}", f"{date_fm}", f"{date_fm} {sn} {sn_map[sn][1]} Failed")
        pass_dir = os.path.join(iqc_data_dir, pass_dir_name)
        fail_dir = os.path.join(iqc_data_dir, fail_dir_name)

        # Fail file
        if re.search(state_ptn[0], sub_dir):
          os.makedirs(fail_dir, exist_ok=True)
          shutil.move(sub_route, fail_dir)
        # Pass file
        elif re.search(state_ptn[1], sub_dir):
          os.makedirs(pass_dir, exist_ok=True)
          shutil.move(sub_route, pass_dir)
        else:
          print(f"File format error: {sub_dir}")
          os.makedirs(unknown_dir, exist_ok=True)
          shutil.move(sub_route, unknown_dir)
      elif re.match(state_ptn[2], sub_dir):
        # Log file
        os.makedirs(log_dir, exist_ok=True)
        os.rename(os.path.join(iqc_data_dir, sub_dir), os.path.join(iqc_data_dir, log_n_name))
        sub_route = os.path.join(iqc_data_dir, log_n_name)
        log_n += 1
        shutil.move(sub_route, log_dir)
      else:
        # Unknown file
        print(f"The dir {sub_dir} don't have SN")
        os.makedirs(unknown_dir, exist_ok=True)
        sub_route = os.path.join(iqc_data_dir, sub_dir)
        shutil.move(sub_route, unknown_dir)

    except KeyError as key_error:
      print(f"The cap type file don't contain: {key_error}")
