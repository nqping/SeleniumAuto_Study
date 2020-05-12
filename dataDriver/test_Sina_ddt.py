#!/usr/bin/sh python
# -*- coding: utf-8 -*-
# @Time : 2020/5/11 11:07 
# @Author : qingping.niu
# @File : test_Sina_ddt.py
# @Desc : 数据驱动

import unittest
from selenium import webdriver
from ddt import data,unpack,ddt
import os

def getData():
    '''数据分离出来放到列表中'''
    return [
        ['','','请输入邮箱名'],
        ['','admin','请输入邮箱名'],
        ['admin','','您输入的邮箱名格式不正确']
    ]

@ddt
class SinaLoginByDDT(unittest.TestCase):
    def setUp(self) -> None:
        self.driver = webdriver.Firefox()
        self.driver.maximize_window()
        self.driver.get('http://mail.sina.com.cn/')
        self.driver.implicitly_wait(30)

    def tearDown(self) -> None:
        self.driver.quit()

    #@data(('','','请输入邮箱名'),('','admin','请输入邮箱名'),('admin','','您输入的邮箱名格式不正确'))
    @data(*getData())
    @unpack
    def test_login(self,username,password,result):
        '''验证:测试新浪邮箱登录N种情况'''
        self.driver.find_element_by_id('freename').send_keys(username)
        self.driver.find_element_by_id('freepassword').send_keys(password)
        self.driver.find_element_by_link_text('登录').click()
        divText = self.driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div/div/div[4]/div[1]/div[1]/div[1]/span[1]').text
        self.assertEqual(divText,result)

    if __name__ == '__main__':
        unittest.main(verbosity=2)
