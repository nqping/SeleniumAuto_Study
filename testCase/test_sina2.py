#!/usr/bin/sh python
# -*- coding: utf-8 -*-
# @Time : 2020/5/12 14:33 
# @Author : qingping.niu
# @File : test_sina2.py 
# @Desc : po模式用

import unittest
from selenium import webdriver
from page.sina import *
from page.init import *
import time as t
from utils.operationXml import *

class SinaTest(Init,Sina):
    # def setUp(self) -> None:
    #     self.driver = webdriver.Firefox()
    #     self.driver.maximize_window()
    #     self.driver.get(self.getXmlData('url'))
    #     self.driver.implicitly_wait(30)
    #
    # def tearDown(self) -> None:
    #     self.driver.quit()

    def test_singLogin_001(self,parent='divText',value='emailNull'):
        '''登录业务:账号密码为空验证'''
        self.login('','')
        self.assertEqual(self.getLoginError,self.getXmlUser(parent,value))

    def test_sinaLogin_002(self,parent='divText',value='emailFormat'):
        '''登录业务:输入不规范邮箱'''
        self.login('dddfsd', '78757')
        self.assertEqual(self.getLoginError, self.getXmlUser(parent,value))


if __name__ == '__main__':
    unittest.main(verbosity=2)