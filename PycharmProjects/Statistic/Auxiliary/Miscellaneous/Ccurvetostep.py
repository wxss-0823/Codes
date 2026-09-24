import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os
import sys
import math

def captostep(df, target, direction):
  """
  根据目标容值和方向，从DataFrame中插值计算微步数。

  参数:
      df: DataFrame，必须包含列 'Step'（整步数）、'CW'、'CCW'
      target: float，目标容值
      direction: int，1 表示 CW，0 表示 CCW

  返回:
      int，微步数（四舍五入）
  """
  # Log list：记录查表过程
  log_list = []

  # 确定使用的容值列
  cap_col = 'CW' if direction == 1 else 'CCW'

  # 提取数组（假设 df 已按容值升序排列）
  cap_vals = df[cap_col].values
  step_vals = df['Step'].values          # 整步数
  micro_vals = step_vals * 16            # 转换为微步数

  n = len(cap_vals)
  if n == 1:
    return int(micro_vals[0])

  # 边界检查
  if target <= cap_vals[0]:
    return int(micro_vals[0])
  if target >= cap_vals[-1]:
    return int(micro_vals[-1])

  # 二分查找
  low, high = 0, n - 1
  low_list, high_list = [], []
  i = 0
  plt.close('all')
  while low < high - 1:
    mid = (low + high) // 2
    mid_val = cap_vals[mid]
    if abs(mid_val - target) < 1e-15:
      # 查表路径
      plt.plot(range(len(low_list)), low_list, range(len(low_list)), high_list)
      plt.legend([f'low{i}', f'high{i}'])
      # plt.show()
      return int(micro_vals[mid]), log_list
    elif mid_val < target:
      low = mid
    else:
      high = mid
    i = i + 1
    low_list.append(low)
    high_list.append(high)
    log_list.append(f"第{i}次查找：low: {low}，high: {high}")
    # print(f"第{i}次查找：low: {low}，high: {high}")

  # 插值区间 [high, low]
  left, right = low, high
  y0, y1 = cap_vals[left], cap_vals[right]
  x0, x1 = micro_vals[left], micro_vals[right]

  # 线性插值得到微步数
  interp = x0 + (x1 - x0) * (target - y0) / (y1 - y0)
  # 四舍五入（模拟 C++ round，对正数有效）

  # 查表路径
  plt.plot(range(len(low_list)), low_list, range(len(low_list)), high_list)
  plt.legend([f'low{i}', f'high{i}'])
  # plt.show()
  return int(math.floor(interp + 0.5)), log_list


def steptocap(df, step_micro, direction):
  """
  根据微步数和方向，从DataFrame中插值计算对应的容值。

  参数:
      df: DataFrame，必须包含列 'Step'（整步数）、'CW'、'CCW'
      step_micro: int，目标微步数
      direction: int，1 表示 CW，0 表示 CCW

  返回:
      float，插值后的容值
  """
  cap_col = 'CW' if direction == 1 else 'CCW'
  cap_vals = df[cap_col].values
  step_vals = df['Step'].values
  micro_vals = step_vals * 16

  n = len(cap_vals)
  if n == 1:
    return float(cap_vals[0])

  # 边界检查
  if step_micro <= micro_vals[0]:
    return float(cap_vals[0])
  if step_micro >= micro_vals[-1]:
    return float(cap_vals[-1])

  # 二分查找定位区间
  low, high = 0, n - 1
  while low <= high:
    mid = (low + high) // 2
    mid_val = micro_vals[mid]
    if mid_val == step_micro:   # 精确匹配（整数比较，无需容差）
      return float(cap_vals[mid])
    elif mid_val < step_micro:
      low = mid + 1
    else:
      high = mid - 1

  # 插值区间 [high, low]
  left, right = high, low
  y0, y1 = micro_vals[left], micro_vals[right]
  x0, x1 = cap_vals[left], cap_vals[right]
  # 线性插值：容值 = x0 + (x1-x0)*(step_micro - y0)/(y1-y0)
  interp = x0 + (x1 - x0) * (step_micro - y0) / (y1 - y0)
  return float(interp)


#df = pd.read_excel(r'e:\VScode\Python\UaualCal\Mycode\CcurveTostep\CcurveV1.xlsx')
df = pd.read_excel(r"C:\Users\w00025121\Desktop\CurveData-20260827-10265J204889-RAM.xlsx")
# df = df.drop(0)
df[['CW', 'CCW']] = df[['CW', 'CCW']].apply(pd.to_numeric, errors='coerce').round(0)
df_int=df
df_int.rename(columns={df_int.columns[0]: 'Step', df_int.columns[1]: 'CW',df_int.columns[2]: 'CCW'}, inplace=True)

#C曲线处理，当CW>CCW，正反曲线一致，取平均值。否则正反曲线保持一致性
avg = ((df_int['CW'] + df_int['CCW']) / 2).round(0) # 丢弃0.05pF
mask = df_int['CCW'] < df_int['CW']
df_int.loc[mask, 'CW'] = avg[mask]
df_int.loc[mask, 'CCW'] = avg[mask]

# 画图
plt.rcParams['font.sans-serif'] = ['SimHei']   # 显示中文标签
plt.rcParams['axes.unicode_minus'] = False     # 正常显示负号
fig, ax1 = plt.subplots(figsize=(10, 6))
ax1.plot(df_int['Step'] * 16 , df_int['CW'] / 10 , 'b-', linewidth=2, label='容值 pF')
ax1.set_xlabel('微步数', fontsize=12)
ax1.set_ylabel('容值 (pF)', color='b', fontsize=12)
ax1.tick_params(axis='y', labelcolor='b')
ax1.grid(True, linestyle='--', alpha=0.6)
ax2 = ax1.twinx()
ax2.plot(df_int['Step'] * 16  , (df_int['CCW'] - df_int['CW']) / 10, 'r-', linewidth=2, label='正反偏差 pF')
ax2.set_ylabel('正反偏差 (pF)', color='r', fontsize=12)
ax2.tick_params(axis='y', labelcolor='r')
lines1, labels1 = ax1.get_legend_handles_labels()
lines2, labels2 = ax2.get_legend_handles_labels()
ax1.legend(lines1 + lines2, labels1 + labels2, loc='best', fontsize=11)
plt.title('容值与正反偏差曲线', fontsize=14)
fig.tight_layout()
# plt.show()

#################################################
Cap_innital=228.7   #0.1pF容值  初始容值
current_orientation=0    #cw 正方向为1,CCW反方向为0   初始方向
plt.figure(figsize=(6, 6), dpi=100, facecolor="w")
current_step, _=captostep(df_int, Cap_innital, current_orientation)  #Preset容值下的微步数
print(f"innital，容值 {Cap_innital} 对应的整步数: {current_step / 16}")
print("************************************************************")
#################################################

# print("输入相对微步数，输入 'q' 退出：")
# while True:
#     user_input = input("相对微步数: ")
#     if user_input.lower() == 'q':
#         break
#     try:
#         rel = int(user_input)
#     except ValueError:
#         print("请输入整数或 'q'")
#         continue
#     # 根据相对步数正负决定新方向
#     if rel < 0:
#         new_orientation = 0
#     else:
#         new_orientation = 1   # rel >=0 时方向为1
#     target_abs = current_step + rel
#     try:
#         cap_value = steptocap(df_int, current_step, current_orientation)
#     except IndexError:
#         print("目标微步数超出数据范围，请重新输入")
#         continue
#     print(f"相对微步步数: {rel} -> 当前C曲线: {'CW' if current_orientation==1 else 'CCW'}, 当前绝对步数: {current_step}, 当前容值: {cap_value:.4f}")
#     current_step = target_abs
#     current_orientation = new_orientation
#
#     try:
#         cap_value = steptocap(df_int, target_abs, current_orientation)
#     except IndexError:
#         print("目标微步数超出数据范围，请重新输入")
#         continue
#     print(f"相对微步步数: {rel} -> 运动后C曲线: {'CW' if current_orientation==1 else 'CCW'}, 运动后绝对步数: {target_abs},运动后容值: {cap_value:.4f}")
#
#     print("************************************************************")



#手动测试，分别输入容值和步进，查找对应的C曲线

# target_val = 48
# steps_cw = captostep(df_int, target_val, 1)  # 方向 1 (CW)
# steps_ccw = captostep(df_int, target_val, 0)  # 方向 0 (CCW)
# print(f"CW方向，容值 {target_val} 对应的微步数: {steps_cw} 整步数: {steps_cw / 16}")
# print(f"CCW方向，容值 {target_val} 对应的微步数: {steps_ccw} 整步数: {steps_ccw / 16}")
#
#
# test_micro = 1000
# cap_cw = steptocap(df_int, test_micro, 1)
# cap_ccw = steptocap(df_int, test_micro, 0)
# print(f"CW方向，微步数 {test_micro} 对应的容值: {cap_cw:.4f}")
# print(f"CCW方向，微步数 {test_micro} 对应的容值: {cap_ccw:.4f}")

# for cap in np.linspace(2288, 2301, 14):
# 20260827 C曲线存在异常大值点，导致连续多个容值查表对应至同一步进，修复异常点后，恢复，但本脚本未复现该查表问题。
plt.figure(figsize=(6, 6), dpi=100, facecolor="w")
plt.title('Table-Lookup Route')
for cap in np.linspace(2288, 2301, 14):
  step, log_txt = captostep(df_int, cap, current_orientation)
  log_dir = r"C:\Users\w00025121\Desktop\log.txt"
  # os.makedirs(log_dir, exist_ok=True)
  with open(log_dir, 'a', encoding='utf-8') as f:
    f.write(f"\nCap: {cap/10} -> Step: {step/16}\n")
    f.write('\n'.join(log_txt)) if log_txt else None
  print(f"Cap: {cap/10} -> Step: {step/16}")
plt.show()