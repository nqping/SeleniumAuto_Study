#!/usr/bin/sh python
# -*- coding: utf-8 -*-
# @Time : 2020/5/12 15:46 
# @Author : qingping.niu
# @File : weibo.py 
# @Desc : 手机版

from selenium import webdriver
from selenium.webdriver.common.by import By
from base.basePage import *
from time import sleep
from appium import webdriver

class WeiBo(AppUI):
    login_loc = (By.XPATH,"//android.widget.TextView[@text='登录']")
    phone_loc = (By.XPATH,"//android.widget.EditText[@text='输入手机号']")
    codeButton_loc = (By.XPATH,"//android.widget.Button[@text='获取验证码']")

    @property
    def clickMy(self):
        sleep(3)
        self.findElement(*self.login_loc).click()

    def typePhone(self,phone):
        self.findElement(*self.phone_loc).send_keys(phone)

    def clickCodeButton(self):
        self.findElement(*self.codeButton_loc).click()

    def getPhoneCode(self,phone):
        self.clickMy
        self.typePhone(phone)
        self.clickCodeButton()
