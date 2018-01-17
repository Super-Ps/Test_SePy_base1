#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Q1mi"
# Email: master@liwenzhou.com
# Date: 2018/1/17


import os
from selenium import webdriver





d=webdriver.Chrome()
d.get("https:www.baidu.com")



print(d.title)
