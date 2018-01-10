#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Jonny"
# Email: jonnysps@yeah.net
# Date: 2017/12/12

import unittest

from time import sleep as s

from selenium import webdriver
from SE_TEST.bbsHome import Bbshmoe

from SE_TEST.BasePage import basefunction

from SE_TEST.DecoratorScreen import Screen


@unittest.skip("无条件跳过此测试类")
class Login_test(unittest.TestCase):

    driver = webdriver.Chrome()

    @classmethod
    def setUpClass(cls):

        cls.login = Bbshmoe(cls.driver)

        cls.base = basefunction(cls.driver)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()


    # def login_case(self,username,pws,excpet=True):
    #
    #     self.base.open("http://bbs.makex.cc/portal.php")
    #     self.login.login_hmoe_click()
    #
    #     self.login.input_username(username)
    #     self.login.input_password(pws)
    #
    #     s(10)
    #     self.login.click_submit()
    #
    #     self.base.get_title()
    #
    #     result = self.login.is_text_in_element(("xpath",".//*[@id='nv_portal']/div[3]/div[1]/div[3]/div[1]/a"),"3433201@qq.com")
    #
    #     excpet_result = excpet
    #
    #     self.assertEqual(result,excpet_result)

        # 登录成功
    #@Screen(driver)
    def test_login01(self):
        ''' 登陆成功！验证登陆账号 '''
        self.base.open("http://bbs.makex.cc/portal.php")
        self.login.logins("3433201@qq.com", "jy123456")
        result = self.login.is_text_in_element(("xpath", ".//*[@id='nv_portal']/div[3]/div[1]/div[3]/div[1]/a"),
                                               "3433201@qq.com")
        self.assertEqual(result, True, msg='登录失败：%s != %s' % (result, True))

    #@Screen(driver)
    def test_login02(self):
        ''' 退出登陆成功，验证退出后状态'''
        self.login.system_exit()
        result = self.login.is_text_in_element(("xpath", ".//*[@id='nv_portal']/div[3]/div[1]/div[3]/a[2]"),
                                               "立即1注册")
        self.assertEqual(result, True, msg='退出失败：%s != %s' % (result, True))

    #@Screen(driver)
    def test_login03(self):

        ''' 登陆有效账号，密码为空，验证提示：抱歉，密码空或包含非法字符 '''
        self.base.open("http://bbs.makex.cc/portal.php")
        self.login.logins("3433201@qq.com", "")
        result = self.login.is_text_in_element(("xpath", ".//*[@id='ntcwin']/table/tbody/tr/td[2]/div/i"),
                                               "抱歉，密码空或包含非法字符")
        self.assertEqual(result, True, msg=" 密码为空，登录失败！")






    # ''' 点击帖子第一行,跳转页面'''
    # def test_login03(self):
    #     # self.login_case("3433201@qq.com", "jy123456", True)
    #     # s(3)
    #     self.login.click_threadlist()
    #     result = self.login.is_text_in_element(("xpath", ".//*[@id='post_2495']/div[1]/div/h1/a[1]"), "赛事资料下载")
    #
    #     self.assertEqual(result,True)
    #     print("result:%s" % result)

if __name__ == "__main__":

    unittest.man()