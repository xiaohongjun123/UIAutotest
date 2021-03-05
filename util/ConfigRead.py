#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2020/10/16 14:11
# @Author  : hongjun.xiao
# @File    : ConfigRead.py
# @system  : WenJiang



#配置文件实例化
import os
from configobj import ConfigObj
config=ConfigObj(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))+"/configfile/Config.ini",encoding="UTF-8")



'''
f:父级
s:子级
value:内容
'''

#读取文件
def read_ini(f,s):
    data=config[f][s]
    return data

#修改数据
def write_ini(f,s,value):
    config[f][s]=value
    config.write()

if __name__=="__main__":
    print(read_ini("GovernmentTestUrl","QA"))
