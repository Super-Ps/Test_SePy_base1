#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Jonny"
# Email: jonnysps@yeah.net
# Date: 2017/12/26

import unittest
from time import sleep as s
from selenium import webdriver
#from Test_SePy_base1.ObjectPage.BaiduHome import baidupage
#from Test_SePy_base1.ObjectPage.BasePage import basefunction
#from Test_SePy_base1.ObjectPage.DecoratorScreen import Screen


#@unittest.skip
class BaiDuLogin_Test(unittest.TestCase):

    driver = webdriver.Chrome()

    @classmethod
    def setUpClass(cls):
        #cls.driver = webdriver.Chrome()
        cls.bd = baidupage(cls.driver)

        cls.base = basefunction(cls.driver)

    @classmethod
    def tearDownClass(cls):
        pass
        cls.driver.quit()
    #@Screen
    def test_search01(self):
        self.base.open("https://www.baidu.com")
        #self.base.
        self.bd.baidu_input_text("selenium")

        self.assertEqual()
   # @Screen
    def test_search02(self):
        self.base.open("https://www.baidu.com")
        self.bd.baidu_click()



