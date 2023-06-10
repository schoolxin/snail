# -*- coding:utf-8 -*-
# @FileName  :listDemo.py
# @Time      :2023/6/9 9:34
# @Author    :dzz
# @Function  :
list1 = [1,2,3,4,5]
for i in list1:
    print(i)
# print(max(list1))
astr = "python"
print(list(astr))
print(astr)
list1.append([100,299,99])
list1.extend([[100,299,99]])
print(list1)
# print(list1.count(1))
print(list1.index(1000))