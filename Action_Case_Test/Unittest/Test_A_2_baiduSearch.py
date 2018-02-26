#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Jonny"
# Email: jonnysps@yeah.net
# Date: 2017/12/26


import sys
sys.path.append("/usr/local/git_d_local/Test_SePy_base1/Action_Case_Test/Unittest")
#sys.path.append("..")

print(sys.path)
import unittest
import ddt
from time import sleep as s
from selenium import webdriver

from Test_SePy_base1.ObjectPage.BaiduHome import baidupage
from Test_SePy_base1.ObjectPage.BasePage import basefunction
from Test_SePy_base1.ObjectPage.DecoratorScreen import Screen
from Test_SePy_base1.ddt.dataoop import ExcelDate

exclepath = "D:\\git\\Test_SePy_base1\\ddt\\dataoop_t1.xlsx"
sheetname = 'Sheet2'

data = ExcelDate(exclepath, sheetname)

data_o = data.getexceldata()

#@unittest.skip
@ddt.ddt
class BaiDuLogin_Test(unittest.TestCase):

    driver = webdriver.Chrome()

    #print("data_o=%s"% data_o)


    @classmethod
    def setUpClass(cls):
        #cls.driver = webdriver.Chrome()
        cls.bd = baidupage(cls.driver)
        cls.base = basefunction(cls.driver)



    @classmethod
    def tearDownClass(cls):
        pass
        #cls.driver.quit()

    #@Screen
    @ddt.data(*data_o)
    def test_search01(self,data):
        #print('data=%s'%data)
        self.base.open(data['url'])
        s(2)

        #print("url=%s"% data["url"])
        #self.base.
        self.bd.baidu_input_text(data['input'])
        s(2)
       # print("input=%s" % data["input"])
        self.bd.baidu_click()
        s(2)
        #self.base.open(data['url'])
        #self.assertEqual()

   # @Screen
    #@ddt.data(*data_o)
    # def test_search02(self,data):
    #     self.base.open(data["url"])
    #     self.bd.baidu_input_text(data["input"])
    #     self.bd.baidu_click()


if __name__ == "__main__":

    unittest.main()

