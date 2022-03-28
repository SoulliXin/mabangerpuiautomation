# -*- codeing = utf-8 -*-
# @time : 2022/3/2 15:06
# @Author : LiXinRan
# @File : Bace_requests.py.py
# @Software: PyCharm
import os
import sys
import requests
import json
base_path = os.path.abspath(os.path.dirname(__file__)).split('Base')
sys.path.append(base_path)

class BaseRequest:

    def send_post(self,url,data,cookie=None,headers=None):
        '''
        send post method request
        '''
        response =  requests.post(url=url,data=data,cookies=cookie,headers=headers)
        # if get_cookie !=None:
        #     cookie_value_jar = response.cookies
        #     cookie_value = requests.utils.dict_from_cookiejar(cookie_value_jar)
        #     write_cookie(cookie_value,get_cookie['is_cookie'])

        res = response.text
        return res

    def send_get(self,url,data,cookie=None,headers=None):
        '''
        send get method request

        '''

        response = requests.get(url=url,data=data,cookies=cookie,headers=headers)
        # if get_cookie !=None:
        #     cookie_value_jar = response.cookies
        #     cookie_value = requests.utils.dict_from_cookiejar(cookie_value_jar)
        #     write_cookie(cookie_value,get_cookie['is_cookie'])
        res = response.text
        return res

    def run_main(self,url,data,cookies=None,headers=None):
        # if method == "post":
        res = self.send_post(url,data,cookies,headers)
        # else:
        #     res = self.send_get(url,data,cookies,headers)
        # try:
        #     res = json.loads(res)
        # except:
        #    print('This is a text response')
        return res




login_api = "https://www.mabangerp.com/index.php?mod=main.doLogin"