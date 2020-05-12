#!/usr/bin/sh python
# -*- coding: utf-8 -*-
# @Time : 2020/5/11 16:24 
# @Author : qingping.niu
# @File : test_sina_excel.py 
# @Desc : 从excel中获取测试数据

import unittest
import xlrd
import time
from selenium import webdriver

def readExcel(row):
    '''
    :param row: 该参数表示行
    :return:
    '''
    book = xlrd.open_workbook('sina.xlsx','r')
    table = book.sheet_by_index(0)
    return table.row_values(row)


class SinaTestByExcel(unittest.TestCase):
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

    def getLoginError(self):
        '''返回点击"登录"按钮后的错误提示信息'''
        loginError = self.driver.find_element_by_xpath(
            '/html/body/div[1]/div/div[2]/div/div/div[4]/div[1]/div[1]/div[1]/span[1]').text
        return loginError

    def test_sina_login_null(self):
        '''登录业务:用户名和密码为空的错误提示信息'''
        self.login(readExcel(1)[0],readExcel(1)[1])
        self.assertEqual(self.getLoginError(),readExcel(1)[2])


if __name__ == '__main__':
    unittest.main(verbosity=2)


