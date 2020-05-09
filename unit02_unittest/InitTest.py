#!/usr/bin/sh python
# -*- coding: utf-8 -*-
# @Time : 2020/5/9 14:44 
# @Author : qingping.niu
# @File : InitTest.py 
# @Desc : 分离测试固件

import unittest
from selenium import webdriver

class InitTest(unittest.TestCase):
    def setUp(self) -> None:
        self.driver = webdriver.Firefox()
        self.driver.maximize_window()
        self.driver.get('http://www.baidu.com')
        self.driver.implicitly_wait(30)

    def tearDown(self) -> None:
        self.driver.quit()