#!/usr/bin/sh python
# -*- coding: utf-8 -*-
# @Time : 2020/5/12 15:56 
# @Author : qingping.niu
# @File : test_weibo.py 
# @Desc :  使用appium测试

import unittest
import time as t
from appium import webdriver
from page.weibo import WeiBo

class WeiBoTest(unittest.TestCase,WeiBo):
    def setUp(self) -> None:
        desired_caps = {}
        desired_caps['platformName'] = 'Android'  # 系统名称
        desired_caps['platformVersion'] = '4.4.2'  # 系统的版本号
        desired_caps['deviceName'] = 'Android Emulator'  # 设备名称，这里是虚拟机，这个没有严格的规定
        desired_caps['appPackage'] = 'com.lemon.lemonban'  # APP包名
        desired_caps['appActivity'] = 'com.lemon.lemonban.activity.WelcomeActivity'  # APP入口的activity
        # 连接appium server，告诉appium，代码要操作哪个设备上的哪个APP
        driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)

    def test_001(self):
        t.sleep(3)
        self.getPhoneCode('13254759693')

    def tearDown(self) -> None:
        self.driver.quit()

if __name__ == '__main__':
    unittest.main(verbosity=2)