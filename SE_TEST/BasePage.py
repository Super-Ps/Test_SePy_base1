#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Jonny"
# Email: jonnysps@yeah.net
# Date: 2017/12/12

from selenium import  webdriver
from selenium.webdriver.common.action_chains import ActionChains  # 导入鼠标操作类
from selenium.webdriver.support.select import Select   #导入Select类

from selenium.common.exceptions import * # 导入所有异常类

from selenium.webdriver.support import expected_conditions as EC   # 判断元素类

from selenium.webdriver.support.wait import WebDriverWait

import time

# 封装所有页面都共用的方法， dirver `url` findelement

class basefunction(object):

    def __init__(self,selenium_driver):

        self.driver = selenium_driver
        #self.base_url = base_url

    ''' 请求url 判断title '''
    def open(self, url, t='百度搜索', timeout=10):

        self.driver.get(url)
        self.driver.maximize_window()
        try:
            WebDriverWait(self.driver, timeout, 0.5).until(EC.title_contains(t))
        except TimeoutException:
            print("open %s title error" % url)
        except Exception as msg:
            print("Error:%s" % msg)

    def qiut(self):
        self.driver.quit()



    def find_element(self,locator,timeout=10):

        try:
            # 判断某个元素是否被加到了dom树里,并不代表该元素一定可见

           # element = WebDriverWait(self.driver,timeout,1).until(EC.presence_of_all_elements_located(locator))
            element = WebDriverWait(self.driver,timeout,1).until(EC.presence_of_element_located(locator))
        except TimeoutException:
            print("定位失败：%s" % str(locator))
            return False
        else:
            return element

    # 封装元素点击操作
    def click(self, locator):
        element = self.find_element(locator)
        element.click()

    # 输入
    def send_keys(self,locator,text):
        element = self.find_element(locator)

        element.clear()  # 先清除文本
        element.send_keys(text)

    # 获取title
    def get_title(self):

        return self.driver.title

    # 获取文本
    def get_text(self,locator):

        element=self.find_element(locator)
        return element.text

    # 执行js
    def js_execute(self,js):

        return self.driver.execute.script(js)

    # 滚动到底部
    def js_scroll_end(self):

        js = "window.scrollTo(0,document.body.scrollHeight)"
        self.driver.execute(js)

    # 判断文本在元素里，没定位到元素返回False，定位到返回判断结果布尔值
    def is_text_in_element(self,locator, text, timeout=10):

        try:
            result = WebDriverWait(self.driver, timeout, 1).until(EC.text_to_be_present_in_element(locator, text))

        except TimeoutException:
            print("元素没有定位到："+str(locator))
            return False
        else:
            return result

    def move_to_element(self,locator):

        try:
            element=self.find_element(locator)
            ActionChains(self.driver).move_to_element(element).perform()
        except TimeoutException:
            print("元素没有定位到："+str(locator))
        else:
            time.sleep(2)

    # #截图
    # def get_screnn(self):
    #     # 格式化当前时间
    #    nowtime = time.strftime("%Y_%m_%d_%H_%M_%S")
    #     # 截图方法传递时间参数作为截图文件动态名称
    #    self.driver.get_scrennshot_as_file("%s.jpg" % nowtime)
    #
    # # 断言失败异常新增截图 装饰器
    # def screnn(self, func):
    #     def inner(*args, **kwargs):
    #         try:
    #             f = func(*args, **kwargs)
    #             return f
    #         except:
    #             self.get_screnn()
    #             raise
    #         return inner








    # 刷新






#if __name__ == '__main__':


#     driver=webdriver.Chrome()
#     a=basefunction(driver)
#     #
#     a.open("http://bbs.makex.cc/portal.php")
#
#     login_xpath = ("xpath",".//*[@id='nv_portal']/div[3]/div[1]/div[3]/a[1]")
#     username_name = ("name","username")
#     password_name = ("name","password")
#     lgoin_name = ("name","loginsubmit")
#
#     #a.find_element(login_xpath)
#     a.click(login_xpath)
#
#     sleep(3)
#     a.send_keys(username_name,"3433201@qq.com")
#     sleep(20)
#     a.send_keys(password_name, "jy123456")
#     a.click(lgoin_name)

