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
log=LogRecord.LogRd("GovernmentCaseLog").getLog()
if __name__ == '__main__':
    log.info("开始执行测试")
    suite=unittest.defaultTestLoader.discover(r"D:\project\WenJiang_selenium\case",pattern="GovernmentCase.py")
    report_dir=r"D:\project\WenJiang_selenium\testreport"
    result=BeautifulReport(suite)
    result.report(filename="UI自动化测试报告",description=time.strftime("%Y-%m-%d",time.localtime())+"测试结果",log_path=report_dir)
    log.info("生成测试报告成功")
    EmailConfig.emailSend("xiaohongjun1093@dingtalk.com")



