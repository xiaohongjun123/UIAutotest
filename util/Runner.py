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
from util import EmailConfig,ProjectPath,LogRecord,DingdingRebot

log=LogRecord.LogRd("Runner").getLog()
if __name__ == '__main__':
    log.info("***********开始执行测试************")
    suite=unittest.defaultTestLoader.discover(ProjectPath.PtPath("/case"),pattern="GovernmentCase.py")
    report_dir=ProjectPath.PtPath("/testreport")
    result=BeautifulReport(suite)
    result.report(filename="UIAutoTestReport_one",description=time.strftime("%Y-%m-%d-%H-%M-%S",time.localtime())+"测试结果",log_path=report_dir)

    P=result.success_count.__abs__()
    F=result.failure_count.__abs__()
    AllCaseNum=P+F
    print(AllCaseNum)
    #DingdingRebot.Rebort(P,F)
    if P!=AllCaseNum:
        suite = unittest.defaultTestLoader.discover(ProjectPath.PtPath("/case"), pattern="ExcuteTwoCase.py")
        report_dir = ProjectPath.PtPath("/testreport")
        result = BeautifulReport(suite)
        result.report(filename="UIAutoTestReport_two", description=time.strftime("%Y-%m-%d-%H-%M-%S", time.localtime()) + "错误用例二次执行测试结果",
                      log_path=report_dir)

    log.info("************生成测试报告成功********")
    #print(P,F)
    EmailConfig.emailSend("xiaohongjun1093@dingtalk.com","1ti_naq4rifprl@dingtalk.com","yuchangjun9092@dingtalk.com","liangfurong2469@dingtalk.com","liaowanlan2939@dingtalk.com","zhangyiyi5534@dingtalk.com")
    #EmailConfig.emailSend("xiaohongjun1093@dingtalk.com")
    os.system("rm -f /root/uitest/testreport/UI*")



