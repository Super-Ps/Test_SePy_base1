#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Jonny"
# Email: jonnysps@yeah.net
# Date: 2017/12/27
import os
import time
import imaplib
import smtplib
from email.mime.text import MIMEText
from email.header import Header

from email.mime.multipart import MIMEMultipart

#from Test_SePy_base1.SendEmail.textmail2 import git_max_repor


report_dir = 'D:/git_local/Test_SePy_base1/Report/'


def send_mail(max_file,from_addr="jonny.peng@makeblock.com",to_addr="jonny.peng@makeblock.com",
              account="jonny.peng@makeblock.com",passwd_ssl="~~~~~~~",
              smtpserver="smtp.exmail.qq.com"):
    nowitme = time.strftime("%Y_%m_%d_%H_%M_%S")


    f= open(max_file, 'rb')
    mailcontent_s = f.read()
    f.close()
    msg = MIMEText(mailcontent_s, _subtype='html', _charset='utf-8')
#msg = MIMEMultipart()
    subject = "Makeblock_Laser-cut自动化报告" + nowitme  # 邮件主题
    # 设置头
    msg['Subject'] = Header(subject, 'utf-8')
    # 发件人
    msg['from'] = "jonny.peng@makeblock.com"
    # 收件
    msg['to'] = "jonny.peng@makeblock.com"

#msg.attach(MIMEText(ptah_max_report,_subtype='html',_charset='utf-8'))
    try:
        smtp = smtplib.SMTP_SSL(smtpserver,465)
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
    git_max_repor()