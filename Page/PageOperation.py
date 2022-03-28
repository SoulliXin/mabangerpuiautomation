# -*- codeing = utf-8 -*-
# @time : 2022/3/2 17:02
# @Author : LiXinRan
# @File : PageOperation.py
# @Software: PyCharm
from Base.Find_element import FindElement
from selenium import webdriver

class CommonPage:
    def __init__(self,driver):
        self.fd = FindElement(driver)

    # 获取输入账号元素
    def getAcount(self):
        return self.fd.Get_element('CommonElements','usernameelement')
    # 获密码元素
    def getPswd(self):
        return self.fd.Get_element('CommonElements','passwordelement')
    # 获取登录元素
    def getLoginbt(self):
        return self.fd.Get_element('CommonElements','logingbutton')



class AlibabaPublish:
    def __init__(self,driver):
        self.fd = FindElement(driver)

    # 阿里巴巴国际站list按钮
    def getAlbabaList(self):
        return self.fd.Get_element('alibaba','albababt')

    #此账号有弹出充值框，取消元素
    def getTopupWindow(self):
        if self.fd.Get_element('alibaba','cancelelement'):
            return self.fd.Get_element('alibaba','cancelelement')
        else:
            return None
    #获取导航栏元素
    def getNavigation(self):
        return self.fd.Get_element('CommonElements','navigation')

    # 获取数据采集元素
    def getDatacolleciton(self):
        return self.fd.Get_element('CommonElements','datacollection')

    #获取iframe元素
    def getIframe(self):
        return self.fd.Get_element('alibaba','iframeelement')

    #获取新增刊登元素
    def getNewPulish(self):
        return self.fd.Get_element('alibaba','thenewpublish')
    #获取下拉框元素
    def getDropDownBox(self):
        return self.fd.Get_element('alibaba','dropdownbox')
    #获取店铺元素
    def getShopElement(self):
        return self.fd.Get_element('alibaba','shopelement')
    #获取分类按钮元素
    def getClassifyButton(self):
        return self.fd.Get_element('alibaba','classifybutton')
    #获取分类1
    def getFirstClassify(self):
        return self.fd.Get_element('alibaba','clothing')
    #获取分类2
    def getSecondeClassify(self):
        return self.fd.Get_element('alibaba','babyclothing')
    #获取分类3
    def getThirdlyClassify(self):
        return self.fd.Get_element('alibaba','babysuit')
    #获取分类确定按钮元素
    def getConfirmButton(self):
        return self.fd.Get_element('alibaba','confirmbuttons')






if __name__ == '__main__':
    driver = webdriver.Chrome()
    driver.get("https://www.mabangerp.com/main_loginV2.htm?1=1")
    lk = CommonPage(driver)
    ss = lk.getAcount()
    print(ss)
