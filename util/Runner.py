#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2020/10/16 14:11
# @Author  : hongjun.xiao
# @File    : Runner.py
# @system  : WenJiang

import unittest
import os
import time
from BeautifulReport import BeautifulReport
from util import EmailConfig
from util import LogRecord
from util import DingdingRebot
log=LogRecord.LogRd("Runner").getLog()
if __name__ == '__main__':
    log.info("***********开始执行测试************")
    suite=unittest.defaultTestLoader.discover(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))+"\case",pattern="GovernmentCase.py")
    report_dir=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))+"\\testreport"
    result=BeautifulReport(suite)
    result.report(filename="UIAutoTestReport",description=time.strftime("%Y-%m-%d",time.localtime())+"测试结果",log_path=report_dir)

    P=result.success_count.__abs__()
    F=result.failure_count.__abs__()
    DingdingRebot.Rebort(P,F)
    log.info("************生成测试报告成功********")
    #EmailConfig.emailSend("xiaohongjun1093@dingtalk.com")



