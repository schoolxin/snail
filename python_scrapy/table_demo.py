# -*- coding:utf-8 -*-
# @FileName  :table_demo.py
# @Time      :2023/10/6 9:42
# @Author    :dzz
# @Function  :
from urllib.parse import urljoin

import requests
from lxml import etree
from bs4 import BeautifulSoup
import re
import csv
from faker import Faker
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36",
    "Access-Token":"token#1723#90170502236213248",
    "Referer":"https://opstores.com/data/daily",
    "Cookie":"SESSION=MDVhNDhkZDUtNWZmZS00OWU4LWJkZDEtMjM3MDJiOTVjZDk4; Opstores-EncodeUserId=eyJ0eXAiOiJKV1QiLCJleHAiOjE2OTY1NzM2ODcsImFsZyI6IkhTMjU2In0.eyJpc3MiOiJPcHN0b3JlcyIsInVzZXJpZCI6IjE3MjMifQ.MD5IKnbfEvP22eFgQL1wQrWh_SB24buMzVjSgEQ8lS0; SERVERID=9b67fc541b8e0371a3b1071b0d3662f0|1696573387|1696573157"
}
# resp = requests.get("https://www.thesupermade.com/products/retro-style-quilted-racing-jacket-1",headers=headers)
# # print(resp.text)
# soup = BeautifulSoup(resp.text, 'lxml')
# table = soup.find_all('table')[0]
# trs = table.find_all('tr')
# for tr in trs:
#     cols = tr.find_all('td')
#     # 遍历每一列，并打印出该列的文本内容
#     for col in cols:
#         print(col.text)
# fake = Faker()
#
# print(fake.chrome())

sess = requests.Session()
resp = sess.get("https://opstores.com/api/opstores/revenue/queryRevenue?page=1&pageSize=50&mode=&businessUnitIdList=&groupIdList=&currency=1&startDate=20231005&endDate=20231005&t=1696573655000",headers=headers)

print(resp.text)