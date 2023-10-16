# -*- coding:utf-8 -*-
# @FileName  :Pandas_dataFrame.py
# @Time      :2023/10/16 10:41
# @Author    :dzz
# @Function  :
import numpy as np
import pandas
import pandas as pd

if __name__ == "__main__":
    run_code = 0

df1 = pandas.DataFrame([['Frank', 'M', 29], ['Marry', 'F', 29], ['Jerry', 'M', 14]])
print(df1)
df1.columns = ['Name', 'Sex', 'Age']
print(df1)

print("添加列标签")
df2 = pandas.DataFrame([['Frank', 'M', 29], ['Marry', 'F', 29], ['Jerry', 'M', 14]], columns=['Names', 'Sex', 'Age'])
print(df2)

print("给DataFrame中添加数据1:用字典添加")
d = {"Names": "kevin", "Sex": 'M', "Age": 100}
df2_new = df2.append(d, ignore_index=True)  # ignore_index 必须要加 否则就会失败
print(df2_new)
print("给DataFrame中添加数据2:loc")

df2.loc[3] = ['Lily', 'M', 23]
print(df2)

print("在DataFrame指定位置插入一列数据")

df2.insert(3, 'addr', ['成都', '北京', '上海', '西安'])
print("修改列名")
df2.insert(3, 'add', df2.pop('addr'))
print(df2)

print("删除指定的列")
df2_new1 = df2.drop(labels='add', axis=1,
                    inplace=False)  # 列名   axis = 1表示删除的是列   axis = 0 表示删除一行, inplace 表示在源表上修改还是在返回的复制表上修改 默认是False
print(df2_new1)

print("直接增加一列")

df2['emp'] = True
print(df2)

print("直接删除一列")
del df2['emp']
print(df2)

print("删除指定的行")
df3 = pandas.DataFrame(
    [['Frank', 'M', 29], ['Marry', 'F', 29], ['Jerry', 'M', 14], ['Marry2', 'F', 30], ['Marry3', 'F', 30],
     ['Marry4', 'F', 30]], columns=['Names', 'Sex', 'Age'])

# df3.drop(2,axis=0,inplace=True)
# print(df3)

print("修改一行数据")
# df3.loc[1] = ['Marry1','F1',100]
# print(df3)

print("查询操作")

print(df3.head())  # 默认 只显示前5行
print(df3.tail())  # 默认是 后5条
# print(df3.info()) # dataframe的概要信息
print(df3.describe())  # 可以对DataFrame中的数值型数据进行统计计算
print("查看指定区间的数据")
print(df3.iloc[1:4])  # 查看指定区间的数据
print(df3.iloc[[1, 3, 5]])  # 查看指定区间的数据
print("按列查询")
print(df3['Names'])
print(df3[['Names', 'Age']])  # 按照多列
print("指定行和列")
print(df3.loc[[1, 3, 5], ['Names', 'Age']])

print("按单条件筛选")
t = (df3['Sex'] == 'M')
print(t)
print("多条件筛选")
print(df3)
print((df3['Sex'] == 'M') & (df3['Age'] < 30))  # 与
print((df3['Sex'] == 'M') | (df3['Age'] < 30))  # 或

print("自定义行的index")

df4 = pandas.DataFrame(
    [['Frank', 'M', 29], ['Marry', 'F', 29], ['Jerry', 'M', 14], ['Marry2', 'F', 30], ['Marry3', 'F', 30],
     ['Marry4', 'F', 30]], columns=['Names', 'Sex', 'Age'])
df4['user_id'] = range(100,106) # 序列的大小要跟现有的df的行数要一致
print(df4)
df4.set_index('user_id',inplace=True)
print(df4.loc[[100,103]])
'''
iloc 是通过行的真实位置坐标来进行定位 坐标是从0开始
loc 是通过标签进行定位(自定义的index)
'''