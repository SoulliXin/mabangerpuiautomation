# -*- codeing = utf-8 -*-
# @time : 2022/3/2 13:57
# @Author : LiXinRan
# @File : Read_ini.py
# @Software: PyCharm

import configparser

class ReadIni:
    def __init__(self,filename=None,node=None):
        if filename == None:
            self.filename = "c:/MabangerpPublic/Config/Location_element.ini"
        if  node == None:
            self.node = ""
        else:
            self.node = node
        self.cf =self.LoadIni(self.filename)


    def LoadIni(self,filename):
        cf = configparser.ConfigParser()
        cf.read(filename)
        return cf

    def GetValue(self,node,key):
        data = self.cf.get(node,key)
        return data


if __name__ == '__main__':
    rd = ReadIni()
    es = rd.GetValue('Loging','usernameelement')
    print(es)