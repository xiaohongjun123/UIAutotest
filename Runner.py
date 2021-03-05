#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2020/10/16 14:11
# @Author  : hongjun.xiao
# @File    : Runner.py
# @system  : WenJiang
import sys
import os
curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.append(rootPath)
import unittest
import time
from BeautifulReport import BeautifulReport
from util import EmailConfig
from util import LogRecord
log=LogRecord.LogRd("Runner").getLog()
if __name__ == '__main__':
    log.info("***********开始执行测试************")
    print(os.path.dirname(os.path.abspath(__file__))+"/case")
    suite=unittest.defaultTestLoader.discover(os.path.dirname(os.path.abspath(__file__))+"/case",pattern="GovernmentCase.py")
    report_dir=os.path.dirname(os.path.abspath(__file__))+"/testreport"
    result=BeautifulReport(suite)
    result.report(filename="UIAutoTestReport",description=time.strftime("%Y-%m-%d",time.localtime())+"测试结果",log_path=report_dir)
    log.info("************生成测试报告成功********")
    EmailConfig.emailSend("xiaohongjun1093@dingtalk.com")



