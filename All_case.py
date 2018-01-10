#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Jonny"
# Email: jonnysps@yeah.net
# Date: 2017/12/26

from HTMLTestRunner import HTMLTestRunner
from HTMLTestRunner_JONNY import HTMLTestRunner

import unittest

import os


# case路劲
case_path = os.path.join(os.getcwd(), "Action_Case_Test\\Unittest")
print(case_path)

report_path = os.path.join(os.getcwd(), "Report")
print(report_path)


def all_case():

    discover = unittest.defaultTestLoader.discover(case_path,
                                        pattern="Test_*.py",
                                        top_level_dir=None)

    print(discover)
    return discover


if __name__ == "__main__":

    # 写html报告
    import time
    nowtime = time.strftime("%Y_%m_%d_%H_%M_%S")
    report_html_path = os.path.join(report_path, "result"+nowtime+".html")
    fp = open(report_html_path, "wb")
    runner = HTMLTestRunner(stream=fp,
                       title ="全量执行测试报告",
                       description = "具体执行情况",
                        verbosity =2,
                            retry=1)

    runner.run(all_case())

    fp.close()




