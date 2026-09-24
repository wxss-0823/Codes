#!D:\Users\Anaconda\anaconda3\python.exe
# -*- coding: utf-8 -*-
# @Time    : 2026/9/9 10:16
# @Author  : Coffee
# @Project : THLCR_CapTest.py
# @File    : RIGOL_ReadWaveForm.py

import struct
from typing import Literal
import re
import time
from datetime import datetime
import os
from decimal import Decimal, ROUND_HALF_UP
from pathlib import Path

import socket
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from openpyxl.workbook import Workbook
from scipy.signal import savgol_filter


class OscillatorDataProcess:
  """RIGOL DH04204 示波器波形数据后处理类"""

  def __init__(self, t, ch1, ch2, ch3=None, ch4=None, save_dir=r"\\10.21.234.127\实验室文件"):
    # 示波器通道数据
    self.t = t
    self.ch1 = ch1
    self.ch2 = ch2
    self.ch3 = ch3
    self.ch4 = ch4
    # 编码器相位数据
    self.phase_a = self.ch1
    self.phase_b = self.ch2
    self.pulse_c = self.ch3 if self.ch3 is not None else None
    # 编码器计数器判定边沿触发位置
    self.pha_pos_trig = {"POS": [], "V": []}
    self.pha_neg_trig = {"POS": [], "V": []}
    self.phb_pos_trig = {"POS": [], "V": []}
    self.phb_neg_trig = {"POS": [], "V": []}
    # 触发边沿计数
    self.pha_pos_edge_num = 0
    self.pha_neg_edge_num = 0
    self.phb_pos_edge_num = 0
    self.phb_neg_edge_num = 0
    # 运行时间戳
    self.fmt_dt = "2026_9_18-18_40_48"
    # 电机参数
    self.micro_step = 16
    self.omega = np.array([], dtype=float)
    self.omega_t = np.array([], dtype=float)
    self.alpha = np.array([], dtype=float)
    self.alpha_t = np.array([], dtype=float)
    # 编码器参数
    self.grating_num = 200
    self.physical_division = 10
    self.quad_decode = 4
    self.grating_r_div = self.grating_num * self.physical_division
    # 文件保存路径
    self.save_dir = save_dir
    # 四舍五入精度
    self.ndigits = 0

  def encoder_counter(self, cal_move_para=True, sg_filter=True) -> tuple:
    """模拟C语言__HAL_TIM_GET_COUNTER实现对编码器脉冲计数"""
    # 初始化参数
    start_pos = 0
    current_pos = start_pos
    pos_list = []
    t_list = []
    micro_step = 0
    # 编码器波形触发电平
    encoder_up_lim = 3.3
    encoder_dw_lim = 1.3
    # TM429 脉冲触发电平
    pulse_up_lim = 2.0
    pulse_dw_lim = 0.5
    # 电平标志
    pha_hi_level = False if self.phase_a[0] <= encoder_dw_lim else True
    phb_hi_level = False if self.phase_b[0] <= encoder_dw_lim else True
    phc_hi_level = False if self.phase_b[0] <= pulse_dw_lim else True
    # 检测边沿
    for i in range(len(self.phase_a)):
      # PHASE A 边沿判断
      pha_flag_tuple, pha_trig_pos = self.edge_detect(self.phase_a[i], pha_hi_level, encoder_up_lim, encoder_dw_lim)  # 决定 A 相边沿计数方向的元组
      pha_pos_edge_flag, pha_neg_edge_flag, pha_hi_level = pha_flag_tuple
      self.pha_pos_trig = {**self.pha_neg_trig, **pha_trig_pos(0)}
      self.pha_neg_trig = {**self.pha_neg_trig, **pha_trig_pos(1)}
      # PHASE B 边沿判断
      phb_flag_tuple, phb_trig_pos = self.edge_detect(self.phase_b[i], phb_hi_level, encoder_up_lim, encoder_dw_lim)  # 决定 B 相边沿计数方向的元组
      phb_pos_edge_flag, phb_neg_edge_flag, phb_hi_level = phb_flag_tuple
      self.phb_pos_trig = {**self.phb_neg_trig, **phb_trig_pos(0)}
      self.phb_neg_trig = {**self.phb_neg_trig, **phb_trig_pos(1)}
      # Pulse C 边沿判断
      if self.ch3 is not None:
        phc_flag_tuple, phc_trig_pos = self.edge_detect(self.phase_c[i], phc_hi_level, pulse_up_lim, pulse_dw_lim)
        phc_pos_edge_flag, phc_neg_edge_flag, phc_hi_level = phc_flag_tuple
        phc_pos_trig = {**self.phc_pos_trig, **phc_trig_pos(0)}
      # if not pha_hi_level and self.phase_a[i] >= up_lim:  # 低电平且大于上限
      #   pha_pos_edge_flag = True
      #   pha_hi_level = True
      #   self.pha_pos_edge_num += 1
      #   self.pha_pos_trig["POS"].append(self.t[i])
      #   self.pha_pos_trig["V"].append(self.phase_a[i])
      # elif pha_hi_level and self.phase_a[i] <= dw_lim:  # 高电平且小于下限
      #   pha_neg_edge_flag = True
      #   pha_hi_level = False
      #   self.pha_neg_edge_num += 1
      #   self.pha_neg_trig["POS"].append(self.t[i])
      #   self.pha_neg_trig["V"].append(self.phase_a[i])
      # else:
      #   # 没有边沿，恢复边沿标志位，更新电平标志
      #   pha_pos_edge_flag = False
      #   pha_neg_edge_flag = False
      #   # ch1_hi_level = False if self.phase_a[i] <= dw_lim else True

      # PHASE B 边沿判断
      # if not phb_hi_level and self.phase_b[i] >= up_lim:  # 低电平且大于上限
      #   phb_pos_edge_flag = True
      #   phb_hi_level = True
      #   self.phb_pos_edge_num += 1
      #   self.phb_pos_trig["POS"].append(self.t[i])
      #   self.phb_pos_trig["V"].append(self.phase_b[i])
      # elif phb_hi_level and self.phase_b[i] <= dw_lim:  # 高电平且小于下限
      #   phb_neg_edge_flag = True
      #   phb_hi_level = False
      #   self.phb_neg_edge_num += 1
      #   self.phb_neg_trig["POS"].append(self.t[i])
      #   self.phb_neg_trig["V"].append(self.phase_b[i])
      # else:
      #   # 没有边沿，恢复边沿标志位，更新电平标志
      #   phb_pos_edge_flag = False
      #   phb_neg_edge_flag = False
      #   # ch2_hi_level = False if self.phase_b[i] <= dw_lim else True

      # 处理边沿标志
      # pha_flag_tuple = (pha_pos_edge_flag, pha_neg_edge_flag, phb_hi_level)
      # phb_flag_tuple = (phb_pos_edge_flag, phb_neg_edge_flag, pha_hi_level)
      # 计数方向标志位
      count_direction = 0  # CW(1): A 超前 B, CCW(-1): B 超前 A
      # 判断方向边沿
      if pha_pos_edge_flag or pha_neg_edge_flag:
        match pha_flag_tuple:
          case (True, False, True):  # A 上升 B 为高 -> 反转
            count_direction = -1
          case (True, False, False):  # A 上升 B 为低 -> 正转
            count_direction = 1
          case (False, True, True):  # A 下降 B 为高 -> 正转
            count_direction = 1
          case (False, True, False):  # A 上升 B 为低 -> 反转
            count_direction = -1
      elif phb_pos_edge_flag or phb_neg_edge_flag:
        match phb_flag_tuple:
          case (True, False, True):  # B 上升 A 为高 -> 正转
            count_direction = 1
          case (True, False, False):  # B 上升 A 为低 -> 反转
            count_direction = -1
          case (False, True, True):  # B 下降 A 为低 -> 反转
            count_direction = -1
          case (False, True, False):  # B 下降 A 为低 -> 正转
            count_direction = 1
      # 根据方向计算等效边沿
      if count_direction in (-1, 1):
        current_pos += count_direction
        pos_list.append(current_pos)
        t_list.append(self.t[i])
    # 增量式编码器: 每 4 个 A B 相脉冲对应移动一个最小周期
    encoder_period_num = current_pos / self.quad_decode
    # 每 10 个最小周期对应 16 个微步, 即一整步被采样为 10 个小周期脉冲
    # micro_step = int(round_half_up(encoder_grating / 10 * 16))
    micro_step = encoder_period_num / self.physical_division * self.micro_step
    print(f"✓ 位置计算完成：等效边沿数 {current_pos} 移动微步数 {micro_step}")
    print(f"✓ 脉冲统计完成: \n"
      f"A 相上升沿 {self.pha_pos_edge_num}, A 相下降沿 {self.pha_neg_edge_num}\n"
      f"B 相上升沿 {self.phb_pos_edge_num}, B 相下降沿 {self.phb_neg_edge_num}")
    # 计算电机瞬时角速度和角加速度
    self.calculate_motor_speed(t_list, pos_list, sg_filter=sg_filter) if cal_move_para else None
    return t_list, pos_list, micro_step

  def edge_detect(self, wave_form, wave_hi_level, up_lim=0.0, dw_lim=0.0) -> Tuple:
    """波形边沿检测"""
    # 边沿标志
    wave_pos_edge_flag = False
    wave_neg_edge_flag = False
    # 边沿计数
    wave_pos_edge_num = 0
    # 触发位置列表
    wave_pos_trig = {"POS": [], "V": []}
    wave_neg_trig = {"POS": [], "V": []}

    # 检测边沿
    if not wave_hi_level and wave_form[i] >= up_lim:  # 低电平且大于上限
      wave_pos_edge_flag = True
      wave_hi_level = True
      wave_pos_edge_num += 1
      wave_pos_trig["POS"].append(self.t[i])
      wave_pos_trig["V"].append(wave_form[i])
    elif wave_hi_level and wave_form[i] <= dw_lim:  # 高电平且小于下限
      wave_neg_edge_flag = True
      wave_hi_level = False
      self.pha_neg_edge_num += 1
      wave_pos_trig["POS"].append(self.t[i])
      wave_pos_trig["V"].append(wave_form[i])
    else:
      # 没有边沿，恢复边沿标志位，更新电平标志
      wave_pos_edge_flag = False
      wave_neg_edge_flag = False
      # wave_hi_level = False if wave_form[i] <= dw_lim else True

    # 归并返回参数
    wave_flag_tuple = (wave_pos_edge_flag, wave_neg_edge_flag, wave_hi_level)
    wave_trig_pos = (wave_pos_trig, wave_neg_trig)
    return wave_flag_tuple, wave_trig_pos

  def plot_trace(self, set_step="16", read_step="16", save_trace=True, cal_move_para=True, sg_filter=True, filename=r"Trace.xlsx") -> None:
    """绘制电机实际移动路径"""
    # 更新时间戳
    self.get_timestamp()
    # 调用编码器计数器
    t_trig_list, pos_list, micro_step = self.encoder_counter(cal_move_para=cal_move_para, sg_filter=sg_filter)
    # 保存 Trace
    self.save_trace(t_trig_list, pos_list, filename, set_step) if save_trace else None
    # 绘图
    # 示波器波形图
    # print(len(ch1))
    fig, axes = plt.subplots(2, 1, figsize=(10, 6), dpi=300)
    # PHASE A
    axes[0].scatter(self.pha_pos_trig["POS"], self.pha_pos_trig["V"], color="r", zorder=3, s=4)
    axes[0].scatter(self.pha_neg_trig["POS"], self.pha_neg_trig["V"], color="c", zorder=3, s=4)
    axes[0].plot(self.t, self.phase_a, label=f"pos: {self.pha_pos_edge_num}, neg: {self.pha_neg_edge_num}", lw=0.5)
    axes[0].set_title("PHASE A")
    axes[0].legend(loc="lower right")
    axes[0].set_xlabel("t/ms")
    axes[0].set_ylabel("U/V")
    # PHASE B
    axes[1].scatter(self.phb_pos_trig["POS"], self.phb_pos_trig["V"], color="r", zorder=3, s=4)
    axes[1].scatter(self.phb_neg_trig["POS"], self.phb_neg_trig["V"], color="c", zorder=3, s=4)
    axes[1].plot(self.t, self.phase_b, label=f"pos: {self.phb_pos_edge_num}, neg: {self.phb_neg_edge_num}", lw=0.5)
    axes[1].set_title("PHASE B")
    axes[1].set_xlabel("t/ms")
    axes[1].set_ylabel("U/V")
    axes[1].legend(loc="lower right")
    plt.tight_layout()
    plt.savefig(os.path.join(self.save_dir, rf"{set_step}微步波形_{self.fmt_dt}.png"))
    plt.close()
    # plt.show()

    # 真实移动路径
    fig, axes = plt.subplots(1, 1, figsize=(10, 6), dpi=300)
    axes.plot(t_trig_list, pos_list, ".-", label=f"set: {set_step} step\nread: {read_step} step\nmove:{micro_step} step")
    axes.set_title("Position Trace")
    plt.legend(loc="lower right")
    axes.set_xlabel("t/ms")
    axes.set_ylabel("Counter Num")
    plt.tight_layout()
    plt.savefig(os.path.join(self.save_dir, rf"{set_step}脉冲计数_{self.fmt_dt}"))
    plt.close()
    # plt.show()

    # 绘制角速度，角加速度图像
    if cal_move_para:
      fig, axes = plt.subplots(figsize=(10, 6), dpi=300)
      # 角速度图像
      axes.plot(self.omega_t, self.omega, color='tab:blue', label=r'$\omega$', zorder=3)
      axes.set_xlabel('t/ms')
      axes.set_ylabel('Omega/rpm', color='tab:blue')
      axes.tick_params(axis='y', labelcolor='tab:blue')
      # 角加速度图像
      ax2 = axes.twinx()
      ax2.scatter(self.alpha_t, self.alpha, color='tab:red', s=4, label=r'$\alpha$', zorder=2)
      ax2.set_ylabel('Alpha/rpm/s', color='tab:red')
      ax2.tick_params(axis='y', labelcolor='tab:red')
      # 合并图例
      lines1, labels1 = axes.get_legend_handles_labels()
      lines2, labels2 = ax2.get_legend_handles_labels()
      axes.legend(lines1 + lines2, labels1 + labels2, loc='upper left')
      plt.title('Rotation Speed & Acceleration')
      plt.tight_layout()
      plt.savefig(os.path.join(self.save_dir, rf"{set_step}电机转速_{self.fmt_dt}"))
      # plt.show()

  def calculate_motor_speed(self, t_trig_list: list, pos_list: list, sample=40, sg_filter=True) -> None:
    """计算电机运动的瞬时角速度"""
    # # 提高计算精度，每一个周期（4个边沿）计算一次角速度与角加速度
    # for i in range(int(len(t_trig_list) / self.quad_decode)):
    #   delta_t = t_trig_list[i + self.quad_decode - 1] - t_trig_list[i]
    #   delta_rad = (pos_list[i + self.quad_decode - 1] - pos_list[i]) / self.quad_decode / self.grating_r_div
    #   self.omega_t = np.append(self.omega_t, t_trig_list[i])
    #   self.omega = np.append(self.omega, delta_rad / delta_t * 1e3 * 60)
    # # 计算角加速度
    # for i in range(int(len(t_trig_list) / self.quad_decode) - 1):
    #   delta_t = t_trig_list[i + self.quad_decode - 1] - t_trig_list[i]
    #   delta_omega = self.omega[i + 1] - self.omega[i]
    #   self.alpha_t = np.append(self.alpha_t, t_trig_list[i])
    #   self.alpha = np.append(self.alpha, delta_omega / delta_t * 1000)
    self.omega_t = t_trig_list[::sample]
    self.alpha_t = t_trig_list[::sample]
    t_array = np.array(t_trig_list[::sample]) / 1e3
    r_array = np.array(pos_list[::sample]) / self.quad_decode / self.grating_r_div
    t_array = savgol_filter(t_array, window_length=sample, polyorder=3) if sg_filter else t_array  # 对不均匀时间平滑处理
    self.omega = np.abs(np.gradient(r_array, t_array / 60))  # 单位缩放
    self.omega = savgol_filter(self.omega, window_length=sample, polyorder=3) if sg_filter else self.omega # 对转速平滑处理
    self.alpha = np.gradient(self.omega, t_array)  # 单位缩放

    return None

  def save_trace(self, t_trig: list, pos_list: list, filename: str=r"Trace.xlsx", step:str="16") -> None:
    """保存实际运动 Trace 及时间至本地文件"""
    sheet_name = f'{step}微步'
    file_path = os.path.join(self.save_dir, filename)
    # 创建文件并写入路径信息
    if not Path(file_path).exists():
      new_wb = Workbook()
      new_wb.save(file_path)
    try:
      trace_df = pd.read_excel(file_path, sheet_name=sheet_name)
    except ValueError as e:
      trace_df = pd.DataFrame()
      with pd.ExcelWriter(file_path, engine='openpyxl', mode='a', if_sheet_exists='replace') as writer:
        trace_df.to_excel(writer, sheet_name=sheet_name, index=False)
    old_len = len(trace_df)
    new_len = len(pos_list)
    if new_len == old_len:
      trace_df[f"Time{self.fmt_dt}"] = t_trig
      trace_df[f"Trace{self.fmt_dt}"] = pos_list
    elif new_len > old_len:
      trace_df = trace_df.reindex(range(new_len))
      trace_df[f"Time{self.fmt_dt}"] = t_trig
      trace_df[f"Trace{self.fmt_dt}"] = pos_list
    else:
      pos_list = list(pos_list) + [np.nan] * (old_len - new_len)
      t_trig = list(t_trig) + [np.nan] * (old_len - new_len)
      trace_df[f"Time{self.fmt_dt}"] = t_trig
      trace_df[f"Trace{self.fmt_dt}"] = pos_list
    with pd.ExcelWriter(file_path, engine='openpyxl', mode='a', if_sheet_exists='replace') as writer:
      trace_df.to_excel(writer, sheet_name=sheet_name, index=False)

  def save_osc_data(self, chunk_size=1_000_000, filename: str=r"RIGOL DH04204 20260918 CCW.csv") -> None:
    """保存示波器的数据至 CSV 文件"""
    wave_data = {"t/ms": self.t, "CH1/V": self.ch1, "CH2/V": self.ch2}
    wave_df = pd.DataFrame(wave_data)
    csv_path = os.path.join(self.save_dir, filename)
    header = not os.path.exists(csv_path)
    for i in range(0, len(wave_df), chunk_size):
      print("Writing chunk {}".format(i))
      chunk = wave_df.iloc[i:i + chunk_size]
      chunk.to_csv(csv_path, mode='a', header=header, index=False)
      header = False
    return None

  def get_timestamp(self) -> None:
    """获取当前运行时间戳"""
    timestamp = time.time()
    dt = datetime.fromtimestamp(timestamp)
    fmt = "%Y_%#m_%d-%H_%M_%S"
    self.fmt_dt = dt.strftime(fmt)
    return None

  def round_half_up(self, x) -> float:
    """实现标准数学四舍五入"""
    q = Decimal(1).scaleb(-self.ndigits)  # 10^-ndigits
    return float(Decimal(str(x)).quantize(q, rounding=ROUND_HALF_UP))

class RigolDHO4204:
  """RIGOL DHO4204 示波器 TCP/IP 控制类"""

  def __init__(self, ip_address, port=5555, timeout=5):
    """
    初始化连接参数。

    参数:
        ip_address (str): 示波器 IP 地址
        port (int): 端口号，默认 5555
        timeout (int): 超时时间（秒）
    """
    # 示波器连接参数
    self.ip_address = ip_address
    self.port = port
    self.timeout = timeout
    self.sock = None
    self.is_connected = False

    # 示波器配置参数
    self.response = None
    self.error = None
    self.max_storage_depth = 50000000
    self.get_data_up_lim = 250000
    self.chunk_lim = {"BYTE": 5_000_000, "WORD": 125000, "ASC": 15625}

    # 波形读取配置参数
    self.poin = 1000
    self.sour: Literal["CHAN1", "CHAN2", "CHAN3", "CHAN4", "MATH1", "MATH2", "MATH3", "MATH4"] = "CHAN1"
    self.mode: Literal["NORM", "MAX", "RAW"] = "RAW"
    self.form: Literal["WORD", "BYTE", "ASC"] = "ASC"
    self.star = 1
    self.stop = 120000
    self.wav_instr_set = {
      "SOUR": self.sour,
      "MODE": self.mode,
      "FORM": self.form,
      "POIN": self.poin,
      "STAR": self.star,
      "STOP": self.stop
    }
    self.cont = 1
    self.xinc = None
    self.xorg = None
    self.xref = None
    self.yinc = None
    self.yorg = None
    self.yref = None

  def connect(self):
    """
    建立 TCP 连接。

    返回:
        bool: 连接成功返回 True，失败返回 False
    """
    try:
      self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
      self.sock.settimeout(self.timeout)
      self.sock.connect((self.ip_address, self.port))
      self.is_connected = True
      print(f"✓ 成功连接到 {self.ip_address}:{self.port}")
      print(f"✓ 仪表型号为: {self.send('*IDN?', data_len=51).strip().decode()}")
      self.sock.sendall("*CLS\n".encode('utf-8'))
      return True
    except socket.timeout:
      print(f"✗ 连接超时: {self.ip_address}:{self.port}")
      self.is_connected = False
      return False
    except ConnectionRefusedError:
      print(f"✗ 连接被拒绝: {self.ip_address}:{self.port}，请检查IP和端口")
      self.is_connected = False
      return False
    except Exception as err:
      print(f"✗ 连接失败: {err}")
      self.is_connected = False
      return False

  def send(self, command, chunk_size=65536, timeout=0.5, data_len=1000):
    """
    发送 SCPI 命令并接收响应。

    参数:
        command (str): SCPI 命令，例如 '*IDN?'

    返回:
        str: 示波器的响应内容，失败返回 None
    """
    if not self.is_connected or self.sock is None:
      print("✗ 未连接到示波器，请先调用 connect()")
      return None

    self.sock.settimeout(timeout)
    chunks = []
    recv_len = 0

    try:
      # 发送命令（确保以换行符结尾）
      if not command.endswith('\n'):
        command = command + '\n'
      self.sock.sendall(command.encode('utf-8'))

      while True:
        # 接收响应
        try:
          chunk = self.sock.recv(chunk_size)
        except socket.timeout:
          # 数据接收完成
          print(f"✓ 接收超时: [{command.strip()}] 回复 {recv_len} 字节")
          break
        chunks.append(chunk)
        recv_len += len(chunk)
        if recv_len == data_len:
          print(f"✓ 指令完成: [{command.strip()}] 回复 {recv_len} 字节")
          break
    except Exception as err:
      print(f"✗ 发送/接收失败: {err}")
      return None
    finally:
      # 恢复原有超时设置
      self.sock.settimeout(self.timeout)
    self.response = b''.join(chunks)
    return self.response

  def query(self, command):
    """send 方法的别名，更符合 SCPI 习惯"""
    return self.send(command)

  def write(self, command):
    """
    发送命令但不等待响应（适用于设置类命令）。

    参数:
        command (str): SCPI 命令
    """
    if not self.is_connected or self.sock is None:
      print("✗ 未连接到示波器，请先调用 connect()")
      return

    try:
      if not command.endswith('\n'):
        command = command + '\n'
      self.sock.sendall(command.encode('utf-8'))
      print(f"✓ 指令完成: [{command.strip()}]")

    except Exception as err:
      print(f"✗ 发送失败: {err}")

    # 查询报错信息
    # try:
    #   self.sock.sendall(":SYST:ERR?\n".encode('utf-8'))
    #   self.error = self.sock.recv(1024)
    #
    # except socket.timeout:
    #   if self.error.strip().decode() != '0,"No error"':
    #     print(f"? Error Info: {self.error.strip().decode()}")
    #   self.sock.sendall("*CLS\n".encode('utf-8'))
    #   pass

  def readPreamble(self):
    self.send(":WAV:PRE?", data_len=67)
    if self.response:
      match self.form:
        case "ASC" | "BYTE" | "WORD":
          info_list = self.response.decode('utf-8').strip().split(',')
          format_list = ["BYTE", "WORD", "ASC"]  # 0(BYTE) 1(WORD) 2(ASC)
          type_list = ["NORM", "MAX", "RAW"]  # 0(NORM) 1(MAX) 2(RAW)
          self.form = format_list[int(info_list[0])]
          self.mode = type_list[int(info_list[1])]
          self.poin = int(info_list[2])
          self.cont = int(info_list[3])
          self.xinc = np.float64(info_list[4])
          self.xorg = np.float64(info_list[5])
          self.xref = np.float64(info_list[6])
          self.yinc = np.float64(info_list[7])
          self.yorg = np.float64(info_list[8])
          self.yref = np.float64(info_list[9])

  def updatePara(self, kwargs):
    self.wav_instr_set.update(kwargs)
    self.sour = self.wav_instr_set["SOUR"]
    self.mode = self.wav_instr_set["MODE"]
    self.form = self.wav_instr_set["FORM"]
    self.poin = self.wav_instr_set["POIN"]
    self.star = self.wav_instr_set["STAR"]
    self.stop = self.wav_instr_set["STOP"]

  def processData(self):
    if not self.response:
      return []
    match self.form:
      case "ASC":
        pattern = r'[-+]?\d*\.?\d+(?:[eE][-+]?\d+)?'  # 匹配科学计数法
        self.response = self.response.decode('utf-8').strip()
        str_data_list = self.response.split(',')
        str_data_filter = [re.match(pattern, data).group(0) for data in str_data_list]
        wave_data = np.array(str_data_filter, dtype=float)
        return t_data, wave_data
      case "WORD" | "BYTE":
        wave_data = []
        chunk = self.response
        # 1. 解析 TMC 数据头，获取数据体长度
        # 假设 response_bytes 以 b'#' 开头
        if not chunk.startswith(b'#'):
          raise ValueError("无效的波形数据头")

        # 获取第二个字节（ASCII数字），表示长度数字的位数
        num_digits = int(chr(chunk[1]))
        # 根据位数提取数据体长度
        body_len_str = chunk[2:2 + num_digits].decode('ascii')
        body_len = int(body_len_str)

        # 2. 提取数据体
        # 数据体的起始位置 = 2 (#'#') + 1 (位数) + num_digits (长度数字)
        body_start = 1 + 1 + num_digits
        data_body = chunk[body_start:body_start + body_len]

        # 3. 根据格式解析数据体
        fmt = self.form

        if fmt == "BYTE":
          # 每个点占1字节，无符号字符
          raw_values = list(struct.unpack(f'{len(data_body)}B', data_body))
          # y_reference = 127
        elif fmt == "WORD":  # WORD 格式
          # 每个点占2字节，小端序无符号短整型
          num_points = len(data_body) // 2
          raw_values = list(struct.unpack(f'<{num_points}H', data_body))
          # y_reference = 32768
        else:
          raise ValueError(f"不支持的格式: {fmt}")

        # 4. 应用公式转换为电压
        y_origin = np.float64(self.yorg)
        y_increment = np.float64(self.yinc)
        y_reference = np.float64(self.yref)

        voltages = [(raw - y_origin - y_reference) * y_increment for raw in raw_values]
        wave_data += voltages
        return wave_data

  def readScreen(self, **kwargs):
    # 设置默认参数
    self.updatePara(kwargs)
    # 指令流
    self.write(f":WAV:SOUR {self.sour}")
    self.write(f":WAV:MODE {self.mode}")
    self.write(f":WAV:FORM {self.form}")
    # 初始化参数
    self.readPreamble()
    # self.write(f":WAV:POIN {self.poin}")

    self.response = self.send(":WAV:DATA?", data_len=14 * self.poin)

    return self.processData()

  def readRam(self, **kwargs):
    # 设置默认参数
    self.updatePara(kwargs)
    # 指令流
    self.write("*CLS")
    self.write(":STOP")
    time.sleep(0.2)
    self.write(f":WAV:SOUR {self.sour}")
    self.write(f":WAV:MODE {self.mode}")
    self.write(f":WAV:FORM {self.form}")
    self.write(f":WAV:POIN {self.chunk_lim[self.form]}")

    # 初始化参数
    self.readPreamble()

    # 计算数据流长度
    if self.form == "ASC":
      data_len = self.poin * 14
    elif self.form == "BYTE":
      data_len = self.poin + 12
    else:
      data_len = self.poin * 2 + 12

    self.max_storage_depth = int(np.float64(self.send(":ACQ:MDEP?", data_len=data_len)))
    self.stop = self.chunk_lim[self.form] if self.mode == "RAW" else 1000
    self.write(f":WAV:STAR {self.star}")
    self.write(f":WAV:STOP {self.stop}")

    # 完全读取内存数据
    self.get_data_up_lim = self.max_storage_depth
    wave_data = np.array([], dtype=float)
    for idx in range(1, int(self.get_data_up_lim / self.stop + 1)):
      self.response = self.send(":WAV:DATA?")
      wave_data = np.concatenate([wave_data, self.processData()])
      self.stop += self.chunk_lim[self.form]
      self.star += self.chunk_lim[self.form]
      if self.stop <= self.max_storage_depth:
        self.write(f":WAV:STAR {self.star}")
        self.write(f":WAV:STOP {self.stop}")

    # 处理时间序列
    xinc = np.float64(self.xinc)
    xorg = np.float64(self.xorg)
    xref = np.float64(self.xref)
    t_data = [(xorg + xref + i * xinc) * 1e3 for i in range(len(wave_data))]  # 时间轴 ms

    return t_data, wave_data

  def close(self):
    """关闭连接"""
    if self.sock:
      self.sock.close()
      self.is_connected = False
      print("✓ 连接已关闭")

  def __enter__(self):
    """支持 with 语句"""
    self.connect()
    return self

  def __exit__(self, exc_type, exc_val, exc_tb):
    """退出 with 语句时自动关闭连接"""
    self.close()


if __name__ == "__main__":
  save_dir = r"\\10.21.234.127\实验室文件\7_滚珠电容_20260909\未使能模式"
  # save_dir = r"\\10.21.234.127\实验室文件\8_常规电容&编码器_20260915\未使能"
  set_step = f"Delay"
  read_step = "-"
  # read_step = "32"

  # 实时读取示波器数据
  with RigolDHO4204("169.254.112.67", 5555) as scope:
    t1, ch1 = scope.readRam(SOUR="CHAN1", MODE="RAW", FORM="BYTE")  # WORD 模式异常 STOP 3750000
    t2, ch2 = scope.readRam(SOUR="CHAN2", MODE="RAW", FORM="BYTE")
    t3, ch3 = scope.readRam(SOUR="CHAN3", MODE="RAW", FORM="BYTE")
  # 处理数据
  osc_dp = OscillatorDataProcess(t1, ch1, ch2, ch3, save_dir=save_dir)
  kw_args = {"set_step": set_step, "read_step": read_step, "save_trace": True, "cal_move_para": True, "sg_filter": True}
  osc_dp.plot_trace(**kw_args)
