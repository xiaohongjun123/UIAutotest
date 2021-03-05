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


opt = webdriver.ChromeOptions()
opt.add_argument(r"user-data-dir=C:\Users\Administrator\AppData\Local\Google\Chrome\User Data")
opt.add_experimental_option('excludeSwitches', ['enable-automation'])
driver=webdriver.Chrome(options=opt)
driver.maximize_window()
driver.get("http://user_pc.frontend.qa-wenjiang.heroera.com/")
time.sleep(3)
'''
cookie={'domain': '.user_pc.frontend.qa-wenjiang.heroera.com/',
        "name":"Cookie",
       "value":"bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJkYXRhIjp7InVzZXJfaWQiOjUwNzksInR5cGUiOjEsInNpZ24iOiJOcFo5QngxdWRIIn19.Gy3VeJMiUip7q0q25vTS1gGYnHtw3gs9pHZTk90sTIJEoAygD6rpV3X32JyoX7tWtQ6Tbyjy3Qxj8Nkhcw6cYNmqDmOzaM7SHo3cMb-IxGjDiR7LowjLPUyFq1wN1kHWCm2V4P7AGYiI0bK-cR05iNYEso01p0D6CM0pALrAT4PeeluUdT7C9xYeV6QTIxowBH8n4F9D3vjtW3d4bMeEqbYThBL2x5AzlHHI8kbwwFATX7l8Tfjm5GYynPNUeriYGiw9qvfPQnZ-PC8kvIkJ0BLYmfuWqjxX2cbju_6w7idNgEzZv78NtsAClnZRnyVl415kp-RfIPWdY1XZ2t7pdw",
        'httpOnly': False,
        "expires": '',
        'path': '/',
        'HostOnly': False,
        'Secure': False
        }
driver.add_cookie(cookie)
'''
driver.find_element_by_xpath('''//*[@id="header-wapper"]/div[3]/ul/li[13]/div''').click()
time.sleep(2)
driver.find_element_by_xpath('''//*[@id="main"]/div[1]/div[2]/div/div[1]/div/ul/li[4]''').click()

driver.quit()


