#!/usr/bin/sh python
# -*- coding: utf-8 -*-
# @Time : 2020/5/9 15:00 
# @Author : qingping.niu
# @File : allTests.py 
# @Desc : 批量执行测试用例

from framework import HTMLTestReportCN
import unittest
import os
import time
import HTMLTestReportCN


def allClass():
    '''获取所有测试模块'''
    suite = unittest.TestLoader().discover(
        start_dir=os.path.join(os.path.dirname(__file__),'testCase'),
        pattern='test_*.py',top_level_dir=None) #获取模块
    return suite

def allTests():
    # 获取所有测试用例
    suite = unittest.defaultTestLoader.discover(
        start_dir=os.path.join(os.path.dirname(__file__),'testCase'),
        pattern='test_*.py', top_level_dir=None)
    return suite

def getNowTime():
    '''获取当前时间'''
    return time.strftime('%Y-%m-%d %H-%M_', time.localtime(time.time()))

def run():
    fileName = os.path.join(os.path.join(os.path.dirname(__file__),'report'),getNowTime()+'report.html')
    fp = open(fileName,'wb')
    runner = HTMLTestReportCN.HTMLTestRunner(stream=fp,title='UI自动化测试报告',description='用例执行情况')
    runner.run(allTests())




if __name__ == '__main__':
    # unittest.TextTestRunner(verbosity=2).run(allClass())
    run()