#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2020/10/16 16:41
# @Author  : hongjun.xiao
# @File    : Runner.py
# @system  : WenJiang

import sys
import os
curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.append(rootPath)
import smtplib
from email.mime.text import MIMEText
from email.header import Header
import time
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
import os
from util import PicScreenShot

def emailSend(*recivers):
#--------邮件服务器--------
    mail_host = 'smtp.qq.com'
    mail_user = '879337649@qq.com'
    mail_passwd = 'zjlsdbxqjujgbdga'
    mail_send = 'uiautotest@qq.com'
    message=MIMEMultipart("alternative")
    message["From"]=Header("UIAutoTest","utf-8")
    message["To"]=Header("Group","utf-8")
    print("构造邮件")

    #够造邮件主题
    subject="UIAuto测试报告"+str(time.strftime("%Y-%m-%d %H:%M:%S",time.localtime()))
    message["Subject"]=Header(subject,"utf-8")
    print("构造主题")
    
    #构造正文内容，并且插入图片
    PicScreenShot.ScreenPic()
    print(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))+"/testreport/"+"Screemshot.png")
    fp=open(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))+"/testreport/"+"Screemshot.png","rb")
    msgimage=MIMEImage(fp.read())
    fp.close()
    print("拿到图片")
    msgimage.add_header("Content-ID","<image1>")
    message.attach(msgimage)
    html='''
    <html>
        <head></head>
        <body>
            <p>本次测试结果如下，详情请使用chrome浏览器打开附件查看：<br>
                <br><img src="cid:image1"></br>
            </p>
        </body>
    </html>
    '''
    htl=MIMEText(html,"html",_charset="utf-8")
    message.attach(htl)
    print("构造正文")

    #构造附件
    att=MIMEText(open(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))+"/testreport/UIAutoTestReport.html","rb").read(),"base64","utf-8")
    print(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))+"/UIAutoTestReport.html")
    att['Content-Type'] = 'application/octet-stream'
    att['Content-Disposition'] = "attachment;filename=UIAutoTestReport.html"
    message.attach(att)
    print("构造附件")

    try:
        smtpobj=smtplib.SMTP_SSL(mail_host,465)
        smtpobj.set_debuglevel(1)
        smtpobj.login(mail_user,mail_passwd)
        smtpobj.sendmail(mail_send,recivers,message.as_string())
        print('send sucessful')
    except smtplib.SMTPException as e:
        print(e)
if __name__=="__main__":
    emailSend("xiaohongjun1093@dingtalk.com")
