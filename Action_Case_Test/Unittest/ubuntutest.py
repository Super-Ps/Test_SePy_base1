#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Q1mi"
# Email: master@liwenzhou.com
# Date: 2018/1/17


import os
from selenium import webdriver

from Test_SePy_base1.Report.importtest import grt_time




d=webdriver.Chrome()
d.get("https:www.baidu.com")

a=grt_time()

print("标题是：%s" % d.title)
print("时间是：%s" % a)
