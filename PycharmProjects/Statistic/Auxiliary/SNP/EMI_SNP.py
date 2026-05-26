#!D:\Users\Anaconda\anaconda3\python.exe
# -*- coding: utf-8 -*-
# @Time    : 2026/4/23 14:12
# @Author  : Coffee
# @Project : Pycharm
# @File    : EMI_SNP.py


import os

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import skrf as rf
import scipy.io as sio

com_snp_dir = r"D:\Users\Share\实验室文件\5_磁芯电感_20260213\EMI-COM-260423.S1P"
dif_snp_dir = r"D:\Users\Share\实验室文件\5_磁芯电感_20260213\EMI-DIF-260423.S1P"

com_network = rf.Network(com_snp_dir)
com_freq = com_network.frequency.f
com_s11 = com_network.s[:, 0, 0]
com_s11a = abs(com_s11)

dif_network = rf.Network(dif_snp_dir)
dif_freq = dif_network.frequency.f
dif_s11 = dif_network.s[:, 0, 0]
dif_s11a = abs(dif_s11)

plt.rcParams['font.sans-serif'] = ['SimHei']
plt.figure(figsize=(8, 8), dpi=100, facecolor="w")
plt.subplot(2, 1, 1)
plt.plot(com_freq, com_s11a)
plt.title('共模 S11')
plt.subplot(2, 1, 2)
plt.plot(dif_freq, dif_s11a)
plt.title('差模 S11')
plt.show()