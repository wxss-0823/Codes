#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2024/9/24 11:53
# @Author  : wxss
# @File    : SQlite3_OP.py

import sqlite3

conn = sqlite3.connect('sss.dat')
c = conn.cursor()

#
# for item in tables:
#     print(item)


c.execute('''CREATE TABLE COMPANY(
    ID INT PRIMARY KEY NOT NULL,
    NAME TEXT NOT NULL,
    AGE INT NOT NULL,
    ADDRESS CHAR(50),
    SALARY REAL)''')
conn.commit()
conn.close()
