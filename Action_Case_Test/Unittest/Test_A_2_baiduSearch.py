#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Jonny"
# Email: jonnysps@yeah.net
# Date: 2017/12/26

import unittest

from time import sleep as s

from selenium import webdriver

from SE_TEST.BaiduHome import baidupage

from SE_TEST.BasePage import basefunction

from SE_TEST.DecoratorScreen import Screen



class BaiDuLogin_Test(unittest.TestCase):

    driver = webdriver.Chrome()

    @classmethod
    def setUpClass(cls):

        cls.bd = baidupage(cls.driver)

        cls.base = basefunction(cls.driver)

    @classmethod
    def tearDownClass(cls):
        pass

    def test_search01(self):
        self.base.open("https://www.baidu.com")
        #self.base.
        self.bd.baidu_input_text("selenium")

    def test_search02(self):
        #self.base.open("https://www.baidu.com")
        self.bd.baidu_click(22)



