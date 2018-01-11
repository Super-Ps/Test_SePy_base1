#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Jonny"
# Email: jonnysps@yeah.net
# Date: 2017/12/8


from selenium.webdriver.support.wait import WebDriverWait
from selenium import  webdriver

# from ObjectPage.ObjectPage import basefunction
#
# class LoginPage(basefunction):


from Test_SePy_base1.ObjectPage.BasePage import basefunction



class baidupage(basefunction):
    # 百度验证
    baidu_loc = ("id", "kw")

    # 按钮
    baidu_click_loc = ("id", "su")

    # 输入
    def baidu_input_text(self,text):

        self.send_keys(self.baidu_loc,text)

    # 点击
    def baidu_click(self):

        self.click(self.baidu_click_loc)




# if __name__ =="__main__":
#
#     driver=webdriver.Chrome()
#     ddb=baidupage(driver)
#     ddb.open("https://www.baidu.com")
#     ddb.baidu_input_text("python")
#     ddb.baidu_click()




