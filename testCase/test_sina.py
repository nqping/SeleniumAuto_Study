#!/usr/bin/sh python
# -*- coding: utf-8 -*-
# @Time : 2020/5/9 14:59 
# @Author : qingping.niu
# @File : test_sina.py
# @Desc :

import unittest
from selenium import webdriver

class SinaTest(unittest.TestCase):
    def setUp(self) -> None:
        self.driver = webdriver.Firefox()
        self.driver.maximize_window()
        self.driver.get('http://mail.sina.com.cn/')
        self.driver.implicitly_wait(30)

    def tearDown(self) -> None:
        self.driver.quit()

    def test_username_password_null(self):
        '''验证:新浪登录页面用户名和密码为空错误提示信息'''
        self.driver.find_element_by_id('freename').send_keys('')
        self.driver.find_element_by_id('freepassword').send_keys('')
        self.driver.find_element_by_link_text('登录').click()
        divError = self.driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div/div/div[4]/div[1]/div[1]/div[1]/span[1]').text
        self.assertEqual(divError,'请输入邮箱名')


    if __name__ == '__main__':
        unittest.main(verbosity=2)

