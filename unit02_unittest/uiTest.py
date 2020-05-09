#!/usr/bin/sh python
# -*- coding: utf-8 -*-
# @Time : 2020/5/8 16:33 
# @Author : qingping.niu
# @File : uiTest.py 
# @Desc : 测试固件只执行一次(只初始化一次)

import unittest
from selenium import webdriver

class UiTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.driver = webdriver.Firefox()
        cls.driver.maximize_window()
        cls.driver.get('http://www.baidu.com')
        cls.driver.implicitly_wait(30)
        print('--------start----------')

    @classmethod
    def tearDownClass(cls) -> None:
        cls.driver.quit()
        print('----------end------------')

    def test_baidu_news(self):
        '''验证:测试百度首页点击新闻后的跳转'''
        self.driver.find_element_by_link_text('新闻').click()
        self.driver.get('http://www.baidu.com')

    def test_baidu_map(self):
        '''验证:测试百度首页点击地图后的跳转'''
        self.driver.find_element_by_link_text('地图').click()
        self.driver.get('http://www.baidu.com')

if __name__=='__main__':
    unittest.main(verbosity=2)