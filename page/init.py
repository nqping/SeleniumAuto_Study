#!/usr/bin/sh python
# -*- coding: utf-8 -*-
# @Time : 2020/5/12 15:02 
# @Author : qingping.niu
# @File : init.py 
# @Desc : 分离测试固件

import unittest
from selenium import webdriver
from utils.operationXml import *

class Init(unittest.TestCase,OperationXml):
    def setUp(self) -> None:
        self.driver = webdriver.Firefox()
        self.driver.maximize_window()
        self.driver.get(self.getXmlData('url'))
        self.driver.implicitly_wait(30)

    def tearDown(self) -> None:
        self.driver.quit()