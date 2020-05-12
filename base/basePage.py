#!/usr/bin/sh python
# -*- coding: utf-8 -*-
# @Time : 2020/5/12 13:23 
# @Author : qingping.niu
# @File : basePage.py 
# @Desc : 页面基类

from selenium import webdriver
from selenium.webdriver.support.expected_conditions import NoSuchElementException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from appium.webdriver.common.mobileby import MobileBy
import time as t

class Factory(object):
    def __init__(self,driver):
        self.driver = driver

    # 工厂方法
    def createDriver(self, driver):
        if driver == 'web':
            return WebUI(self.driver)
        elif driver == 'app':
            return AppUI(self.driver)


class WebDriver(object):
    def __init__(self,driver):
        self.driver = driver

    def findElement(self,*loc):
        '''单个定位元素方法
        加入显示式等待20s
        '''
        try:
            return WebDriverWait(self.driver,20).until(lambda x:x.find_element(*loc))
        except NoSuchElementException as e:
            print('Error Details {}'.format(e.args[0]))

    def findsElement(self,*loc):
        '''多个定位元素方法'''
        try:
            return WebDriverWait(self.driver,20).until(lambda x:x.find_element(*loc))
        except NoSuchElementException as e:
            print('Error Details {}'.format(e.args[0]))

class WebUI(WebDriver):
    def __str__(self):
        return 'WebUI'

class AppUI(WebDriver):
    def __str__(self):
        return 'AppUI'