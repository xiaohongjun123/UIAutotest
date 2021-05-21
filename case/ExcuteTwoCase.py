#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2021/04/28 14:41
# @Author  : hongjun.xiao
# @File    : ExcuteTwoCase.py
# @system  : WenJiang


import unittest
from util import Excel
import ddt
import time
from util import LoginCommon
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains

@ddt.ddt
class Login(unittest.TestCase):

    def isElementExist(self,element):
        try:
            self.driver.find_element_by_xpath(element)
        except NoSuchElementException as e:
            return False
        return True

    def setUp(self):
        self.driver=LoginCommon.Loginmode()
    def tearDown(self):
        self.driver.quit()

    @ddt.data(*Excel.ExecuteTwo())
    def test_login(self,value):
        '''{}'''#获取用例描述
        self.driver.implicitly_wait(10)
        for step in range(len(value)):
            try:

                if value[step]=="输入值":
                    if self.isElementExist(value[step+1])==False:
                        self.driver.refresh()
                    self.driver.find_element_by_xpath(value[step+1]).send_keys(value[step+2])
                    time.sleep(2)
                elif value[step]=="xpath操作":
                    if self.isElementExist(value[step+1])==False:
                        self.driver.refresh()
                    self.driver.find_element_by_xpath(value[step+1]).click()
                    time.sleep(2)
                elif value[step]=="鼠标悬停":
                    ActionChains(self.driver).move_to_element(self.driver.find_element_by_xpath(value[step+1])).perform()
                    time.sleep(1)
                    self.driver.find_element_by_xpath(value[step+2]).click()
                    time.sleep(2)
                elif value[step]=="预计结果":
                    self.assertIn(value[step+1],self.driver.page_source)
                else:
                    pass
            except NoSuchElementException as e:
                raise NoSuchElementException
            except AssertionError as e:
                raise AssertionError








if __name__=="__main__":
    unittest.main()