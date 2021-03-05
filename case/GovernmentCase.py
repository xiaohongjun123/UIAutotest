#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2020/10/19 14:41
# @Author  : hongjun.xiao
# @File    : GovernmentCase.py
# @system  : WenJiang


import unittest
from util import Excel
import ddt
import time
from util import LoginCommon
from util import LogRecord
from selenium.common.exceptions import NoSuchElementException

log=LogRecord.LogRd("GovernmentCaseLog").getLog()
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
        log.info("账号登录成功")
    def tearDown(self):
        self.driver.quit()

    @ddt.data(*Excel.ReadExcel())
    def test_login(self,value):
        '''{}'''#获取用例描述
        self.driver.implicitly_wait(10)
        for step in range(len(value)):
            try:

                if value[step]=="输入值":
                    log.info("元素:%s执行输入操作,输入值为:%s"%(value[step+1],value[step+2]))
                    if self.isElementExist(value[step+1])==False:
                        self.driver.refresh()
                    self.driver.find_element_by_xpath(value[step+1]).send_keys(value[step+2])
                    time.sleep(2)
                elif value[step]=="xpath操作":
                    log.info("元素:%s执行点击" % (value[step + 1]))
                    if self.isElementExist(value[step+1])==False:
                        self.driver.refresh()
                    self.driver.find_element_by_xpath(value[step+1]).click()
                    time.sleep(2)
                elif value[step]=="预计结果":
                    log.info("预期结果为%s"%(value[step+1]))
                    self.assertIn(value[step+1],self.driver.page_source)
                else:
                    pass
            except NoSuchElementException as e:
                log.error("一级模块:%s 二级模块:%s 用例名称:%s 错误信息:%s"%(value[1],value[2],value[3],str(e)))
                raise NoSuchElementException
            except AssertionError as e:
                log.error("一级模块:%s 二级模块:%s 用例名称:%s 错误信息:预期结果与实际结果不匹配"%(value[1],value[2],value[3]))
                raise e






if __name__=="__main__":
    unittest.main()
