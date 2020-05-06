#!/usr/bin/sh python
# -*- coding: utf-8 -*-
# @Time : 2020/5/6 15:22 
# @Author : qingping.niu
# @File : unit1_study.py 
# @Desc : 基础定位和页面交互

from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.action_chains import ActionChains
import time as t

def demo_find_element():
    '''单元素定位方式'''
    driver = webdriver.Firefox()
    driver.maximize_window()  # 窗口最大化
    driver.implicitly_wait(30) #隐式等待
    driver.get("http://www.baidu.com")
    # driver.find_element_by_id("kw").send_keys("selenium")
    # driver.find_element_by_class_name("s_ipt").send_keys("selenium")
    # driver.find_element_by_name("wd").send_keys("selenium")
    # driver.find_element_by_xpath('//*[@id="kw"]').send_keys("selenium")
    # driver.find_element_by_css_selector('#kw').send_keys('selenium')
    # driver.find_element_by_link_text(u'新闻').click()
    # driver.find_element_by_partial_link_text(u'闻').click()  #模糊搜索方式
    #多元素定位方式
    # tag_names = driver.find_elements_by_tag_name('input')
    # for tag_name in tag_names:
    #     print(tag_name)
    # print(type(tag_names))
    # driver.find_elements_by_tag_name('input')[7].send_keys('selenium')

    driver.quit()

def demo_page_interaction():
    '''页面交互'''
    driver = webdriver.Firefox()
    driver.maximize_window()
    driver.get('http://www.baidu.com')
    driver.implicitly_wait(30)
    print('页面标题:{}'.format(driver.title))
    print('执行浏览器为:{}'.format(driver.name))
    #print('页面代码:{}'.format(driver.page_source))
    #页面前进和后退
    t.sleep(2)
    driver.get('http://www.bing.com')
    t.sleep(2)
    #返回百度
    driver.back()
    print('当前URL为:{}'.format(driver.current_url))
    t.sleep(2)
    #前进到bing
    driver.forward()
    print('当前URL为:{}'.format(driver.current_url))
    driver.quit()

def demo_windows():
    '''多窗口交互'''
    driver = webdriver.Firefox()
    driver.maximize_window()
    driver.get('http://mail.sina.com.cn/')
    driver.implicitly_wait(30)
    #获取当前窗口句抦
    now_handle = driver.current_window_handle
    t.sleep(2)
    #点击注册链接
    driver.find_element_by_link_text(u'注册').click()
    t.sleep(2)
    #获取所有窗口句抦
    handles = driver.window_handles
    #对所有窗口句柄循环处理
    for handle in handles:
        #判断handle不是当前窗口句柄
        if handle != now_handle:
            driver.switch_to_window(handle)
            t.sleep(2)
            driver.find_element_by_name('email').send_keys('nqp')
            t.sleep(2)
            #关闭注册页
            driver.close()
    #切换到登录页
    driver.switch_to_window(now_handle)
    t.sleep(3)
    #在账号输入框中输入邮箱
    driver.find_element_by_id('freename').send_keys('nqp')
    t.sleep(4)
    driver.quit()

def demo_WebElement():
    '''刷新,清空,WebElement相关操作'''
    driver = webdriver.Firefox()
    driver.maximize_window()
    # driver.get('http://www.baidu.com')
    # t.sleep(3)
    # #刷新
    # driver.refresh()
    # so = driver.find_element_by_id('kw')
    # so.send_keys('selenium')
    # t.sleep(2)
    # #清空搜索关键字
    # so.clear()
    # t.sleep(3)

    #获取placeholder 提示信息
    # driver.get('http://mail.sina.com.cn/')
    # name = driver.find_element_by_id('freename')
    # print('用户输入框中提示信息为:{}'.format(name.get_attribute('placeholder')))
    # t.sleep(5)

    #获取输入值(value)
    # driver.get('http://www.baidu.com')
    # so = driver.find_element_by_id('kw')
    # so.send_keys('Selenium WebDriver')
    # print('百度输入框中数据为:{}'.format(so.get_attribute('value')))
    # t.sleep(3)

    #检查元素是否可见
    # driver.get('http://www.baidu.com')
    # about = driver.find_element_by_link_text('关于百度')
    # print('关于百度是否可见:{}'.format(about.is_displayed()))
    # t.sleep(3)

    #检查元素是否可编辑
    # driver.get('http://www.baidu.com')
    # so = driver.find_element_by_id('kw')
    # print('搜索输入框是否可编辑:{}'.format(so.is_enabled()))
    # t.sleep(3)

    #检查是否已选中
    driver.get('http://mail.sina.com.cn/')
    autoLogin = driver.find_element_by_id('store1')
    print('新浪登录页面自动登录是否已默认选中:{}'.format(autoLogin.is_selected()))
    t.sleep(2)
    driver.quit()

def demo_select():
    '''下拉框处理'''
    driver = webdriver.Firefox()
    driver.maximize_window()
    driver.implicitly_wait(30)
    driver.get('http://www.baidu.com')
    #实现鼠标悬浮到百度首页的设置
    element = driver.find_element_by_css_selector('a.pf:nth-child(9)')
    t.sleep(3)
    ActionChains(driver).move_to_element(element).perform()
    t.sleep(3)
    #点击设置中的搜索按钮
    driver.find_element_by_css_selector('.setpref').click()
    t.sleep(2)
    #定位到下拉框的元素属性
    nr = driver.find_element_by_name('NR')
    #实例化Select类
    select = Select(nr)
    #select.select_by_index(2) #索引方式定位
    # select.select_by_value('20') #value方式定位
    select.select_by_visible_text('每页显示50条')  #文件方式定位

    print('下拉框选择的最新条数是:{0}'.format(nr.get_attribute('value')))
    t.sleep(3)


    driver.quit()





if __name__ == "__main__":
    # demo_find_element()
    # demo_page_interaction()
    # demo_windows()
    # demo_WebElement()
    demo_select()
