# -*- coding:utf-8 -*-
# @FileName  :tupleDemo.py
# @Time      :2023/6/15 9:24
# @Author    :dzz
# @Function  :


a1 = (1, 2, 3, 4, 5, 6)
print(a1[1:3])

c = [1, 2, 3, 4, 5]

ct = tuple(c)
ct = list(ct)
print(ct.pop(3))
print(ct)
a = "hello"
a = list(a)
print(a)

st1 = {1, 2, 4, 5, 6, 2, 4, (1, 4, 5, 6, 6)}
print(st1)
st1.remove(1)
print(st1.pop())
print(st1)
print(len(st1))
st1.clear()

print(st1)

s1 = "hello"
t = set(s1)
print(t)
print('h' in t)

print("集合运算")
ss1 = {1, 2, 3}
ss2 = {3, 4, 5, 6, 2}
print("并集", ss1 | ss2)
print("交集", ss1 & ss2)
print("差集", ss1 - ss2)  # 在p中的元素 不能再q中
print("对称差集", ss1 ^ ss2)  # 剔除掉在两个集合中都有的元素然后并起来
