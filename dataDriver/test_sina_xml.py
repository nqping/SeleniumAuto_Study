#!/usr/bin/sh python
# -*- coding: utf-8 -*-
# @Time : 2020/5/12 9:40 
# @Author : qingping.niu
# @File : test_sina_xml.py 
# @Desc : 从XML中获取测试数据

import unittest
import xml.dom.minidom
import time
from selenium import webdriver

def getXmlData(value):
    '''
    获取xml单节点中的数据
    :param value: xml文件中单节点数据
    :return:
    '''
    dom = xml.dom.minidom.parse('sina.xml')
    db = dom.documentElement
    name = db.getElementsByTagName(value)
    nameValue = name[0]
    return nameValue.firstChild.data

def getXmlUser(parent,child):
    '''
    获取xml子节点中的数据
    :param parent: xml文件中的父节点的名称
    :param child: xml中子节点的名称
    :return:
    '''
    dom = xml.dom.minidom.parse('sina.xml')
    db = dom.documentElement
    itemlist = db.getElementsByTagName(parent)
    item = itemlist[0]
    return item.getAttribute(child)

class SinaTestByXML(unittest.TestCase):
    def setUp(self) -> None:
        self.driver = webdriver.Firefox()
        self.driver.maximize_window()
        self.driver.get(getXmlData('url'))
        self.driver.implicitly_wait(30)

    def tearDown(self) -> None:
        self.driver.quit()

    def login(self,username,password):
        self.driver.find_element_by_id('freename').send_keys(username)
        self.driver.find_element_by_id('freepassword').send_keys(password)
        time.sleep(5)
        self.driver.find_element_by_link_text(u'登录').click()

    @property
    def getLoginError(self):
        '''返回点击"登录"按钮后的错误提示信息'''
        loginError = self.driver.find_element_by_xpath(
            '/html/body/div[1]/div/div[2]/div/div/div[4]/div[1]/div[1]/div[1]/span[1]').text
        return loginError

    def test_sina_login_emailNull(self):
        '''新浪邮箱登录:登录账号邮箱为空验证'''
        self.login('','')
        self.assertEqual(self.getLoginError,getXmlUser('errorMsg','emailNull'))

    def test_sina_login_emialFormat(self):
        '''新浪邮箱登录:登录账号邮箱格式填写错误验证'''
        self.login('wuya103','adminse')
        self.assertEqual(self.getLoginError,getXmlUser('errorMsg','emailFormat'))

if __name__ == '__main__':
    unittest.main(verbosity=2)