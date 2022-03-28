# -*- codeing = utf-8 -*-
# @time : 2022/3/2 15:22
# @Author : LiXinRan
# @File : Requestserp.py
# @Software: PyCharm
import requests

from Bace_requests import BaseRequest


url ="https://www.mabangerp.com/index.php?mod=main.doLogin"

headers = {
    "accept": "application/json, text/javascript, */*; q=0.01",
    "accept-encoding":"gzip, deflate, br",
    "accept-language":"zh-CN,zh;q=0.9,ru;q=0.8",
    "content-type":"application/x-www-form-urlencoded; charset=UTF-8",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36"
}

data = {
    "username":"mabangtest",
    "password":"mabang3.0",
    "allowImageCode":1
}

res = requests.post(url=url,headers=headers,data=data)
cookies_jar = res.cookies
cookie_value = requests.utils.dict_from_cookiejar(cookies_jar)
print(cookie_value)
