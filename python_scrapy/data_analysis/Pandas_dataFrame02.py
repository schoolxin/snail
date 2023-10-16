# -*- coding:utf-8 -*-
# @FileName: Pandas_dataFrame02.py
# @Time:2023/10/16 23:00
# @Author    :dengzz
import numpy as np
import pandas
import pandas as pd

# 在数据分析中，我们一般使用numpy里面的nan来代表缺失值

df = pd.DataFrame([['jack', 'M', np.nan],
                   ['Bruce', np.nan, 22],
                   ['Lucy', 'F', 22],
                   ['Tom', 'M', 40],
                   ['Lisa', 'F', 30]],
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