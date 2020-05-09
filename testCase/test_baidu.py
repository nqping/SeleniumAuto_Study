#!/usr/bin/sh python
# -*- coding: utf-8 -*-
# @Time : 2020/5/9 14:59 
# @Author : qingping.niu
# @File : test_baidu.py 
# @Desc :

import unittest
from selenium import webdriver

class BaiduTest(unittest.TestCase):
    def setUp(self) -> None:
        self.driver = webdriver.Firefox()
        self.driver.maximize_window()
        self.driver.get('http://www.baidu.com')
        self.driver.implicitly_wait(30)

    def tearDown(self) -> None:
        self.driver.quit()

    def test_baidu_title(self):
        '''验证:测试百度首页的title是否正确'''
        self.assertEqual(self.driver.title,'百度一下，你就知道')

if __name__ == '__main__':
    unittest.main(verbosity=2)