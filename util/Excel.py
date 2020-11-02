#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2020/10/16 14:11
# @Author  : hongjun.xiao
# @File    : Excel.py
# @system  : WenJiang

import sys
import os
curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.append(rootPath)
from openpyxl import load_workbook

#读取Excel的方法
def ReadExcel():
    wb=load_workbook(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))+"/casedata/GovernmentCaseData.xlsx")
    sheet=wb["Sheet1"]
    allvalue=[]
    for row in list(sheet.rows)[2:sheet.max_row]:
        value=[]
        for column in range(1,sheet.max_column-1):
            value.append(row[column].value)
        allvalue.append(value)
    return allvalue


if __name__=="__main__":
    print(ReadExcel())




