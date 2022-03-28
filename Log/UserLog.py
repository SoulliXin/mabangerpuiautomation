# -*- codeing = utf-8 -*-
# @time : 2022/3/23 14:03
# @Author : LiXinRan
# @File : UserLog.py
# @Software: PyCharm
import logging
import time
import os

class LogTool:
    def __init__(self,logger=None):
        '''
        指定保存日志的文件路径，日志级别，以及调用文件
        将日志存入到指定的文件中
        '''
        # 创建一个logger
        self.logger = logging.getLogger(logger)
        self.logger.setLevel(logging.DEBUG)
        # 创建handler，用于写入日志文件
        self.log_time = time.strftime("%Y_%m_%d_")
        base_dir = os.path.dirname(os.path.abspath(__file__))
        self.log_path = os.path.join(base_dir, 'Log')
        self.log_name = self.log_path + self.log_time + 'lg.log'
        fh = logging.FileHandler(self.log_name,'a',encoding='utf-8')
        fh.setLevel(logging.INFO)
        # 再创建一个handler，用于输出控制台
        # ch = logging.StreamHandler()
        # ch.setLevel(logging.INFO)
        # 定义handler的输出格式
        formatter = logging.Formatter('%(asctime)s %(filename)s--> %(funcName)s %(levelno)s: %(levelname)s ----->%(message)s')
        fh.setFormatter(formatter)
        # ch.setFormatter(formatter)
        # 给logger添加handler
        self.logger.addHandler(fh)
        # self.logger.addHandler(ch)
        fh.close()
        # ch.close()



    def getLog(self):
        return self.logger

