# -*- coding:utf-8 -*-
# @FileName  :test.py
# @Time      :2023/7/7 9:10
# @Author    :dzz
# @Function  :

flags = True
def login():
    global flags
    flags = False
login()


print(flags)