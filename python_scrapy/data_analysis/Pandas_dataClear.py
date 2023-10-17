# -*- coding:utf-8 -*-
# @FileName: Pandas_dataClear.py
# @Time:2023/10/17 22:45
# @Author    :dengzz
import pandas as pd
import numpy as np

df = pd.read_csv('./day4/house_data.csv', index_col=0)
del df['標題']
# print(df['物业费']=='暂无资料')
df.loc[df['物业费'] == '暂无资料', '物业费'] = np.nan # loc 也可以返回bool为真的下标数据  loc 可以指定行和列

# print(df.head())

df2 = pd.read_csv('./day4/house_data.csv', index_col=0,na_values='暂无资料')
pd.set_option('display.max_columns', None) # 显示所有列
pd.set_option('display.max_rows', None) # 显示所有行
pd.set_option('display.width', 1000)  # 设置1000列时才换行
pd.set_option('max_colwidth', 100)
del df2['標題']
print(df2.head())