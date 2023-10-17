# -*- coding:utf-8 -*-
# @FileName: Pandas_dataFrame02.py
# @Time:2023/10/16 23:00
# @Author    :dengzz
import numpy as np
import pandas
import pandas as pd

# 在数据分析中，我们一般使用numpy里面的nan来代表缺失值

df = pd.DataFrame([['jack', 'M', 30],
                   ['Bruce', np.nan, 22],
                   ['Lucy', 'F', 30],
                   ['Tom', 'M', 40],
                   ['Lisa', 'F', 50]],
                  columns=['Name', 'Sex', 'Age'],
                  index=['100', '200', '300', '400', '500']
                  )

print(df.isnull().values.any())  # 检测整个df中是否缺失值
print(df.isnull().any())  # 检测整个df中哪些列中有缺失值
print("统计每个字段具体有多少个缺失值")
print(df.isnull().sum())
print("统计所有缺失值的个数")
print(df.isnull().sum().sum())

print("对具体的列检查缺失值")
print(df['Sex'].isnull())
print(df['Sex'].notnull())
print("检查具体的列有没有缺失值")

print(df['Name'].isnull().values.any())
print("具体的列有多少缺失值")
print(df['Age'].isnull().sum())

print("缺失值的处理")
print("1，直接舍弃缺失值，一般用于缺失值的数量占总量比例比较低的时候可以舍弃")
# print(df.dropna())
# print(df.dropna(how='all'))  # 舍弃一行全部都是缺失值的数据
df.loc['600'] = ['Jacks', 'M', np.nan]
# print(df)
# print(df.dropna(thresh=2))  # 舍弃一行有两个缺失值的数据
df['emp'] = np.nan
# print(df)
# print(df.dropna(axis=1,how='all',inplace=True))
# print(df)
print("2，使用平均数 中位数 众数等描述性的统计值来填补这个缺失值")
# print(df.fillna(0))
# print("前后")
# print(df)
# print(df['Age'].fillna(df['Age'].mean())) # 用指定列的平均值填补缺失值
# print("前后2")
# print(df)
df.groupby('Sex')['Age'].transform('mean')  # 根据Sex分组求 每个Sex的平均值
# print(df.groupby('Sex')['Age'].transform('mean'))
# print(df['Age'].fillna(df.groupby('Sex')['Age'].transform('mean')))
# print(df.fillna(method='pad'))  # 往下填充
# print(df)
print("3，使用内插法补全缺失值，比如字段呈线性规律  1,3,,7,9")
df2 = pd.DataFrame([[1, 870], [2, 930], [np.nan, np.nan], [4, 950], [5, 1030]])
df2.columns = ['time', 'value']
print(df2.interpolate())
print(df2)