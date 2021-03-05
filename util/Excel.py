#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2020/10/16 14:11
# @Author  : hongjun.xiao
# @File    : Excel.py
# @system  : WenJiang


from openpyxl import load_workbook
import os

#读取Excel的方法
def ReadExcel():
    wb=load_workbook(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))+"\casedata\GovernmentCaseData.xlsx")
    sheet=wb["Sheet1"]
    allvalue=[]
    for row in list(sheet.rows)[1:sheet.max_row]:
        value=[]
        for column in range(1,sheet.max_column):
            value.append(row[column].value)
        if value[0]=="是":
            allvalue.append(value)
        else:
            continue
    return allvalue


if __name__=="__main__":
    print(ReadExcel())




