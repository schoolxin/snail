# -*- coding:utf-8 -*-
# @FileName  :listDemo.py
# @Time      :2023/6/9 9:34
# @Author    :dzz
# @Function  :
list1 = [1,2,3,4,5,4]
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
# print(list1.index(1000))

# print(list1.pop())
# print(list1.remove(100))
print(list1)

al=[1,2,3,4,5,4,'34']
print(al)
al.sort(key=lambda x:int(x))
print(al)
print(al.reverse())
print(al)
al.clear() # 清空列表元素
# 列表复制
a = [1,2,3]
b = a # 浅拷贝 只是拷贝引用
c = a.copy() # 深拷贝 可以得到两个独立的列表
d = a[:]
a.append(4)

print(c)
print(a)
print(b)
print(d)