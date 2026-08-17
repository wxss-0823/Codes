#!D:\Users\Anaconda\anaconda3\python.exe
# -*- coding: utf-8 -*-
# @Time    : 2026/7/15 18:48
# @Author  : Coffee
# @Project : Pycharm
# @File    : HFSSAutoAddXMarker.py


import ScriptEnv

# 1. 初始化 HFSS 桌面环境
ScriptEnv.Initialize("Ansoft.ElectronicsDesktop")
oDesktop.RestoreWindow()

# 2. 获取当前激活的项目
oProject = oDesktop.GetActiveProject()
if oProject is None:
    raise Exception("没有打开任何 HFSS 项目")

# 3. 获取当前激活的设计（关键步骤）
oDesign = oProject.GetActiveDesign()
if oDesign is None:
    raise Exception("没有激活的设计")

# 4. 通过 oDesign 获取报告模块
oModule = oDesign.GetModule("ReportSetup")

# Var
report_name = "MP_20260817"

# 频点列表
frequencies = [2e6, 13.56e6, 27e6, 40e6, 60e6, 80e6, 100e6, 120e6]
marker_names = ["2MHz", "13MHz", "27MHz", "40MHz", "60MHz", "80MHz", "100MHz", "120MHz"]

# 在指定报告的指定频点添加X轴Marker
for name, freq in zip(marker_names, frequencies):
  oModule.AddCartesianXMarker(report_name, name, freq)
