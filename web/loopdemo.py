# -*- coding:utf-8 -*-
# @FileName  :loopdemo.py
# @Time      :2023/6/20 9:20
# @Author    :dzz
# @Function  :


for index, values in enumerate(('a', 'b', 'c', 'd')):
    if values=='c':
        break
    print("index===>", index, "values--->", values)
else:
    print("循环正常执行完")

