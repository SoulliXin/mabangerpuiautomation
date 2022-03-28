# -*- codeing = utf-8 -*-
# @time : 2022/3/2 13:54
# @Author : LiXinRan
# @File : Find_element.py.py
# @Software: PyCharm
import time

from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By

from Log.UserLog import LogTool
from Unit.Read_ini import ReadIni
from selenium import webdriver
import os
import sys





class FindElement:
    def __init__(self,driver):
        self.driver = driver
        Lt = LogTool()
        self.log = Lt.getLog()
    def Get_element(self,node,key):
        '''
        :param node:配置文件包中的ini文件模块名
        :param key:配置文件包中的ini文件关键字
        :return:返回通过定位找到的元素
        '''
        read_ini = ReadIni()
        data = read_ini.GetValue(node,key)
        by = data.split('>')[0]
        value = data.split('>')[1]
        try:
            if by == "id":
                return self.driver.find_element_by_id(value)
            elif by == 'name':
                return self.driver.find_element_by_name(value)

            elif by == 'className':
                return self.driver.find_element_by_classNmae(value)

            else:
                return self.driver.find_element(By.XPATH,value)
        except NoSuchElementException as e:
            base_path = os.path.abspath(os.path.dirname(__file__)).split('util')[0]
            sys.path.append(base_path)
            nowTime = time.strftime("%Y%m%d.%H.%M.%S")
            imgpath = base_path  + "/Report"
            print(imgpath)
            file_path = imgpath +  nowTime +".png"
            self.driver.save_screenshot(file_path)
            self.log.info('Error details:%s'%(e.args[0]))


if __name__ == '__main__':
    read_ini = ReadIni()
    data = read_ini.GetValue('Loging', 'usernameelement')
    by = data.split('>')[0]
    value = data.split('>')[1]
    print(by)
    print(value)
    driver = webdriver.Chrome()
    url = 'https://www.mabangerp.com/main_loginV2.htm?1=1'
    driver.get(url)
    es = driver.find_element(By.XPATH,value)
    es.send_keys('12345')
    print(es)
