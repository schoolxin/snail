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
# 条件过滤
print(arr > 30)
print(arr[arr > 30])

# 加减乘除log操作(全部元素的操作)
print(arr + 100)
print(t + 100)
print(np.log(t))
# 去重
s1 = pd.Series([1, 2, 3, 4, 5, 6, 5, 3, 1])

s2 = s1.unique()
print("去重=============")
# print(s1)
print(type(s2))  # 变成了ndarray
# print(s1)
print("统计每个元素出现的次数")
print(s1.value_counts())

print("判断Series里面的元素是否在另外一个序列里面")

condition = [5, 6]
print(s1.isin(condition).values)  # 判断那些符合条件
print(type(s1.isin(condition).values))  # 判断那些符合条件  s1.isin(condition) 不加values 返回的是Series 类型 加上values 返回的类型是ndarray
print(s1[s1.isin(condition).values])

print("空值判断")
s1_1 = pd.Series([1, 2, 3, np.nan])  # np.nan 表示空值
print(s1_1.isna())
print(s1_1.isnull())

print("通过字典来创建Series")
dic1 = {'name': "zhangs", 'age': 100}
s1_2 = pd.Series(dic1)
# print(s1_2)

dic2 = {'name': "zhangs", 'age': 200, 'height': 100}

s2_2 = pd.Series(dic2)

print(s1_2 + s2_2)
# print(s1_2 * s2_2)
