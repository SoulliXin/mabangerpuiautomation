# -*- codeing = utf-8 -*-
# @time : 2022/3/23 9:57
# @Author : LiXinRan
# @File : AlibabaPublicCase.py
# @Software: PyCharm
import unittest
from Business.BusinessOperation import CommonBusiness,AlibabaBusiness
from selenium import webdriver
from Lib.HwTestReport import HTMLTestReportEN
import os
import time
import sys


class AlibabaCase(unittest.TestCase):

    def setUp(self) -> None:
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(5)
        self.driver.get('https://www.mabangerp.com/main_loginV2.htm?1=1')
        self.driver.maximize_window()
        self.CB = CommonBusiness(self.driver)
        self.CB.userLogin('mabangtest','mabangit')
        self.AB = AlibabaBusiness(self.driver)

    def tearDown(self) -> None:
        self.driver.close()



    def testAlibabaPublishCase(self):
        self.AB.AlibabaPublic()

if __name__ == '__main__':
    base_path = os.path.abspath(os.path.dirname(__file__)).split('util')[0]
    sys.path.append(base_path)
    nowtime = time.strftime("%Y%m%d.%H.%M.%S")
    file_path = base_path + "/Report" + "/publishTest"+nowtime+".html"

    f = open(file_path, 'wb')
    suite = unittest.TestSuite()
    suite.addTest(AlibabaCase('testAlibabaPublishCase'))
    runner = HTMLTestReportEN(stream=f,title='自动化测试报告',description='执行结果：',verbosity=2,tester='LiXinRan')
    res = runner.run(suite)
    f.close()