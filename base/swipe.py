#!/usr/bin/sh python
# -*- coding: utf-8 -*-
# @Time : 2020/5/12 16:17 
# @Author : qingping.niu
# @File : swipe.py 
# @Desc : swipe二次封装

from appium import webdriver
import time as t

class Swipe(object):
    def __init__(self,driver):
        self.driver = driver

    @property
    def width(self):
        return self.driver.get_window_size()['width']

    @property
    def height(self):
        return self.driver.get_window_size()['height']

    @property
    def getResolution(self):
        return str(self.width)+"*"+str(self.height)

    @property
    def set_Left_Right(self):
        '''
        :return: 实现从左至右滑动,滑动时X轴起点大于终点
        '''
        t.sleep(3)
        self.driver.swipe(self.width*9/10,self.height/2,self.width/20,self.height/2,0)

    @property
    def set_Right_Left(self):
        '''
        实现从右到左滑动,滑动时X轴起点小于终点
        :return:
        '''
        t.sleep(2)
        self.driver.swipe(self.width/10,self.height/2,self.width*9/10,self.height/2,0)

    @property
    def set_Up_Down(self):
        '''
        实现从上往下滑动,滑动时Y轴起点大于终点
        :return:
        '''
        t.sleep(2)
        self.driver.swipe(self.width/2,self.height*9/10,self.width/2,self.height/20,0)

    @property
    def set_Down_Up(self):
        '''
        实现从下往上滑动,滑动时Y轴起点小于终点
        :return:
        '''
        t.sleep(2)
        self.driver.swipe(self.width/2,self.height/20,self.width/2,self.height*9/10,0)