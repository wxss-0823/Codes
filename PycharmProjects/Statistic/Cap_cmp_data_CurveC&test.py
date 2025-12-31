#!D:\Users\Anaconda\anaconda3\python.exe
# -*- coding: utf-8 -*-
# @Time    : 2025/12/27 9:16
# @Author  : wxss
# @File    : Cap_cmp_data_CurveC&test.py

import math
import os
import re
import traceback
from typing import List

import pandas as pd
import pdfplumber


def find_index(matrix: list,
               target: str) -> tuple | None:
  for i, row in enumerate(matrix):
    for j, value in enumerate(row):
      if value == target:
        return i, j
  return None


# Get curve C xlsx files
curveCDir = r'C:\Users\w00025121\Desktop\C曲线'
subdirList = next(os.walk(curveCDir))[1]
currentDirList = [curveCDir + "\\" + subdir for subdir in subdirList]
xlsxName = 'Curve-C Data CMP_tmp.xlsx'
pattern = r"\d{8}-\d{3}"
fileNum = 10
dataNum = 500

# Get filenames in batches. At least two levels of directories are required.
pdfFilesDir: List[List[str]] = [[] for _ in range(fileNum)]
pid = 0

# PDF files directory
for currentDir in currentDirList:
  for root, _, fNames in os.walk(currentDir):
    for file in fNames:
      if file.endswith(".pdf"):
        pdfFilesDir[pid].append(os.path.join(root, file))
  pid += 1

xlsxFilesDir: List[List[str]] = [[] for _ in range(fileNum)]

pid = 0
# XLSX files directory
for currentDir in currentDirList:
  for root, _, fNames in os.walk(currentDir):
    for file in fNames:
      if file.endswith(".xlsx") and file[0] != 'C' and file[0] != '~':
        xlsxFilesDir[pid].append(os.path.join(root, file))
        # with open("dir_rec.txt", 'a') as f:
        #   f.write(os.path.join(root, file) + '\n')
  pid += 1

# PDF title data
pdfTitleData = {
  'Serial NO': [],
  'Type': [],
  'C-min mechanical': [],
  'C-min test': [],
  'C-max mechanical': [],
  'C-max test': [],
  'Tmeasured min': [],
  'Tmeasured max': [],
  'C-min nominal': [],
  'C-min nominal test': [],
  'C-max nominal': [],
  'C-max nominal test': [],
}
xlsxDF = pd.DataFrame(pdfTitleData)

# Column data List
sno: List[List[str]] = [['' for _ in range(dataNum)] for _ in range(fileNum)]
sType: List[List[str]] = [['' for _ in range(dataNum)] for _ in range(fileNum)]
cMinMech: List[List[str]] = [['' for _ in range(dataNum)] for _ in range(fileNum)]
cMaxMech: List[List[str]] = [['' for _ in range(dataNum)] for _ in range(fileNum)]
cMinTest: List[List[str]] = [['' for _ in range(dataNum)] for _ in range(fileNum)]
cMaxTest: List[List[str]] = [['' for _ in range(dataNum)] for _ in range(fileNum)]
tMsMin: List[List[str]] = [['' for _ in range(dataNum)] for _ in range(fileNum)]
tMsMax: List[List[str]] = [['' for _ in range(dataNum)] for _ in range(fileNum)]
cMinNomi: List[List[str]] = [['' for _ in range(dataNum)] for _ in range(fileNum)]
cMaxNomi: List[List[str]] = [['' for _ in range(dataNum)] for _ in range(fileNum)]
cMinNT: List[List[str]] = [['' for _ in range(dataNum)] for _ in range(fileNum)]
cMaxNT: List[List[str]] = [['' for _ in range(dataNum)] for _ in range(fileNum)]

pdfFileDir = ''
batchIndex = 0

# Get PDF column 2D-list
for pdfFileBatch in pdfFilesDir:
  rowIndex = 0
  for pdfFileDir in pdfFileBatch:
    print(pdfFileDir)
    with pdfplumber.open(pdfFileDir) as pdf:
      pdfTables = pdf.pages[0].extract_tables()

      # Data position
      try:
        sno[batchIndex][rowIndex] = pdfTables[0][1][1]
        sType[batchIndex][rowIndex] = pdfTables[0][1][3]
        cMinMech[batchIndex][rowIndex] = pdfTables[1][1][4]
        cMaxMech[batchIndex][rowIndex] = pdfTables[1][9][4]
        cMinNomi[batchIndex][rowIndex] = pdfTables[1][2][4]
        cMaxNomi[batchIndex][rowIndex] = pdfTables[1][8][4]
        tMsMin[batchIndex][rowIndex] = pdfTables[1][1][8]
        tMsMax[batchIndex][rowIndex] = pdfTables[1][8][8]

      except IndexError as e:
        traceback.print_exc()

    rowIndex += 1
  batchIndex += 1

# sno = '2401270125'

for xlsxFileBatch in xlsxFilesDir:
  for xlsxFileDir in xlsxFileBatch:
    print(xlsxFileDir)
    try:
      xlsxTestDF = pd.read_excel(xlsxFileDir, sheet_name="步进CCWCW采集")
    except ValueError as e:
      continue
    posTuple = find_index(sno, re.search(r"\d{10}", xlsxFileDir).group(0))
    # Empty table
    if posTuple and xlsxTestDF.shape[0] > 100:
      # if re.search(r"\d{10}", xlsxFileDir).group(0) == '2504150303':
      #   with open("debug.txt", 'a') as f:
      #     f.write(str(xlsxTestDF.iat[1, 1]) + '\n')
      #     f.write(str(xlsxTestDF.iat[1, 2]) + '\n')
      try:
        # Get C mechanical test data
        cMinTest[posTuple[0]][posTuple[1]] = min(xlsxTestDF.iat[1, 1], xlsxTestDF.iat[1, 2])
        cMaxTest[posTuple[0]][posTuple[1]] = max(xlsxTestDF.iat[-1, 1], xlsxTestDF.iat[-1, 2])
        # Get C nominal test data
        # Calc nominal test data position by Tmeasured
        tMsMinRow = math.floor(math.fabs(float(tMsMin[posTuple[0]][posTuple[1]]) * (360 / 1.8)))
        tMsMinRow = tMsMinRow if tMsMinRow % 2 == 0 else tMsMinRow - 1
        tMsMaxRow = math.floor(
          (float(tMsMax[posTuple[0]][posTuple[1]]) - float(tMsMin[posTuple[0]][posTuple[1]])) * (360 / 1.8)
        )
        tMsMaxRow = tMsMaxRow if tMsMaxRow % 2 == 0 else tMsMaxRow - 1
        # Turn to col index
        tMsMinRow: int = int(tMsMinRow / 2 + 2)
        tMsMaxRow: int = int(tMsMaxRow / 2 + 2)
        # print(tMsMinRow)

        cMinNT[posTuple[0]][posTuple[1]] = min(xlsxTestDF.iat[tMsMinRow, 1], xlsxTestDF.iat[tMsMinRow, 2])
        try:
          cMaxNT[posTuple[0]][posTuple[1]] = max(xlsxTestDF.iat[tMsMaxRow, 1], xlsxTestDF.iat[tMsMaxRow, 2])
        except IndexError as e:
          cMaxNT[posTuple[0]][posTuple[1]] = max(xlsxTestDF.iat[-1, 1], xlsxTestDF.iat[-1, 2])
      except ValueError as e:
        traceback.print_exc()
        print("Might miss data corresponding to sno index")

# Synthesize table
batchIndex = 0
writer = pd.ExcelWriter(xlsxName, engine='openpyxl')
for xlsxFileBatch in xlsxFilesDir:
  if xlsxFileBatch:
    sheetName: str = re.search(pattern, str(xlsxFileBatch[0])).group(0)
    tableData = {
      'Serial NO': sno[batchIndex],
      'Type': sType[batchIndex],
      'C-min mechanical': cMinMech[batchIndex],
      'C-min test': cMinTest[batchIndex],
      'C-max mechanical': cMaxMech[batchIndex],
      'C-max test': cMaxTest[batchIndex],
      'Tmeasured min': tMsMin[batchIndex],
      'Tmeasured max': tMsMax[batchIndex],
      'C-min nominal': cMinNomi[batchIndex],
      'C-min nominal test': cMinNT[batchIndex],
      'C-max nominal': cMaxNomi[batchIndex],
      'C-max nominal test': cMaxNT[batchIndex],
    }
    xlsxDF = pd.DataFrame(tableData)
    xlsxDF.to_excel(writer, sheet_name=sheetName, index=False)
    # xlsxDF.drop(xlsxDF.index, inplace=True)
    batchIndex += 1
writer.close()
