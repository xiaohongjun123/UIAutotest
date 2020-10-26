#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2020/10/16 16:41
# @Author  : hongjun.xiao
# @File    : Runner.py
# @system  : WenJiang


import smtplib
from email.mime.text import MIMEText
from email.header import Header
import time
from email.mime.multipart import MIMEMultipart
import os

def emailSend(*recivers):
#--------邮件服务器--------
    mail_host = 'smtp.qq.com'
    mail_user = '879337649@qq.com'
    mail_passwd = 'zjlsdbxqjujgbdga'
    mail_send = 'uiautotest@qq.com'
    message=MIMEMultipart()
    message["From"]=Header("UIAutoTest","utf-8")
    message["To"]=Header("Group","utf-8")
    #够造邮件主题
    subject="UIAuto测试报告"+str(time.strftime("%Y-%m-%d %H:%M:%S",time.localtime()))
    message["Subject"]=Header(subject,"utf-8")
    #构造正文内容
    message.attach(MIMEText("本轮自动化测试结果如下：","plain","utf-8"))
    #构造附件
    att=MIMEText(open(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))+"\\testreport\\UI自动化测试报告.html","rb").read(),"base64","utf-8")
    att['Content-Type'] = 'application/octet-stream'
    att['Content-Disposition'] = "attachment;filename='UI自动化测试报告.html'"
    message.attach(att)
    try:
        smtpobj=smtplib.SMTP_SSL(mail_host,465)
        smtpobj.set_debuglevel(1)
        smtpobj.login(mail_user,mail_passwd)
        smtpobj.sendmail(mail_send,recivers,message.as_string())
        print('send sucessful')
    except smtplib.SMTPException as e:
        print(e)
if __name__=="__main__":
    emailSend("979669145@qq.com","xiaohongjun1093@dingtalk.com")
