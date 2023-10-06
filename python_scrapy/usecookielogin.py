# -*- coding:utf-8 -*-
# @FileName  :table_demo.py
# @Time      :2023/10/6 9:42
# @Author    :dzz
# @Function  :
import json
from urllib.parse import urljoin

import requests
from lxml import etree
from bs4 import BeautifulSoup
import re
import csv
from faker import Faker

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36",
    "Content-Type": "application/json"
}
#
#
# # sess = requests.Session()
# resp = requests.get("https://woniuxy.com/",headers=headers)
#
# print(resp.text)
# 多步操作要使用session
# sess = requests.Session()
# resp = sess.get("https://woniuxy.com/sys/user/captcha?t=Math.random()")
# with open('checkcode.png', 'wb') as file:
#     file.write(resp.content)
#
# checkcode = input("请输入验证码")
# datas = {
#     "tel": "15591819289",
#     "password": "708170",
#     "captcha": checkcode,
#     "loginType": 1
# }
#
# resp2 = sess.post("https://woniuxy.com/sys/user/login", data=json.dumps(datas),headers=headers)
# print(resp2.text)
# sess.post("https://woniuxy.com/user/authstudent/433")


print("github")
resp = requests.get("https://github.com/login", headers=headers)

soup = BeautifulSoup(resp.text, 'lxml')

authenticity_token = soup.select_one('input[name="authenticity_token"]').get('value')

print(authenticity_token)
