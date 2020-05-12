#!/usr/bin/sh python
# -*- coding: utf-8 -*-
# @Time : 2020/5/11 14:38 
# @Author : qingping.niu
# @File : test_sina_csv.py 
# @Desc : 从csv中读取测试数据

import os,unittest,time,csv
from selenium import webdriver
import codecs
import pandas

def readCsv(row,col):
    rows = []
    with open('test.csv')as f:
        reader = csv.reader(f)
        next(reader,None) #下一行
        for iter in reader:
            rows.append(iter)
    return ''.join(rows[row][col])

class SinaLoginByCsv(unittest.TestCase):
    def setUp(self) -> None:
        self.driver = webdriver.Firefox()
        self.driver.maximize_window()
        self.driver.get('http://mail.sina.com.cn/')
        self.driver.implicitly_wait(30)

    def tearDown(self) -> None:
        self.driver.quit()

    def login(self,username,password):
        self.driver.find_element_by_id('freename').send_keys(username)
        self.driver.find_element_by_id('freepassword').send_keys(password)
        time.sleep(5)
        self.driver.find_element_by_link_text(u'登录').click()

    def divText(self):
        divText = self.driver.find_element_by_xpath(
            '/html/body/div[1]/div/div[2]/div/div/div[4]/div[1]/div[1]/div[1]/span[1]').text
        return divText

    def test_username_password_null(self):
        '''验证:测试用户名和密码都为空的错误提示信息'''
        self.login(readCsv(0,0),readCsv(0,1))
        self.assertEqual(self.divText(),readCsv(0,2))

    def test_sina_password_null(self):
        '''验证:测试用户名为空密码不为空的错误提示信息'''
        self.login(readCsv(1,0),readCsv(1,1))
        self.assertEqual(self.divText(),readCsv(1,2))

    def test_sina_username_format(self):
        '''验证:测试用户名邮箱格式不正确的错误提示信息'''
        self.login(readCsv(2,0),readCsv(2,1))
        self.assertEqual(self.divText(),readCsv(2,2))

if __name__ == '__main__':
    unittest.main(verbosity=2)