# -*- coding:utf-8 -*-
# @FileName  :urllibdemo.py
# @Time      :2023/7/10 10:49
# @Author    :dzz
# @Function  :
import http
import json
import urllib.request
import urllib.parse
from urllib import request


#
#
# resp:http.client.HTTPResponse = request.urlopen('https://www.hao123.com') #访问页面
# print(type(resp))
#
# print(dir(resp))
# print(resp.msg)
#
#

def urllib_get():
    user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36"
    headers = {
        "User-Agent": user_agent
    }
    # 构造request对象 以便我们设置http请求的header信息
    req = urllib.request.Request('https://www.hao123.com', headers=headers)

    resp = urllib.request.urlopen(req)

    print(resp.read().decode())


def urllib_post():
    user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36"
    headers = {
        "User-Agent": user_agent,
        "Content-Type": "application/json",
        "Host":"woniuxy.com"
    }
    datas = {
        'tel': "13788399433",
        'password': "222",
        'captcha': "0223",
         'loginType':1
    }

    datas = urllib.parse.urlencode(datas).encode()  # parse.urlencode 按照http报文要求的格式将字典数据进行编码  encode:数据类型进行编码 将字符串编码为字节串

    req = urllib.request.Request('https://woniuxy.com/sys/user/login', headers=headers, data=datas, method='POST')
    resp = urllib.request.urlopen(req)
    print(resp.read().decode())


if __name__ == '__main__':
    urllib_post()
