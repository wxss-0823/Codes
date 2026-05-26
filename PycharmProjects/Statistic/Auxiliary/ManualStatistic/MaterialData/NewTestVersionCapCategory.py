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
iqc_data_dir_list.append(r"C:\Users\w00025121\Desktop\新建文件夹\测试工位1\测试工位1")
iqc_data_dir_list.append(r"C:\Users\w00025121\Desktop\新建文件夹\测试工位2\测试工位2")
iqc_data_dir_list.append(r"C:\Users\w00025121\Desktop\新建文件夹\测试工位3\测试工位3")

sn_map = dict(tuple())
sn_ptn = r"0819\d{4}-00[12]"
state_ptn = (r"Fail", r"Pass")

# SN set list: [pass(), fail()]
sn_set = [set(), set()]
# 处理数据时间
timestamp = time.time()
date = datetime.fromtimestamp(timestamp)
date_ptn = "%Y%m%d"
date_fm = date.strftime(date_ptn)


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
    sn_map[row_split[1]] = (row_split[0], row_split[2])

for iqc_data_dir in iqc_data_dir_list:
  sub_dir_list = next(os.walk(iqc_data_dir))[1]
  for sub_dir in sub_dir_list:
    try:
      if re.search(sn_ptn, sub_dir):
        sn = re.search(sn_ptn, sub_dir).group(0)
        sub_route = os.path.join(iqc_data_dir, sub_dir)
        pass_dir_name = os.path.join(f"{sn_map[sn][0]}", f"{date_fm} {sn} {sn_map[sn][1]}")
        fail_dir_name = os.path.join(f"{sn_map[sn][0]}", f"{date_fm} {sn} {sn_map[sn][1]} Failed")
        pass_dir = os.path.join(iqc_data_dir, pass_dir_name)
        fail_dir = os.path.join(iqc_data_dir, fail_dir_name)

        # Fail file
        if re.search(state_ptn[0], sub_dir):
          os.makedirs(fail_dir, exist_ok=True)
          sn_set.append(sn)
          shutil.move(sub_route, fail_dir)
        # Pass file
        elif re.search(state_ptn[1], sub_dir):
          os.makedirs(pass_dir, exist_ok=True)
          sn_set.append(sn)
          shutil.move(sub_route, pass_dir)
        else:
          print(f"File format error: {sub_dir}")

      else:
        print(f"The dir {sub_dir} don't have SN")
    except KeyError as key_error:
      print(f"The cap type file don't contain: {key_error}")


