#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2020/10/16 14:11
# @Author  : hongjun.xiao
# @File    : LoginCommon.py
# @system  : WenJiang



import sys
import os
curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.append(rootPath)
from util import ConfigRead
from selenium import webdriver
import time
from selenium.common.exceptions import NoSuchElementException
import traceback
from selenium.webdriver.chrome.options import Options


#将登陆配置为模块方便调用
def Loginmode():
    options = Options()
    options.add_argument("--disable-notifications")
    options.add_argument("--disable-infobars")
    options.add_argument('--window-size=1280x1024')
    options.add_argument('--start-maximized')
    options.add_argument("--mute-audio")
    options.add_argument('--disable-dev-shm-usage')
    options.add_argument('--no-sandbox')
    options.add_experimental_option('excludeSwitches', ['enable-automation'])
    #prefs = {"profile.managed_default_content_settings.images": 2}
    #options.add_experimental_option("prefs", prefs)

    options.add_argument("--headless")
    options.add_argument('--disable-gpu')
    driver = webdriver.Chrome(executable_path="/opt/google/chrome/chromedriver", options=options)
    driver.get(ConfigRead.read_ini("GovernmentTestUrl","PD"))
    driver.implicitly_wait(10)
    try:
        driver.find_element_by_xpath('''//*[@id="app"]/div/div[1]/div/div/div/div[2]/div/form/div[1]/div/div/input''').send_keys(ConfigRead.read_ini("GovernmentAccount","PD"))
        driver.find_element_by_xpath('''//*[@id="app"]/div/div[1]/div/div/div/div[2]/div/form/div[2]/div/div/input''').send_keys(ConfigRead.read_ini("GovernmentPwd","PD"))
        driver.find_element_by_xpath('''//*[@id="app"]/div/div[1]/div/div/div/div[2]/div/form/div[4]/div/button/span''').click()
        time.sleep(2)
        print(driver.title)
    except NoSuchElementException as e:
        print(e)
    return driver
if __name__=="__main__":
    Loginmode()

