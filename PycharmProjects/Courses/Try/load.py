# coding=utf-8

import sys

import warnings

sys.dont_write_bytecode = True

warnings.filterwarnings("ignore")

f = open("./uid.csv", "r")

bid = []

line = f.readline()
while line:
    brand_id = line.strip().split(',')

    bid.append(brand_id)

    line = f.readline()

f.close()
