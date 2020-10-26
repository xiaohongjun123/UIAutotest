#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2020/10/16 14:11
# @Author  : hongjun.xiao
# @File    : LogRecord.py
# @system  : WenJiang

import logging
import time
import os
#日志记录
class LogRd(object):

    #构造函数，初始化logger名称和定义记录报错等级
    def __init__(self,logger_name):
        self.logger=logging.getLogger(logger_name)
        self.logger.setLevel(logging.INFO)
        rq=time.strftime("%Y-%m-%d-%H-%M-%S",time.localtime())
        #获取当前文件的上一层目录的绝对路径
        log_path=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        #日志文件名称,下面两个是等价的
        #all_log_name=os.path.join(log_path+"\log",rq+".log")
        all_log_name =log_path + "\log\\"+rq + ".log"
        err_log_name=os.path.join(log_path+"\log",rq+"error.log")
        #定义log输出方式以及输出日志等级
        fh=logging.FileHandler(all_log_name)
        fh.setLevel(logging.DEBUG)
        eh=logging.FileHandler(err_log_name)
        eh.setLevel(logging.ERROR)
        ch=logging.StreamHandler()
        ch.setLevel(logging.INFO)
        #定义输出格式
        all_log_formatter=logging.Formatter("%(asctime)s-%(name)s-%(levelname)s-%(message)s")
        err_log_formatter=logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(module)s  - %(lineno)s - %(message)s')
        #设置输入log的格式
        fh.setFormatter(all_log_formatter)
        eh.setFormatter(err_log_formatter)
        ch.setFormatter(all_log_formatter)
        self.logger.addHandler(fh)
        self.logger.addHandler(eh)
        self.logger.addHandler(ch)

    def getLog(self):
        return self.logger

if __name__=="__main__":
    log=LogRd("test").getLog()
    a="hahah"
    log.info("测试信息-%s"%(str(a)))
    log.error("错误信息")