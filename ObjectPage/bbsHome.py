#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Jonny"
# Email: jonnysps@yeah.net
# Date: 2017/12/12


from selenium import webdriver

from SE_TEST.BasePage import basefunction

from time import sleep as s

    # bbs首页类 继承原生封装方法类
class Bbshmoe(basefunction):

    login_loc = ("xpath", ".//*[@id='nv_portal']/div[3]/div[1]/div[3]/a[1]") # 点击登录
    username_loc = ("name", "username")
    password_loc = ("name", "password")
    lgoin_loc = ("name", "loginsubmit")

    exit_loc = ("link text", "新手上路")
    exit_click_loc = ("class name", "graysmallbutton")

    # 社区讨论 查看帖子第一行
    search_loc = ("xpath", ".//*[@id='index']/div[1]/div[2]/div[3]/div[1]/div[2]/a")





    # 点击登录按钮
    def login_hmoe_click(self):

        self.click(self.login_loc)

    # 输入用户名
    def input_username(self,username):
        self.send_keys(self.username_loc,username)

    # 输入密码
    def input_password(self,password):

        self.send_keys(self.password_loc,password)

    # 点击提交按钮
    def click_submit(self):

        self.click(self.lgoin_loc)

    # 登陆方法
    def logins(self,username,password):
        self.login_hmoe_click()
        self.input_username(username)
        self.input_password(password)

        s(20)
        self.click_submit()
    # 退出方法
    def system_exit(self):

        self.move_to_element(self.exit_loc)
        self.click(self.exit_click_loc)
        #s(2)
        #self.qiut()

    def click_threadlist(self):

        self.click(self.search_loc)


# if __name__ =="__main__":
#
#     driver=webdriver.Chrome()
#     bb=Bbshmoe(driver)
#     bb.open("http://bbs.makex.cc/portal.php")
#     bb.login("3433201@qq.com","jy123456")
