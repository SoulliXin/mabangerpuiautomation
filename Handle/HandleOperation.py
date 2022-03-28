# -*- codeing = utf-8 -*-
# @time : 2022/3/2 16:56
# @Author : LiXinRan
# @File : HandleOperation.py
# @Software: PyCharm
import time
from Page.PageOperation import CommonPage,AlibabaPublish



class Handlcommon:
    def __init__(self,driver):
        self.CommonHandle = CommonPage(driver)




    # 1.输入账号操作
    def sendAcount(self,username):
        username = str(username)
        self.CommonHandle.getAcount().send_keys(username)
        time.sleep(1)

    # 2.输入密码操作
    def sendPaswd(self,password):
        password = str(password)
        self.CommonHandle.getPswd().send_keys(password)
        time.sleep(1)

    # 3.点击登录按钮操作
    def clickBt(self):
        self.CommonHandle.getLoginbt().click()
        time.sleep(1)






class HandleAlibabaPublic:
    def __init__(self,driver):
        self.AlibabaHandle = AlibabaPublish(driver)
        self.driver = driver
    # 1.充值弹窗点击取消操作
    def cancleclick(self):
        self.AlibabaHandle.getTopupWindow().click()
    # 2.点击刊登导航栏操作
    def clickNavigation(self):
        self.AlibabaHandle.getNavigation().click()
    # 3.点击数据采集操作
    def clickDatacollection(self):
        self.AlibabaHandle.getDatacolleciton().click()
    # 4.点击阿里巴巴刊登list
    def clickAlibabaList(self):
        self.AlibabaHandle.getAlbabaList().click()

    # 5.第一次定位iframe元素操作
    def Swichiframe(self):
        iframe = self.AlibabaHandle.getIframe()
        self.driver.switch_to.frame(iframe)



    # 6.点击新增刊登操作
    def clickNewPubish(self):
        self.AlibabaHandle.getNewPulish().click()

    # 7.切换出来光标到默认位置
    def swichOut(self):
        self.driver.switch_to.default_content()
    # 8.获取两个窗口的句柄# 9.切换新的句柄
    def getHandles(self):
        handles = self.driver.window_handles
        self.driver.switch_to.window(handles[-1])
    # 10.选择店铺
    # 11.切换新的iframe

    # 12.选择店铺下拉框并且点击操作
    def clickDropDownBox(self):
        boxelements = self.AlibabaHandle.getDropDownBox()
        boxelements.click()

    # 13.选择店铺操作
    def choseShop(self):
        self.AlibabaHandle.getShopElement().click()

    # 14.选择分类操作
    def choseClassify(self):
        self.AlibabaHandle.getClassifyButton().click()
        self.AlibabaHandle.getFirstClassify().click()
        self.AlibabaHandle.getSecondeClassify().click()
        self.AlibabaHandle.getThirdlyClassify().click()

    # 15.点击确定操作
    def clickConfirm(self):
        self.AlibabaHandle.getConfirmButton().click()