#!D:\Users\Anaconda\anaconda3\python.exe
# -*- coding: utf-8 -*-
# @Time    : 2026/5/6 10:16
# @Author  : Coffee
# @Project : Pycharm
# @File    : BatchArchived.py


import zipfile
import os
import re

from flask_restful.fields import Fixed


def BatchArchive(
    root_dir: str,
    data_date: str,
    **kwargs
) -> None:
  archive_dir = ""
  arc_type = kwargs.get("archive_type")
  cap_type = kwargs.get("cap_type")
  match arc_type:
    case 'IQC':
      iqc_archive_dir = root_dir + r"\02IQC"
      match cap_type:
        case 'Variable':
          archive_dir = iqc_archive_dir + r"\0Variable\2026" + data_date
        case 'Trimmer':
          archive_dir = iqc_archive_dir + r"\1Trimmer" + data_date
        case 'Fixed':
          archive_dir = iqc_archive_dir + r"\2Fixed" + data_date
        case 'Matrix':
          archive_dir = iqc_archive_dir + r"\3Matrix" + data_date
    case 'COA':
      archive_dir = root_dir + r"\01COA" + data_date
    case 'POO':
      archive_dir = root_dir + r"\04FigureArchive" + r"\1上下电找零" + data_date
    case 'CAP':
      cap_archive_dir = root_dir + r"\04FigureArchive" + r"\0容值精度"
      match cap_type:
        case 'Coa Cap':
          archive_dir = cap_archive_dir + r"\COA" + data_date
        case 'Iqc Cap':
          archive_dir = cap_archive_dir + r"\IQC" + data_date
    case _:
      archive_dir = ""
      print("Archive Type Error!")

  sub_dirs = next(os.walk(archive_dir))[1]
  date_sn_set = set()

  match arc_type:
    case "IQC" | "COA":
      # IQC & COA 文件名模式
      filename_ptn = r"\d{8} 08190\d{3}-00[1-2]"
      for sub_dir in sub_dirs:
        if re.search(filename_ptn, sub_dir):
          date_sn_set.add(re.search(filename_ptn, sub_dir).group(0))
    case "POO" | "CAP":
      # POO, 容值精度 文件名模式
      date_sn_set.add(r"One")
    case _:
      pass
      # filename_ptn = ""

  for date_sn in date_sn_set:
    for sub_dir in sub_dirs:
      match arc_type:
        case "COA":
          zip_name = date_sn + "交付件COA.zip"
        case "IQC":
          zip_name = date_sn + ".zip"
        case "POO" | "CAP":
          zip_name = sub_dir + ".zip"
        case _:
          zip_name = ""
      if arc_type == "COA" or arc_type == "IQC":
        if re.search(date_sn, sub_dir):
          zip_path = os.path.join(archive_dir, zip_name)
        else:
          zip_path = "error.tmp"
      elif arc_type == "POO" or arc_type == "CAP":
        zip_path = os.path.join(archive_dir, zip_name)
      else:
        zip_path = "error.tmp"
      if zip_path != "error.tmp":
        mode: Literal["r", "w", "x", "a"] = "a" if os.path.exists(zip_path) else "w"
        with zipfile.ZipFile(zip_path, mode, zipfile.ZIP_DEFLATED) as zip_file:
          print(f"Compress: {zip_path}.")
          for root, dirs, files in os.walk(os.path.join(archive_dir, sub_dir)):
            for file in files:
              file_path = os.path.join(root, file)
              archived_name = os.path.relpath(file_path, start=archive_dir)
              zip_file.write(file_path, archived_name)

if __name__ == "__main__":
  data_dir = r"D:\Users\Wxss\01Project\01VVC\03Data"
  fig_dir = r"D:\Users\Wxss\01Project\01VVC\03Data\04FigureArchive"
  date = r"\20260807"
  archive_type: Literal["IQC", "COA", "POO", "CAP"] = "POO"
  cap_type_list = ["Variable", "Trimmer", "Fixed", "Matrix", "Coa Cap", "Iqc Cap", ""]
  BatchArchive(data_dir, date, archive_type=archive_type, cap_type=cap_type_list[6])