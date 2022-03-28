# -*- codeing = utf-8 -*-
# @time : 2022/3/25 11:20
# @Author : LiXinRan
# @File : Runcase.py
# @Software: PyCharm
import os
import sys
import time
from Lib.HwTestReport import HTMLTestReportEN
import unittest

base_path = os.path.abspath(os.path.dirname(__file__)).split('util')[0]
sys.path.append(base_path)
# print(base_path)
case_path = base_path + "/Case"
# print(case_path)
tests = unittest.defaultTestLoader.discover(case_path,'*Case.py')
suit =unittest.TestSuite()
suit.addTest(tests)
report_path = base_path + '/Report'
nowtime = time.strftime("%Y%m%d.%H.%M.%S")
file_path = report_path + "/Report" + nowtime+".html"

f = open(file_path, 'wb')

runner = HTMLTestReportEN(stream=f,title='自动化测试报告',description='执行结果：',verbosity=2,tester='LiXinRan')
res = runner.run(suit)
f.close()