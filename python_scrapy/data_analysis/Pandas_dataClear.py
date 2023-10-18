# -*- coding:utf-8 -*-
# @FileName: Pandas_dataClear.py
# @Time:2023/10/17 22:45
# @Author    :dengzz
import pandas as pd
import numpy as np

df = pd.read_csv('./day4/house_data.csv', index_col=0)
# del df['標題']
# print(df['物业费']=='暂无资料')
df.loc[df['物业费'] == '暂无资料', '物业费'] = np.nan  # loc 也可以返回bool为真的下标数据  loc 可以指定行和列

# print(df.head())

df2 = pd.read_csv('./day4/house_data.csv', index_col=0, na_values='暂无资料')
pd.set_option('display.max_columns', None)  # 显示所有列
pd.set_option('display.max_rows', None)  # 显示所有行
pd.set_option('display.width', 1000)  # 设置1000列时才换行
pd.set_option('max_colwidth', 100)

# del df2['標題'] # 删除标题列
# print(df2.head())
# print(df.columns)
# print(df.dtypes)
# print(df.describe())
# print(df.isnull().sum())  # 每一列的缺失值的数量
# del df2['参考月供']

df2 = df2.drop('参考月供', axis=1)  # 删除列

# print(df2.count())  # 每一列的非空行数
# print(df['产权性质'].isnull().sum()) # 指定列有多少个缺失值
# print(df2.head())

# print(df2['产权性质'].value_counts())  # 每个列中有多少种数据  并且每种数据的个数是多少

# print(df2[df2['产权性质'] == '个人产权']) # 列出产品性质为个人产权的数据
# print(df2[df2['建筑类别'].isnull()]) # 列出产建筑类别为缺失值的数据

# print(df2.dropna(axis=1, how="all").count())  # 删除所有列都缺失的行数据
df2 = df2.dropna(axis=1, how="all")
# print(df2.count())  # 删除所有列都缺失的行数据
df2['物业费'] = df2['物业费'].fillna(0)
#
# df2['總價'] = df2['總價'].fillna(0)
# print(df2['總價'].isnull().sum())
print((df2['總價'] / df2['建筑面积']).mean())  # 平均单价
avg_price = (df2['總價'] / df2['建筑面积']).mean()
df2['總價'] = df2['總價'].fillna(avg_price * df2['建筑面积'])
print(df2['總價'].isnull().sum())
print(df2.head(20))

df2.to_csv('house_final.csv')
