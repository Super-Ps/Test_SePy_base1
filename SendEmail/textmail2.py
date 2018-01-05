#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Jonny"
# Email: jonnysps@yeah.net
# Date: 2017/12/29


import os
import time
from email.mime.text import MIMEText

from email.header import Header

from email.mime.multipart import MIMEMultipart



result_dir = "C:\\Users\\Administrator\\Desktop\\SE\\Report"

lists_fial =os.listdir(result_dir)

lists_pop=lists_fial[:-2]
print(lists_fial)
print(lists_pop)

#b=os.path.getmtime(lists_pop)
#列表最大值
b=max(lists_pop)
#a=lists_pop.reverse()
#a=lists_fial[0]
#a=lists_fial.sort(key=lambda x: os.path.getmtime(lists_fial+'\\'+lists_fial) )


#print(a)
print(b)