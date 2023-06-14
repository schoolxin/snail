# -*- coding:utf-8 -*-
# @FileName  :listDemo.py
# @Time      :2023/6/9 9:34
# @Author    :dzz
# @Function  :
list1 = [1, 2, 3, 4, 5, 4]
for i in list1:
    print(i)
# print(max(list1))
astr = "python"
print(list(astr))
print(astr)
list1.append([100, 299, 99])
list1.extend([[100, 299, 99]])
print(list1)
# print(list1.count(1))
# print(list1.index(1000))

# print(list1.pop())
# print(list1.remove(100))
print(list1)

al = [1, 2, 3, 4, 5, 4, '34']
print(al)
al.sort(key=lambda x: int(x))
print(al)
print(al.reverse())
print(al)
al.clear()  # 清空列表元素
# 列表复制
a = [1, 2, 3]
b = a  # 浅拷贝 只是拷贝引用
c = a.copy()  # 深拷贝 可以得到两个独立的列表
d = a[:]
a.append(4)

print(c)
print(a)
print(b)
print(d)
print("++++++++可变与不可变+++++++")

a3 = 1
print(id(a3))
a3 = 2
print(id(a3))

b1 = "hello"
print(id(b1))
b1 = "hello1"
print(id(b1))

c1 = [2, 23, 4]
print(id(c1))
c1[0] = 100
c1.append(1000)
print(id(c1))

d1 = (1, 2, 3, c1)
print(id(d1))

s1 = {1, 2, 3, 4, 5}

print(id(s1))
s1.add(200)
print(id(s1))
print("字典")
s2 = {"a": 11, "b": 2}
print(id(s2))
s2.update({"c": 22})
print(id(s2))
