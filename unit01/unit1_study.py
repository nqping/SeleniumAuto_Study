#!/usr/bin/sh python
# -*- coding: utf-8 -*-
# @Time : 2020/5/6 15:22 
# @Author : qingping.niu
# @File : unit1_study.py 
# @Desc : 基础定位和页面交互

from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
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
    '''页面交互(前进或后退)'''
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
    '''多窗口交互(窗口句柄)'''
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

def demo_alert():
    '''弹出框处理(switch_to_alert()使用)'''
    #提示框处理
    driver = webdriver.Firefox()
    driver.maximize_window()
    driver.implicitly_wait(30)
    driver.get('http://www.baidu.com')
    #实现鼠标悬浮到百度首页的设置
    element = driver.find_element_by_css_selector('a.pf:nth-child(9)')
    t.sleep(3)
    ActionChains(driver).move_to_element(element).perform()
    t.sleep(3)
    #点击设置中的搜索设置按钮
    driver.find_element_by_css_selector('.setpref').click()
    t.sleep(2)
    #点击保存设置按钮
    driver.find_element_by_css_selector('#gxszButton > a.prefpanelgo').click()
    t.sleep(2)
    #获取弹出框的文件信息
    print('alert弹出框的文本信息为:{}'.format(driver.switch_to_alert().text))
    #点击alert 弹出框中的确定按钮
    driver.switch_to_alert().accept()
    t.sleep(5)
    driver.quit()


def demo_WebDriverWait():
    '''等待方式
    1.固定等待: 如调用 time中的sleep方式
    2.隐式等待: 如implicitly_wait 指设置最长等待时间
    3.显示等待: 程序每隔一段时间执行自定义的程序判断条件,如果条件判断成功,程序继续执行;条件判断失败,程序抛出TimeOutException
    element_to_be_clickable() :判断元素可见后返回WebElement类的实例对象,这样就可执行输入,点击操作.
    text_to_be_present_in_element() :指定元素的文本位置,一般用于验证一个文本信息或者错误提示信息;文本匹配返回True
    visibility_of_element_located : 等元素可见过执行操作
    '''
    #元素可见并且可操作element_to_be_clickable()
    # driver = webdriver.Firefox()
    # driver.maximize_window()
    # driver.get('http://www.baidu.com')
    # driver.implicitly_wait(30)
    # so = WebDriverWait(driver,10).until(expected_conditions.element_to_be_clickable((By.ID,'kwss')))
    # so.send_keys('Selenium')
    # t.sleep(5)

    #指定元素的文本位置
    driver = webdriver.Firefox()
    driver.maximize_window()
    driver.implicitly_wait(30)
    driver.get('https://mail.sina.com.cn/#')
    #输入新浪邮箱用户名和密码
    driver.find_element_by_id('freename').send_keys('')
    driver.find_element_by_id('freepassword').send_keys('')
    #点击登录按钮
    driver.find_element_by_link_text('登录').click()
    isText = WebDriverWait(driver,10).until(expected_conditions.text_to_be_present_in_element((By.XPATH,'/html/body/div[1]/div/div[2]/div/div/div[4]/div[1]/div[1]/div[1]/span[1]'),'请输入邮箱名'))
    print('打印结果是:{0}'.format(isText))
    t.sleep(5)
    
    #判断元素是否可见
    # driver = webdriver.Firefox()
    # driver.maximize_window()
    # driver.implicitly_wait(30)
    # driver.get('http://www.baidu.com')
    # aboutBaidu = WebDriverWait(driver,10).until(expected_conditions.visibility_of_element_located((By.LINK_TEXT,'关于百度')))
    # aboutBaidu.click()
    # t.sleep(5)

    driver.quit()

def demo_ActionChains():
    '''鼠标操作'''
    #鼠标双击
    # driver = webdriver.Firefox()
    # driver.maximize_window()
    # driver.implicitly_wait(30)
    # driver.get('http://www.baidu.com')
    # # 对ActionChains进行实例化
    # actionChains = ActionChains(driver)
    # driver.find_element_by_id('kw').send_keys('Selenium')
    # locator = driver.find_element_by_id('su')
    # #对"百度一下"按钮双击操作
    # actionChains.double_click(locator).perform()
    # t.sleep(5)

    #鼠标右键
    # driver = webdriver.Firefox()
    # driver.maximize_window()
    # driver.implicitly_wait(30)
    # driver.get('http://www.baidu.com')
    # #对ActionChains进行实例化
    # actionChains = ActionChains(driver)
    # so = driver.find_element_by_id('kw')
    # actionChains.context_click(so).perform()
    # t.sleep(5)

    #键盘事件
    driver = webdriver.Firefox()
    driver.maximize_window()
    driver.implicitly_wait(30)
    driver.get('http://www.baidu.com')
    so = driver.find_element_by_id('kw')
    so.send_keys('Selenium')
    so.send_keys(Keys.CONTROL,'a')#选中输入框的搜索关键字
    so.send_keys(Keys.CONTROL,'c')#复制搜索的关键字
    so.send_keys(Keys.BACKSPACE) #按下Backspace删除输入的关键字
    #打开bing 搜索的首页
    driver.get('http://www.bing.com')
    bingSo = driver.find_element_by_id('sb_form_q')
    bingSo.send_keys(Keys.CONTROL,'v')
    t.sleep(5)

    driver.quit()

def demo_JavaScript():
    '''脚本,富文件处理'''

    #富文件处理
    driver = webdriver.Firefox()
    driver.implicitly_wait(30)
    driver.get('http://ueditor.baidu.com/website/onlinedemo.html')
    js = "document.getElementById('ueditor_0').contentWindow.document.body.innerHTML='自动化测试实战'"
    driver.execute_script(js)
    t.sleep(3)

    #js脚本处理
    # driver = webdriver.Firefox()
    # driver.implicitly_wait(30)
    # driver.get('http://www.baidu.com')
    # driver.find_element_by_id('kw').send_keys('Selenium')
    # driver.find_element_by_id('su').click()
    # #浏览器滑动到底部js代码
    # down = "var q=document.documentElement.scrollTop=1000"
    # t.sleep(3)
    # #操作js实现鼠标滑动到浏览器底部
    # driver.execute_script(down)
    # t.sleep(3)
    # #点击下一页
    # driver.find_element_by_link_text('下一页>').click()
    # t.sleep(3)
    # #浏览器滑动到顶部
    # up = "var q=document.documentElement.scrollTop=0"
    # #先滑动到底部
    # driver.execute_script(down)
    # t.sleep(3)
    # driver.execute_script(up)
    # t.sleep(4)
    driver.quit()

def demo_screenshot():
    '''截图处理'''
    driver = webdriver.Firefox()
    driver.maximize_window()
    driver.implicitly_wait(30)
    driver.get('http://www.baidu.com')
    driver.save_screenshot('baidu.png')  #获取当前截取图
    # driver.get_screenshot_as_file('G:\\gitworkspace\\SeleniumAuto_Study\\baidu2.png') #当前截取图保存到指定路径
    # print(driver.get_screenshot_as_png()) #获取图片二进制数据
    driver.quit()



if __name__ == "__main__":
    # demo_find_element()
    # demo_page_interaction()
    # demo_windows()
    # demo_WebElement()
    # demo_select()
    # demo_alert()
    # demo_WebDriverWait()
    # demo_ActionChains()
    # demo_JavaScript()
    demo_screenshot()