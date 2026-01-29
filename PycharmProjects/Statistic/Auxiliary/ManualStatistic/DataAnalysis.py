#!D:\Users\Anaconda\anaconda3\python.exe
# -*- coding: utf-8 -*-
# @Time    : 26/01/25 01:37
# @Author  : Coffee
# @Project : Statistic
# @File    : DataAnalysis.py


import os


class DataAnalysis:
  """
  Data Analysis Class
  """
  def __init__(self, file_dir, file_type='.xlsx'):
    """
    Initialize DataAnalysis class:
    :param file_dir:
    :param file_type:
    """

    self.file_dir = file_dir
    self.file_type = file_type

    print(f"Loading file type: xxx{self.file_type} from {self.file_dir}...")

    self.files_dir_list: list[str] = []

    for root_dir, dirs, files in os.walk(self.file_dir):
      for file in files:
        # Read files with input suffix and exclude temp files
        if file.endswith(self.file_type) and not file[0] == '~':
          # Append file directory
          self.files_dir_list.append(os.path.join(root_dir, file))

    print(f"Load {len(self.files_dir_list)} files.")

  def read_snp_data(self, s_parameter=[1, 1]):


    return self

