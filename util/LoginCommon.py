#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2020/10/16 14:11
# @Author  : hongjun.xiao
# @File    : LoginCommon.py
# @system  : WenJiang

from util import ConfigRead
from selenium import webdriver
import time
from selenium.common.exceptions import NoSuchElementException
import traceback

#将登陆配置为模块方便调用
def Loginmode():
    driver=webdriver.Chrome()
    driver.get(ConfigRead.read_ini("GovernmentTestUrl","PD"))
    #driver.maximize_window()
    driver.implicitly_wait(10)
    try:
        driver.find_element_by_xpath('''//*[@id="app"]/div/div[1]/div/div/div/div[2]/div/form/div[1]/div/div/input''').send_keys(ConfigRead.read_ini("GovernmentAccount","PD"))
        driver.find_element_by_xpath('''//*[@id="app"]/div/div[1]/div/div/div/div[2]/div/form/div[2]/div/div/input''').send_keys(ConfigRead.read_ini("GovernmentPwd","PD"))
        driver.find_element_by_xpath('''//*[@id="app"]/div/div[1]/div/div/div/div[2]/div/form/div[4]/div/button/span''').click()
        time.sleep(2)
    except NoSuchElementException as e:
        print(e)
    return driver
if __name__=="__main__":
    Loginmode()

