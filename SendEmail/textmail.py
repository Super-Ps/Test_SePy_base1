#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Jonny"
# Email: jonnysps@yeah.net
# Date: 2017/12/27

import  time
import imaplib
import smtplib
from email.mime.text import MIMEText
from email.header import Header

from email.mime.multipart import MIMEMultipart

# with open("C:\\Users\\Administrator\\Desktop\\SE\\Report\\result2017_12_27_12_02_33.html","rb") as fp:
# #C:\Users\Administrator\Desktop\SE\Report
# #C:\Users\Administrator\Desktop\SE\Report\result2017_12_27_12_02_33.html
#     liset_report=fp.read()
#     print(liset_report)

# msg_html = MIMEMultipart()
# msg_html["from"] ="jonnypss@163.com"
# msg_html["to"] ="jonny.peng@makeblock.com"

nowitme = time.strftime("%Y_%m_%d_%H_%M_%S")

sender = "jonnypss@163.com"#"jonny.peng@makeblock.com " #"jonnypss@163.com"  # 发送邮箱

receiver ="jonny.peng@makeblock.com"  #"jonny.peng@makeblock.com"#"jonnyps@yeah.net"    #dextor.liu@makeblock.com

subject = "Makeblock_1laser-cut自动化报告"+nowitme # 邮件主题

smtpserver = "smtp.163.com"# smtp.exmail.qq.com"  #  smtp.163.com"  # 发送邮件服务器

email_username = "jonnypss@163.com"#"jonny.peng@makeblock.com"#"jonnypss@163.com"  # 发送邮箱账号 密码

email_pwd = "274094800" # "jy123456","274094800"


msg = MIMEText('你好，文本内容~这里是py输入', 'text','utf-8')

# 设置头
msg['Subject'] = Header(subject, 'utf-8')
# 发件人
msg['from'] = "jonnypss@163.com"
# 收件人
msg['to'] = "jonny.peng@makeblock.com"




#smtp=imaplib.IMAP4_SSL("imap.exmail.qq.com",993)

smtp= smtplib.SMTP()

#smtp =smtplib.SMTP_SSL(smtpserver,port=465)

#smtp.starttls()
smtp.connect(smtpserver)

smtp.set_debuglevel(1)

#
smtp.login(email_username,email_pwd)
smtp.sendmail(sender,receiver, msg.as_string())  # 把MIMEText 转化成str
smtp.quit()

