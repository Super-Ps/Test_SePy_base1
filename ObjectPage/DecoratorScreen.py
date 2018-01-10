#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Jonny"
# Email: jonnysps@yeah.net
# Date: 2017/12/26

from selenium import webdriver


class Screen(object):
    def __init__(self, driver):
        self.driver = driver

    def __call__(self, func):

        def inner(*args):
            try:
                return func(*args)
            except:
                import time
                nowtime = time.strftime("%Y_%m_%d_%H_%M_%S")
                srceen_png = self.driver.get_screenshot_as_file("C:/Users/Administrator/Desktop/SE/FalsScreen/%s.PNG" % nowtime)
                print(srceen_png)
                raise
        return inner












