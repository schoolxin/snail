# -*- coding:utf-8 -*-
# @FileName: Pandas_Series1.py
# @Time:2023/10/15 22:45
# @Author    :dengzz
import pandas as pd

a = pd.Series([1, 3, 5, 7, 9], index=['a', 'b', 'c', 'd', 'e'])  # Series类型 默认的索引是从0开始，也可以自己定义索引

# print(a)
# print(a.index)
# print(a.values)
# print(a['c'])

print(a[['a', 'c']])

# 通过numpy的array对象生成一个series
import numpy as np

arr = np.array([33, 44, 55, 77, 22])
t = pd.Series(arr)

print(type(arr))
print(type(t))
