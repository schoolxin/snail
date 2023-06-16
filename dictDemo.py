# -*- coding:utf-8 -*-
# @FileName  :dictDemo.py
# @Time      :2023/6/16 9:14
# @Author    :dzz
# @Function  :


dic1 = {"name": "lisi", "age": 200, "name": "lisi2"}

print(dic1)
print(dic1.get("name"))
print(dic1["name"])
dic1['name'] = "woniu"
dic1['height'] = 186
print(dic1)

# del dic1['name']
print(dic1)
print(dic1.pop('name'))
print(dic1.popitem())
