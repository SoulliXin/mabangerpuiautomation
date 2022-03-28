# -*- codeing = utf-8 -*-
# @time : 2022/3/17 16:50
# @Author : LiXinRan
# @File : Testpublic.py
# @Software: PyCharm
import time

from selenium import webdriver
from selenium.webdriver.common.by import By

from Page.PageOperation import CommonPage


from selenium import webdriver



driver = webdriver.Chrome()
driver.get("https://www.mabangerp.com/main_loginV2.htm?1=1")
driver.maximize_window()
# 输入账号
driver.find_element(By.XPATH,"//form[@id='loginForm']/div[1]/input").send_keys('17675735413')
time.sleep(2)
# 输入密码
driver.find_element(By.XPATH,"//input[@name='password' and @id='loginPassWord']").send_keys('MB17675735413')
time.sleep(2)
# 点击登录
time.sleep(2)
driver.find_element(By.XPATH,"//button[@class='loginBtn' and @id='loginBtnKeyCode']").click()
time.sleep(2)
driver.find_element(By.XPATH,"//button[@data-bb-handler='cancel']").click()  #此账号有弹出充值框，点击取消

# 点击刊登导航栏按钮
driver.find_element(By.XPATH,"//ul[@id='mb-nav']/li[2]/a").click()
time.sleep(2)
# 点击数据采集
driver.find_element(By.XPATH,"//a[text()='数据采集']").click()
time.sleep(2)
# 点击阿里巴巴刊登list
driver.find_element(By.XPATH,"//i[text()='阿里巴巴国际站刊登']").click()
time.sleep(2)
# 点击新增刊登
iframe = driver.find_element(By.ID,"iframeContent") # 找到iframe元素
driver.switch_to.frame(iframe) # 切换到iframe
driver.find_element(By.XPATH,"//span[text()=' 新增刊登 ']").click()
time.sleep(2)
# 切换出来光标到默认位置
driver.switch_to.default_content()
# 获取两个窗口的句柄
allhand = driver.window_handles
# 切换新的句柄
driver.switch_to.window(allhand[-1])

# 选择店铺
iframe1 = driver.find_element(By.ID,"iframeContent") # 找到新的iframe元素
print(iframe1)
driver.switch_to.frame(iframe1) # 切换到新的iframe
try:
    shop_elements = driver.find_elements(By.XPATH,"//input[@type='text' and @placeholder='请选择']")# 定位下拉框元素
    print(shop_elements)
    shop_elements[0].click()# 选择店铺下拉框并且点击
    time.sleep(2)
except Exception:
    print("没找到店铺信息")
try:
    driver.find_element(By.XPATH,"//li[@class='el-select-dropdown__item hover']").click()
    time.sleep(2)
except Exception:
    print("该账号没有店铺或者没有授权")

# 选择分类
driver.find_element(By.XPATH,"//span[text()=' 选择分类 ']").click()# 点击选择分类按钮
time.sleep(2)
# 找到分类的元素

# 分别选择服装，婴儿服装、婴儿套装分类
driver.find_element(By.XPATH,"//label[@title='Apparel']").click()
time.sleep(1)
driver.find_element(By.XPATH,"//label[@title='Baby Clothing']").click()
time.sleep(1)
driver.find_element(By.XPATH,"//label[@title='Baby clothing sets']").click()
time.sleep(1)
# 点击确定按钮
ss = driver.find_elements(By.XPATH,"//span[text()='确 定']")
time.sleep(1)
ss[0].click()

