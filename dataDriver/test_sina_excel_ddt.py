#!/usr/bin/sh python
# -*- coding: utf-8 -*-
# @Time : 2020/5/11 16:50 
# @Author : qingping.niu
# @File : test_sina_excel_ddt.py 
# @Desc : ddt与excel结合使用

import xlrd
import unittest
import time
from ddt import ddt ,data,unpack
from selenium import webdriver

def readExcel(row):
    '''
    :param row: 该参数表示行
    :return:
    '''
    book = xlrd.open_workbook('sina.xlsx','r')
    table = book.sheet_by_index(0)
    return table.row_values(row)

def readExcels():
    '''读取excel数据添加到rows列表中'''
    rows = []
    book = xlrd.open_workbook('sina.xlsx', 'r')
    sheet = book.sheet_by_index(0)
    for row in range(1,sheet.nrows):
        rows.append(sheet.row_values(row,0,sheet.ncols))
    return rows

@ddt
class SinaTestByExcelAndDDT(unittest.TestCase):
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

    @data(*readExcels())
    @unpack
    def test_sina_login(self,username,password,result):
        '''登录业务测试'''
        self.login(username,password)
        self.assertEqual(self.getLoginError(),result)


if __name__ == '__main__':
    unittest.main(verbosity=2)