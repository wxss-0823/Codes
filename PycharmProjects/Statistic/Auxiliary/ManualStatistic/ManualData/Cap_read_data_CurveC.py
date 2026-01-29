#!D:\Users\Anaconda\anaconda3\python.exe
# -*- coding: utf-8 -*-
# @Time    : 2025/12/25 14:36
# @Author  : wxss
# @File    : Cap_read_data_CurveC.py


import os
import time
from typing import List

import pandas as pd
import re
import pdfplumber


def find_index(matrix : list,
               target : str) -> tuple | None :
  for i, row in enumerate(matrix):
    for j, col in enumerate(row):
      for k, value in enumerate(col):
        if value == target:
          return i, j, k
  return None

# Get curve C xlsx files
curveCDir = r'C:\Users\w00025121\Desktop\C曲线'
subdirList = next(os.walk(curveCDir))[1]
currentDirList = [curveCDir + "\\" + subdir for subdir in subdirList]
xlsxName = 'Curve-C Data_tmp.xlsx'
pattern = r"\d{8}-\d{3}"
fileNum = 10
sheetNameList = [re.search(pattern, currentDir).group(0)
  for currentDir in currentDirList
]

# Get filenames in batches. At least two levels of directories are required.
pdfFilesDir: List[List[str]] = [[] for _ in range(fileNum)]
pid = 0
for currentDir in currentDirList:
  for root, _, fNames in os.walk(currentDir):
    for file in fNames:
      if file.endswith(".pdf"):
        pdfFilesDir[pid].append(os.path.join(root, file))
  pid += 1

# PDF title data
pdfTitleData = {
  #'File name': [],
  'Serial NO': [],
  'Type': [],
  'C-min mechanical': [],
  'C-max mechanical': [],
  'Slope measured': [],
  'Measured peak': [],
  'Start torque': [],
  'Diff of CW and CCW': []
}
xlsxDF = pd.DataFrame(pdfTitleData)

# main
pdfFileDir = ''
writer = pd.ExcelWriter(xlsxName, engine='openpyxl')

for pdfFileBatch in pdfFilesDir:
  for pdfFileDir in pdfFileBatch:
    print(pdfFileDir)
    with pdfplumber.open(pdfFileDir) as pdf:
      pdfTables = pdf.pages[0].extract_tables()
      # print(pdfTables)
      # print(find_index(pdfTables, "Measured Peak:"))

      # Data position
      try:
        lineData = {
          #'File name': pdfFile,
          'Serial NO': pdfTables[0][1][1],                      # Serial NO: (1, 2, 2)
          'Type': pdfTables[0][1][3],                           # Type: (1, 2 ,4)
          'C-min mechanical': pdfTables[1][1][4],               # C-min mechanical: (2, 2, 5)
          'C-max mechanical': pdfTables[1][9][4],               # C-max mechanical: (2, 10, 5)
          'Slope measured': pdfTables[3][1][4] + ' pF/T',       # Slope measured: (4, 2, 5)
          'Measured peak': pdfTables[5][1][1],                  # Measured Peak: (6, 2, 2)
          'Start torque': pdfTables[5][2][1],                   # Start Torque: (6, 3 ,2)
          'Diff of CW and CCW': re.search(r"\d+.\d+", pdfTables[6][0][1]).group(0)    # Diff of CW and CCW: (7, 1, 2)
        }

        xlsxDF = xlsxDF.append(lineData, ignore_index=True)
      except IndexError as e:
        print(f"Missing SNO & Type: {e}\n")
        with open("Failed Data List.txt", 'a', encoding="utf-8") as f:
          f.write('[' + time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())) + ']  ')
          f.write('Missing SNO，Type: ')
          f.write(str(pdfFileDir) + '\n')
        continue
      except AttributeError as e:
        print(f"Missing Torque: {e}\n")
        with open("Failed Data List.txt", 'a', encoding="utf-8") as f:
          f.write('[' + time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())) + ']  ')
          f.write('Missing Torque: ')
          f.write(str(pdfTables[0][1][1]) + '\n')

        lineData = {
          #'File name': pdfFile,
          'Serial NO': pdfTables[0][1][1],                      # Serial NO: (1, 2, 2)
          'Type': pdfTables[0][1][3],                           # Type: (1, 2 ,4)
          'C-min mechanical': pdfTables[1][1][4],               # C-min mechanical: (2, 2, 5)
          'C-max mechanical': pdfTables[1][7][4],               # C-max mechanical: (3, 8, 5)
          'Slope measured': pdfTables[3][1][4] + ' pF/T',       # Slope measured: (4, 2, 5)
          'Measured peak': '',                                  # Measured Peak: (6, 2, 2)
          'Start torque': '',                                   # Start Torque: (6, 3 ,2)
          'Diff of CW and CCW': re.search(r"\d+.\d+", pdfTables[5][0][1]).group(0)    # Diff of CW and CCW: (6, 1, 2)
        }

        xlsxDF = xlsxDF._append(lineData, ignore_index=True)

  # Write to Excel file
  sheetName = re.search(pattern, str(pdfFileDir)).group(0)
  xlsxDF.to_excel(writer, sheet_name=sheetName, index=False)
  xlsxDF.drop(xlsxDF.index, inplace=True)

writer.close()
