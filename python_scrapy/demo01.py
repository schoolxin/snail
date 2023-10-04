# -*- coding:utf-8 -*-
# @FileName  :demo01.py
# @Time      :2023/10/4 9:28
# @Author    :dzz
# @Function  :
import requests

# 设置请求参数
params={
    '':""
}

url = "http://httpbin.org/cookies"
headers = {
    'name': "woniu",
    'pwd': '123',
    'Cookie': 'cna=WXE+HdAmtQ4CAX1MsSPI95Dw; sca=fe661f45; yunpk=238170963846161394; tbsa=2d825acda6de06b59587756d_1694670404_8; cnaui=%2522iraq.deng%2520%2540%2520orderplus%2522; aui=%2522iraq.deng%2520%2540%2520orderplus%2522; atpsida=48f3455568ea1bb21b9c13cc_1696382533_13'
}
# r = requests.get(url,headers=headers)

# print(r.text)
# 保持会话状态
sess = requests.Session()
sess.get("http://httpbin.org/cookies/set?sessioncookiess=12234")
r = sess.get("http://httpbin.org/cookies")
# print(r.text)

# 设置访问代理
proxies = {
    'https': "121.8.215.106:9797"
}
r = requests.get("https://httpbin.org/ip",proxies=proxies)
print(r.text)

if __name__ == "__main__":
    run_code = 0
