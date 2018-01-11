#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Jonny"
# Email: jonnysps@yeah.net
# Date: 2017/12/26

import unittest
from time import sleep as s
from selenium import webdriver
from Test_SePy_base1.ObjectPage.BaiduHome import baidupage
from Test_SePy_base1.ObjectPage.BasePage import basefunction
from Test_SePy_base1.ObjectPage.DecoratorScreen import Screen



class BaiDuLogin_Test(unittest.TestCase):

    driver = webdriver.Chrome()

    @classmethod
    def setUpClass(cls):

        cls.bd = baidupage(cls.driver)

        cls.base = basefunction(cls.driver)

    @classmethod
    def tearDownClass(cls):
        pass
    @Screen
    def test_search01(self):
        self.base.open("https://www.baidu.com")
        #self.base.
        self.bd.baidu_input_text("selenium")
    @Screen
    def test_search02(self):
        #self.base.open("https://www.baidu.com")
        self.bd.baidu_click()



