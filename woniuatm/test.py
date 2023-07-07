# -*- coding:utf-8 -*-
# @FileName  :test.py
# @Time      :2023/7/7 9:10
# @Author    :dzz
# @Function  :
usename=["2"]
def login():
    uname = input("请输入用户名")
    print("外",id(uname))
    while True:

        for i in range(10):
            print(i)
            if i ==8:
                break

login()

l1 = [['a','2'],['b','3'],'a']
if 'a' in l1:
    print("exists")