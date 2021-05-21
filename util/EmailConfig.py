#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2020/10/16 16:41
# @Author  : hongjun.xiao
# @File    : EmailConfig
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
from util import PicScreenShot,ProjectPath
from mimetypes import guess_type

def emailSend(*recivers):
#--------邮件服务器--------
    mail_host = 'smtp.sina.com'
    mail_user = 'autowengjiang@sina.com'
    mail_passwd = 'dc77e8dbc727e611'
    mail_send = 'autowengjiang@sina.com'
    message=MIMEMultipart("alternative")#定义邮件可以发送超文本内容
    message["From"]=Header("autowengjiang@sina.com")
    message["To"]=Header("Group","utf-8")

    #够造邮件主题
    subject="自动化"+str(time.strftime("%Y-%m-%d %H:%M:%S",time.localtime()))
    message["Subject"]=Header(subject,"utf-8")
    
    #构造正文内容，并且插入图片
    url_one=ProjectPath.PtPath("/testreport/UIAutoTestReport_one.html")
    screenshot_name="screenshot_one.png"
    screenshot_path=ProjectPath.PtPath("/testreport/"+screenshot_name)
    PicScreenShot.ScreenPic(url_one,screenshot_name,screenshot_path)
    Pic_two=PicScreenShot.ScreenPicTwo()
    if os.path.exists(Pic_two[0])==True:
        Pic_url=[screenshot_path,Pic_two[1]]
        for i,Pic_image in enumerate(Pic_url):
            (mimetype, encoding) = guess_type(Pic_image)
            (maintype, subtype) = mimetype.split('/')
            with open(Pic_image,"rb") as fp:
                msgimage = MIMEImage(fp.read(),**{'_subtype': subtype})
                fp.close()
                msgimage.add_header("Content-ID","<image%d>"%(i+1))
                message.attach(msgimage)
        html = '''
        <html>
            <head></head>
            <body>
                <p>本来结果如下，详情请看附件：<br>
                    <br><img src="cid:image1"></br>
                    错误用例重跑结果如下：<br>
                    <br><img src="cid:image2"></br>
                </p>
            </body>
        </html>
        '''
    else:
        fp=open(screenshot_path,"rb")
        msgimage=MIMEImage(fp.read())
        fp.close()
        msgimage.add_header("Content-ID","<image1>")
        message.attach(msgimage)
        html='''
        <html>
            <head></head>
            <body>
                <p>本来结果如下，详情请看附件：<br>
                    <br><img src="cid:image1"></br>
                </p>
            </body>
        </html>
        '''

    #html=open(r'D:\project\WenJiang_selenium\\testreport\UIAutoTestReport.html',"rb")
    #html1=html.read()
    #html.close()

    htl=MIMEText(html,"html",_charset="utf-8")
    message.attach(htl)

    #构造附件
    att=MIMEText(open(ProjectPath.PtPath("/testreport/UIAutoTestReport_one.html"),"rb").read(),"base64","utf-8")
    att['Content-Type'] = 'application/octet-stream'
    att['Content-Disposition'] = "attachment;filename=UIAutoReport_one.html"
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
    emailSend("xiaohongjun1093@dingtalk.com")