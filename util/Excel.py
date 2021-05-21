#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2020/10/16 14:11
# @Author  : hongjun.xiao
# @File    : Excel.py
# @system  : WenJiang

import os,sys
curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.append(rootPath)

from openpyxl import load_workbook
from util import ProjectPath

#读取Excel的方法
def ReadExcel():
    wb=load_workbook(ProjectPath.PtPath("/casedata/GovernmentCaseData.xlsx"))
    sheet=wb["Sheet1"]
    allvalue=[]
    for row in list(sheet.rows)[1:sheet.max_row]:
        value=[]
        for column in range(0,sheet.max_column):
            value.append(row[column].value)
        if value[2]=="是":
            allvalue.append(value)
        else:
            continue
    return allvalue

def ExecuteTwo():
    wb=load_workbook(ProjectPath.PtPath("/casedata/GovernmentCaseData.xlsx"))
    sheet=wb["Sheet1"]
    allvalue=[]
    for row in list(sheet.rows)[1:sheet.max_row]:
        value=[]
        for column in range(0,sheet.max_column):
            value.append(row[column].value)
        if value[1]=="Fail":
            allvalue.append(value)
        else:
            continue
    return allvalue


def WriteExcel(row,results):
    wb=load_workbook(ProjectPath.PtPath("/casedata/GovernmentCaseData.xlsx"))
    sheet=wb["Sheet1"]
    sheet.cell(row=row,column=2).value=results
    wb.save(ProjectPath.PtPath("/casedata/GovernmentCaseData.xlsx"))



if __name__=="__main__":
    print(ReadExcel())



