#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Jonny"
# Email: jonnysps@yeah.net
# Date: 2017/12/12

from selenium import  webdriver
from time import sleep as s
import time

from selenium.webdriver.common.action_chains import ActionChains

from Test_SePy_base1.ObjectPage.DecoratorScreen import Screen

driver = webdriver.Chrome()

def get_screen():
    nowtime = time.strftime("%Y_%m_%d_%H_%M_%S")
    driver.get_screenshot_as_file("%s.PNG" % nowtime)
    print(nowtime)

# def screen(func):
#
#     def inner(*args):
#         try:
#             f=func(*args)
#
#             return f
#         except:
#             get_screen()
#             #print("异常信息是：%s" % e)
#             raise
#
#     return inner


@Screen(driver)
def search(driver):

    driver.get("https://www.baidu.com/")
    driver.maximize_window()
    s(2)
    driver.find_element_by_id("kw").send_keys("python")
    s(2)
    driver.find_element_by_id("s2u").click()
    s(2)
    #get_screen()



# s=screen(search(driver))  #S变量 是 inner 函数地址，  S（） 等于调用内部inner函数
# s()
search(driver)


# driver.get("http://bbs.makex.cc/portal.php")
# driver.maximize_window()
#
# driver.find_element_by_xpath(".//*[@id='nv_portal']/div[3]/div[1]/div[3]/a[1]").click()
#
# s(3)
#
#
# s(3)
# #driver.find_element_by_xpath(".//*[@id='username_LDSbx']").click()
# driver.find_element_by_name("username").send_keys("3433201@qq.com")
# driver.find_element_by_name("password").click()
# driver.find_element_by_name("password").send_keys("jy123456")
#
# s(10)
# driver.find_element_by_name("loginsubmit").click()
#
#
# s(5)
#
# element=driver.find_element_by_link_text("新手上路")
# ActionChains(driver).move_to_element(element).perform()
# s(3)
#
#    #driver.find_element_by_xpath(".//*[@id='nv_home']/div[3]/div[1]/div[3]/div[1]/div/div[3]/a[2]").click()
# driver.find_element_by_class_name("graysmallbutton").click()