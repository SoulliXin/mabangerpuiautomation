# -*- codeing = utf-8 -*-
# @time : 2022/3/2 17:03
# @Author : LiXinRan
# @File : BusinessOperation.py
# @Software: PyChar
import time

from Handle.HandleOperation import Handlcommon,HandleAlibabaPublic



class CommonBusiness:
    def __init__(self,driver):
        self.HandLog = Handlcommon(driver)

    def userLogin(self,username,password):
        self.HandLog.sendAcount(username)
        self.HandLog.sendPaswd(password)
        self.HandLog.clickBt()


class AlibabaBusiness:
    def __init__(self,driver):
        self.AlibabaB= HandleAlibabaPublic(driver)


    def AlibabaPublic(self):
        try:
            self.AlibabaB.cancleclick()
        except Exception:
            print("此账号没有充值弹窗出现")
        self.AlibabaB.clickNavigation()
        self.AlibabaB.clickDatacollection()
        self.AlibabaB.clickAlibabaList()
        time.sleep(1)
        self.AlibabaB.Swichiframe()
        time.sleep(1)
        self.AlibabaB.clickNewPubish()
        self.AlibabaB.swichOut()
        time.sleep(1)
        self.AlibabaB.getHandles()
        time.sleep(1)
        self.AlibabaB.Swichiframe()
        time.sleep(1)
        self.AlibabaB.clickDropDownBox()
        try:
            self.AlibabaB.choseShop()
        except Exception:
                print("该账号没有店铺信息")
        self.AlibabaB.choseClassify()
        self.AlibabaB.clickConfirm()





