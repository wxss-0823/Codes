##################################################################################################
#
#   Title: 把文件路径写入CSV文件(ADS仿真使用)
#   Project:
#   Author: Rainey Liao
#   Date: 07.21.2021
#
#
##################################################################################################



import os
import csv

path1 = r"D:/Users/Wxss/99pureDir/SNP/2506210102/" #读取文件
path2 = r"D:/Users/Wxss/99pureDir/SNP/"  #写入文件
file_list= os.listdir(path1)

# 获取创建时间
file_mtime_list = [(file_name, os.path.getmtime(os.path.join(path1, file_name))) for file_name in file_list]

# 按创建时间排序
file_ctime_sorted = sorted(file_mtime_list, key=lambda x: x[1])


with open(path2+"/CAP20260108.csv", 'w') as f:  #/xx.csv中xx为保存的文件名
    # ADS 中组件名称 SNP1
    content = 'SNP1.File'
    f.write(content)
    for item in file_ctime_sorted:
        content = '\n'+path1 + item[0]
        f.write(content)
