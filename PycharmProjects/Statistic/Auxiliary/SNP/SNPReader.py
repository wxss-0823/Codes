#!D:\Users\Anaconda\anaconda3\python.exe
# -*- coding: utf-8 -*-
# @Time    : 2026/8/13 14:21
# @Author  : Coffee
# @Project : Pycharm
# @File    : SNPReader.py


# -*- coding: utf-8 -*-
"""
Created on Tue Mar  4 14:06:36 2025

@author: l00002294
"""

import numpy as np
import skrf as rf
from fontTools.ttLib.tables.E_B_D_T_ import ebdt_bitmap_format_6

import SNPFunctions as sf
from matplotlib import pyplot as plt
import math
import os
import re

def read_snp(
    root_dir: str,
    rst_list: ndarray,
    Z_p,
    Z_s,
    labels=None,
    *args,
    **kwargs
) -> tuple[ndarray, dict]:
  if labels is None:
    labels = {}
  file_name = []
  idx = 0
  # dir1 = os.listdir(path1)
  snp_list = sf.sortSNPFile(root_dir)
  label_name = kwargs.get("label_key_name", "SNP")
  for snp in snp_list:
    file_name.append(re.search(r"_(\d+.0_pf)_", snp[0]).group(1))  # 取文件名
    snp_network = rf.Network(os.path.join(root_dir, snp[0]))
    imag_data = ((snp_network.z.reshape(N)) * Z_p / ((snp_network.z.reshape(N)) + Z_p) + Z_s).imag
    # Imag=network_13M.z_im.reshape(N)
    rst_list[:, idx] = imag_data
    idx = idx + 1

  labels[label_name] = file_name

  return rst_list, labels

N = 19901  # 网分设置测试点数
FreqStart = 1e6
FreqStop = 200e6
Freqstep = (FreqStop - FreqStart) / (N - 1)
FileNum = 10  # 测试的文件数量，即容值点位


FreqShowStart = 24e6  # 画图起始频率
FreqShowStop = 30e6
CenterFreq = 27

# FreqShowStart = 54e6
# FreqShowStop = 66e6
# CenterFreq = 60

# FreqShowStart = 1.8e6
# FreqShowStop = 2.2e6
# CenterFreq = 2

FreqShowStart_Num = int((FreqShowStart - FreqStart) / (FreqStop - FreqStart) * N)
FreqShowStop_Num = int((FreqShowStop - FreqStart) / (FreqStop - FreqStart) * N)
FreqShow_Num = FreqShowStop_Num - FreqShowStart_Num + 1

Freqnum_data = int((CenterFreq * 1e6 - FreqStart) / (FreqStop - FreqStart) * N)  # 取数list频率，这里为13.56MHz

gl172601310151_250PF = np.zeros(shape=(N, FileNum), dtype=np.complex128)
gl202601311014_1500PF = np.zeros(shape=(N, FileNum), dtype=np.complex128)
gl172601310101_250pF = np.zeros(shape=(N, FileNum), dtype=np.complex128)
gl202511213901_1500pF = np.zeros(shape=(N, FileNum), dtype=np.complex128)
C2207075_250pF = np.zeros(shape=(N, FileNum), dtype=np.complex128)
C2219619_250pF = np.zeros(shape=(N, FileNum), dtype=np.complex128)
C2290262_1500pF = np.zeros(shape=(N, FileNum), dtype=np.complex128)
C2291830_1500pF = np.zeros(shape=(N, FileNum), dtype=np.complex128)

Cp = 0.001e-12  # 国产电容补偿并联电容
Ls = 0e-9  # 国产电容补偿串联电感
Zp = 1 / (1j * np.linspace(FreqStart, FreqStop, N) * 2 * math.pi * Cp)
Zs = 1j * np.linspace(FreqStart, FreqStop, N) * 2 * math.pi * Ls
Labels = {}
path = []

root_snp_dir = r"D:\Users\Wxss\bin\WeLink\DownloadFiles\CapParasiticRe"
# path1:442 path2:830 path3:151 path4:014
sub_snp_dir = next(os.walk(root_snp_dir))[1]

# print(sub_snp_dir)

# comet 2207075-250pF
path.append(os.path.join(root_snp_dir, sub_snp_dir[0]))
(C2207075_250pF, Labels) = read_snp(path[-1], C2207075_250pF, Zp, Zs, Labels, label_key_name="C2207075_250pF")

# comet 2219619-250pF
path.append(os.path.join(root_snp_dir, sub_snp_dir[1]))
(C2219619_250pF, Labels) = read_snp(path[-1], C2219619_250pF, Zp, Zs, Labels, label_key_name="C2219619_250pF")

# comet 2290262-1500pF
path.append(os.path.join(root_snp_dir, sub_snp_dir[2]))
(C2290262_1500pF, Labels) = read_snp(path[-1], C2290262_1500pF, Zp, Zs, Labels, label_key_name="C2290262_1500pF")

# comet 2291830-1500pF
path.append(os.path.join(root_snp_dir, sub_snp_dir[3]))
(C2291830_1500pF, Labels) = read_snp(path[-1], C2291830_1500pF, Zp, Zs, Labels, label_key_name="C2291830_1500pF")

# GL172601310151-250pF
path.append(os.path.join(root_snp_dir, sub_snp_dir[5]))
(gl172601310151_250PF, Labels) = read_snp(path[-1], gl172601310151_250PF , Zp, Zs, Labels, label_key_name="gl172601310151")

# # GL202601311014-1500pF
path.append(os.path.join(root_snp_dir, sub_snp_dir[7]))
(gl202601311014_1500PF, Labels) = read_snp(path[-1], gl202601311014_1500PF , Zp, Zs, Labels, label_key_name="gl202601311014")

# GL172601310101-250pF
path.append(os.path.join(root_snp_dir, sub_snp_dir[4]))
(gl172601310101_250pF, Labels) = read_snp(path[-1], gl172601310101_250pF , Zp, Zs, Labels, label_key_name="gl172601310101")

# GL202511213901-1500pF
path.append(os.path.join(root_snp_dir, sub_snp_dir[6]))
(gl202511213901_1500pF, Labels) = read_snp(path[-1], gl202511213901_1500pF , Zp, Zs, Labels, label_key_name="gl202511213901")

# i个容值位置
for i in range(0, FileNum):
  plt.figure(i)
  fig_label = "C2207075_250pF"
  # fig_label = "C2290262_1500pF"

  # 250pF: 27M, 60M
  plt.title(f"{CenterFreq}MHz {Labels[fig_label][i]}")
  plt.plot(np.linspace(FreqShowStart / 1e6, FreqShowStop / 1e6, FreqShow_Num),
           C2207075_250pF[FreqShowStart_Num - 1:FreqShowStop_Num, i], linestyle='dashed', label='C2207075_250pF')
  plt.plot(np.linspace(FreqShowStart / 1e6, FreqShowStop / 1e6, FreqShow_Num),
           C2219619_250pF[FreqShowStart_Num - 1:FreqShowStop_Num, i], linestyle='dashed', label='C2219619_250pF')
  plt.plot(np.linspace(FreqShowStart / 1e6, FreqShowStop / 1e6, FreqShow_Num),
           gl172601310151_250PF[FreqShowStart_Num - 1:FreqShowStop_Num, i], linestyle='dashed', label='gl172601310151_250PF')
  plt.plot(np.linspace(FreqShowStart / 1e6, FreqShowStop / 1e6, FreqShow_Num),
           gl172601310101_250pF[FreqShowStart_Num - 1:FreqShowStop_Num, i], linestyle='dashed', label='gl172601310101_250pF')
  # print(gl172601310101_250pF[0, 1], gl172601310151_250PF[0, 1])

  # 1500pF: 2M
  # plt.title(f"{CenterFreq}MHz {Labels[fig_label][i]}")
  # plt.plot(np.linspace(FreqShowStart / 1e6, FreqShowStop / 1e6, FreqShow_Num),
  #          C2290262_1500pF[FreqShowStart_Num - 1:FreqShowStop_Num, i], linestyle='dashed', label='C2290262_1500pF')
  # plt.plot(np.linspace(FreqShowStart / 1e6, FreqShowStop / 1e6, FreqShow_Num),
  #          C2291830_1500pF[FreqShowStart_Num - 1:FreqShowStop_Num, i], linestyle='dashed', label='C2291830_1500pF')
  # plt.plot(np.linspace(FreqShowStart / 1e6, FreqShowStop / 1e6, FreqShow_Num),
  #          gl202601311014_1500PF[FreqShowStart_Num - 1:FreqShowStop_Num, i], linestyle='dashed', label='gl202601311014_1500PF')
  # plt.plot(np.linspace(FreqShowStart / 1e6, FreqShowStop / 1e6, FreqShow_Num),
  #          gl202511213901_1500pF[FreqShowStart_Num - 1:FreqShowStop_Num, i], linestyle='dashed', label='gl202511213901_1500pF')
  # print(Lables[i], (C1829302_1000pF[Freqnum_data, i]).real)

  plt.legend()
  plt.xlabel('Freq(MHz)', fontsize=12)
  plt.ylabel('Imag(Ω)', fontsize=12)
  plt.xticks(fontsize=12)
  plt.yticks(fontsize=12)
  plt.tight_layout()

  # plt.ylim(-60,-20)
  fig_dir = rf"D:\Users\Wxss\bin\WeLink\DownloadFiles\寄生参数图像-2\{CenterFreq}MHz"
  os.makedirs(fig_dir, exist_ok=True)
  plt.savefig(os.path.join(fig_dir, f"{Labels[fig_label][i]}.png"))
  # plt.show()

NUM = 10
# print(Lables[NUM], (C1829302_1000pF[Freqnum_data, NUM]).real)
# print(Lables[NUM], (C1852526_1000pF[Freqnum_data, NUM]).real)
# print(Lables[NUM], (C1868445_1000pF[Freqnum_data, NUM]).real)
# print(Lables[NUM], (gl63260131111_1000PF[Freqnum_data, NUM]).real)
# print(Lables[NUM], (gl632601311114_1000PF[Freqnum_data, NUM]).real)
#
'''

for i in range(0,FileNum):
    plt.figure(i) 
    plt.title(Lables[i])
    plt.plot(np.linspace(1, 20,int(N/10)),GL007_1000pF[0:int(N/10),i]-GL006_1000pF[0:int(N/10),i],linestyle='dashed',label='Diff') 

    print(Lables[i],abs(GL007_1000pF[Freqnum_data,i]-GL006_1000pF[Freqnum_data,i]))

    plt.xlabel('Freq(MHz)',fontsize=12)
    plt.ylabel('Imag(Ω)',fontsize=12)
    plt.xticks(fontsize=12)
    plt.yticks(fontsize=12)

    plt.ylim(-0.5,0.5)    

    plt.legend()

'''