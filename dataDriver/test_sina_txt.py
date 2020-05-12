#!/usr/bin/sh python
# -*- coding: utf-8 -*-
# @Time : 2020/5/11 13:34 
# @Author : qingping.niu
# @File : test_sina_txt.py 
# @Desc : 从txt中获取测试数据 (不可用)

import os,unittest,time
from selenium import webdriver

def getTxtData(index):
    '''根据index从txt中获取对应数据'''
    with open(os.path.join(os.path.dirname(__file__),'sina.txt'),'r',encoding='utf-8') as f:
        d = f.readlines()
    return d[index]

class SinaLoginByTxt(unittest.TestCase):
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
        self.login(getTxtData(0),getTxtData(0))
        print(getTxtData(2))
        print('----'+self.divText())
        self.assertTrue(self.divText(),getTxtData(2))

    def test_sina_password_null(self):
        '''验证:测试用户名为空密码不为空的错误提示信息'''
        self.login(getTxtData(0),getTxtData(1))
        print(getTxtData(0))
        print(getTxtData(1))
        print(self.divText())
        print(getTxtData(2))
        self.assertTrue(self.divText(),getTxtData(2))
    #
    # def test_sina_username_format(self):
    #     '''验证:测试用户名邮箱格式不正确的错误提示信息'''
    #     self.login(getTxtData(0),getTxtData(1))
    #     self.assertTrue(self.divText(),getTxtData(3))

if __name__ == '__main__':
    unittest.main(verbosity=2)




