#!/usr/bin/sh python
# -*- coding: utf-8 -*-
# @Time : 2020/5/8 16:06 
# @Author : qingping.niu
# @File : test_case_badu.py
# @Desc : 单元测试使用与测试报告
import unittest
from selenium import webdriver

class BaiduTest(unittest.TestCase):

    def setUp(self) -> None:
        '''
        测试之前的准备工作
        :return:
        '''
        self.driver = webdriver.Firefox()
        self.driver.maximize_window()
        self.driver.get('http://www.baidu.com')
        self.driver.implicitly_wait(30)

    def tearDown(self) -> None:
        '''
        测试之后的收尾
        如关闭数据库
        :return:
        '''
        self.driver.quit()

    def test_baidu_news(self):
        '''验证:测试百度首页点击新闻后的跳转'''
        self.driver.find_element_by_link_text('新闻').click()
        url = self.driver.current_url
        self.assertEqual(url,'https://www.baidu.com/')



class BaiduMap(unittest.TestCase):
    def setUp(self) -> None:
        self.driver = webdriver.Firefox()
        self.driver.maximize_window()
        self.driver.get('http://www.baidu.com')
        self.driver.implicitly_wait(30)

    def tearDown(self) -> None:
        self.driver.quit()

    def test_baidu_map(self):
        '''验证:测试百度首页点击地图后的跳转'''
        self.driver.find_element_by_link_text('地图').click()
        self.driver.get('http://www.baidu.com')

if __name__=='__main__':
    # unittest.main(verbosity=2)
    #测试套件(按顺序执行)
    # suite = unittest.TestSuite()
    # suite.addTest(BaiduTest('test_baidu_news'))
    # suite.addTest(BaiduTest('test_baidu_map'))
    # unittest.TextTestRunner(verbosity=2).run(suite)

    #测试套件(按类执行)
    # suite = unittest.TestSuite(unittest.makeSuite(BaiduTest))
    # unittest.TextTestRunner(verbosity=2).run(suite)

    #测试套件(按类执行
    # suite = unittest.TestLoader().loadTestsFromTestCase(BaiduTest)
    # unittest.TextTestRunner(verbosity=2).run(suite)

    #测试套件(按模块执行, 一个python文件就是一个模块)
    suite = unittest.TestLoader().loadTestsFromModule('unittest1.py')
    unittest.TextTestRunner(verbosity=2).run(suite)


