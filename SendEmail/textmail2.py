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

#D:\git_local\Test_SePy_base1\Report

# def  git_max_repor():
#
#
#     result_dir = "D:/git_local/Test_SePy_base1/Report/"
#     lists_count = os.listdir(result_dir)
#     #print(type(lists_count))
#     print('排序前的列表：%s' % lists_count)
#     # print(os.path.getmtime(result_dir))
#     # print(os.path.getctime(result_dir))
#     lists_count.sort(key=lambda x: os.path.getmtime(result_dir+'\\'+x)
#     if not os.path.isdir(result_dir+'\\'+x) else 0)
#     print("排序后的列表：%s"%lists_count)
#     maxfile =os.path.join(result_dir,lists_count[-1])
#     print("下标-1的元素：%s"%lists_count[-1])
#     print(maxfile)

    # for i in lists_count:
    #     print('获取的i:',i)
    #     if i == max(lists_count):
    #         print(max(lists_count))
    #         fp=open(os.path.join(result_dir, i))
    #         max_list_boy = fp.read()
    #         fp.close()
    #         # with open(os.path.join(result_dir,i),"rb") as tp:
    #         #     max_list_boy = tp.read()
    #         # #     print(os.path.join(result_dir,i))
    #
    #         return max_list_boy#print(type(os.path.join(result_dir, i)))


    #lists_count =os.listdir(result_dir)

    #lists_pop=lists_count[:-1]
    #print(lists_count)
    #print(lists_pop)

    #b=os.path.getmtime(lists_pop)
    #列表最大值

    #a=lists_pop.reverse()
    #a=lists_fial[0]
    #a=lists_fial.sort(key=lambda x: os.path.getmtime(lists_fial+'\\'+lists_fial) )


    #print(a)
# g=git_max_repor()
# print(g)



git_max_repor()


