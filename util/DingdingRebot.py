#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2020/10/16 16:41
# @Author  : hongjun.xiao
# @File    : DingdingRebot.py
# @system  : WenJiang





import time
import hmac
import hashlib
import base64
import urllib.parse
import json
import requests



timestamp = str(round(time.time() * 1000))
secret = 'this is secret'
secret_enc = secret.encode('utf-8')
string_to_sign = '{}\n{}'.format(timestamp, secret)
string_to_sign_enc = string_to_sign.encode('utf-8')
hmac_code = hmac.new(secret_enc, string_to_sign_enc, digestmod=hashlib.sha256).digest()
sign = urllib.parse.quote_plus(base64.b64encode(hmac_code))


url=r"https://oapi.dingtalk.com/robot/send?access_token=5b389db45f3cd6f6cd227dc77f21897eee606056630eb29e2c1a791b93618531&timestamp=%s&sign=%s"%(timestamp,sign)
#url=r"https://oapi.dingtalk.com/robot/send?access_token=74a7c4aeee3e746af0ff0c46c0c46a46481a1add1c4ab1567aa917c5742dec85&timestamp=%s&sign=%s"%(timestamp,sign)
print(url)
def Rebort(P,F):
    header={"Content-Type":"application/json; charset=utf-8"}
    re_url=url

    data={
    "msgtype": "text",
    "text": {
        "content": "UI自动化执行完成，详情请查看邮件。通过:%s,失败:%s"%(P,F)
    },
    "at": {
        "isAtAll":False
}
    }
    r=requests.post(re_url,data=json.dumps(data),headers=header)
    print(r.json())
if __name__=="__main__":
    Rebort(30,2)
