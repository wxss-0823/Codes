#!D:\Users\Anaconda\anaconda3\python.exe
# -*- coding: utf-8 -*-
# @Time    : 2026/3/14 16:52
# @Author  : Coffee
# @Project : Pycharm
# @File    : HighAccelerateTest.py

import numpy as np
import pandas as pd

# cap_list = [487.5, 352.5, 285, 217.5, 177, 163.5, 151.35]
# cap_list = [81.25, 58.75, 47.5, 36.25, 29.5, 27.25, 25.225]
per_list = [25, 15, 10, 5, 2, 1, 0.1]
cap_list = [487.5, 352.5, 285, 217.5, 177, 163.5, 151.35]
num_list = [1, 5, 10, 58, 15, 10, 1]
# 复位容值：最小容值
end_value = 150
# 0.7 至 0.3 切换阈值
threshold = 218
big_interval = 0.7
sml_interval = 0.3


test_list = np.array([])
duration_list = np.array([])
step_description_list = np.array([])

for i in range(len(cap_list)):
  for j in range(num_list[i]):
    # test_list = np.append(test_list, [150, cap_list[i]])
    # test_list = np.append(test_list, [25, cap_list[i]])
    # test_list = np.append(test_list, [100, cap_list[i]])
    test_list = np.append(test_list, [end_value, cap_list[i]])
    step_description_list = np.append(step_description_list, ["0%", f"{j+1}-{per_list[i]}%"])
    if cap_list[i] >= threshold:
      duration_list= np.append(duration_list, [big_interval, big_interval])
    # elif 145 <= cap_list[i] <= 190:
    #   if duration_list[-1] != 0.5:
    #     duration_list = np.append(duration_list, [duration_list[-1], 0.5])
    #   else:
    #     duration_list= np.append(duration_list, [0.5, 0.5])
    else:
      if duration_list[-1] != sml_interval:
        duration_list = np.append(duration_list, [duration_list[-1], sml_interval])
      else:
        duration_list = np.append(duration_list, [sml_interval, sml_interval])

# duration_list[0] = 5
duration_list = np.append(duration_list, duration_list[-1])
delay_list = duration_list
step_description_list[0] = "初始值"
step_description_list = np.append(step_description_list, "结束值")
test_list = np.append(test_list, end_value)



test_dict = {
  "step": [i for i in range(201)],
  "duration": duration_list,
  # "duration": np.full(201, 0.01),
  "delay": delay_list,
  # "delay": np.full(201, 0.01),
  "step description": step_description_list,
  "cap": test_list
}

test_df = pd.DataFrame(test_dict)
xlsx_name = r"D:\Users\Wxss\01Project\01VVC\00Project\O-20260304VVC寿命测试\高加速度\高加速度测试用例.xlsx"

with pd.ExcelWriter(xlsx_name, engine='openpyxl', mode='a', if_sheet_exists='replace') as writer:
  test_df.to_excel(writer, sheet_name="GZSG_0.2Nm_1500", index=False)








