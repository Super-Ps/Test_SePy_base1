#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Jonny"
# Email: jonnysps@yeah.net
# Date: 2017/12/26

from HTMLTestRunner import HTMLTestRunner
from HTMLTestRunner_JONNY import HTMLTestRunner
import smtplib
from email.mime.text import MIMEText
from email.header import Header
import  time
import unittest

import os


# case路劲
case_path = os.path.join(os.getcwd(), "Action_Case_Test\\Unittest")
print(case_path)


# 报告存放路径
report_path = os.path.join(os.getcwd(), "Report")
print(report_path)

# 报告路劲
report_dir = 'D:/git_local/Test_SePy_base1/Report/'



def all_case():

    discover = unittest.defaultTestLoader.discover(case_path,
                                        pattern="Test_*.py",
                                        top_level_dir=None)

    print(discover)
    return discover

def send_mail(max_file,from_addr="jonny.peng@makeblock.com",to_addr="jonny.peng@makeblock.com",
              account="jonny.peng@makeblock.com",passwd_ssl="G6sNcvPkE2GWWQPb",
              smtpserver="smtp.exmail.qq.com"):
    nowitme = time.strftime("%Y_%m_%d_%H_%M_%S")

    f = open(max_file, 'rb')
    mailcontent_s = f.read()
    f.close()
    msg = MIMEText(mailcontent_s, _subtype='html', _charset='utf-8')
    # msg = MIMEMultipart()
    subject = "Makeblock_Laser-cut自动化报告" + nowitme  # 邮件主题
    # 设置头
    msg['Subject'] = Header(subject, 'utf-8')
    # 发件人
    msg['from'] = "jonny.peng@makeblock.com"
    # 收件
    msg['to'] = "jonny.peng@makeblock.com"

    # msg.attach(MIMEText(ptah_max_report,_subtype='html',_charset='utf-8'))
    try:
        smtp = smtplib.SMTP_SSL(smtpserver, 465)
        smtp.login(account, passwd_ssl)

        smtp.sendmail(from_addr, to_addr, msg.as_string())  # 把MIMEText 转化成str
        smtp.set_debuglevel(1)
        smtp.quit()
        # smtp= smtplib.SMTP()
        # smtp.connect(smtpserver)
        # smtp.set_debuglevel(1)
        # smtp.login(account, passwd_ssl)
    except Exception as e:
        raise ('e:', e)

    return


def git_max_repor():

    #report_dir = "D:/git_local/Test_SePy_base1/Report/"
    lists_count = os.listdir(report_dir)
    # print(type(lists_count))
    print('排序前的列表： ', lists_count)
    # print(os.path.getmtime(result_dir))
    # print(os.path.getctime(result_dir))
    lists_count.sort(key=lambda x: os.path.getmtime(report_dir +'\\'+ x)if not os.path.isdir(report_dir +'\\'+x) else 0)
    print("排序后的列表：", lists_count)
    # 组合目录与最新文件
    max_file = os.path.join(report_dir, lists_count[-1])
    print("下标-1的元素：" , lists_count[-1])
    print(max_file)

    send_mail(max_file)


if __name__ == "__main__":

    # 写html报告
    import time
    nowtime = time.strftime("%Y_%m_%d_%H_%M_%S")
    report_html_path = os.path.join(report_path, "result"+nowtime+".html")
    fp = open(report_html_path, "wb")
    runner = HTMLTestRunner(stream=fp,
                       title ="全量执行测试报告",
                       description = "具体执行情况",
                        verbosity =2)
                            #retry=1)

    runner.run(all_case())

    fp.close()
    git_max_repor()





