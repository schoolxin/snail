# -*- coding:utf-8 -*-
# @FileName  :dictDemo.py
# @Time      :2023/6/16 9:14
# @Author    :dzz
# @Function  :


dic1 = {"name": "lisi", "age": 200, "name": "lisi2"}

print(dic1)
print(dic1.get("name"))
print(dic1["name"])
dic1['name'] = "woniu"
dic1['height'] = 186
print(dic1)

# del dic1['name']
print(dic1)
# print(dic1.pop('name'))
# print(dic1.popitem())
print(len(dic1))

# 浅拷贝
dic2 = dic1
print(dic2)
dic2['name'] = "woniuniu"
print(dic1)
# 深拷贝
dic3 = dic1.copy()
dic3.update({"name": "蜗牛"})

print(dic3)
print(dic1)

alist = ['name', 'age', 'address']
alist2 = [1, 2, 3]
d4 = dict.fromkeys(alist, alist2)
d5 = dict(zip(alist, alist2))
print("d5", d5)
for item in d5.items():
    print(item)

print("setdefault")
print(d5.setdefault("name1", "jack"))
print(d5)
d5.update({"name": "eee", 'height': 100})
print(d5)
print(d5.pop('name'))
print(d5.pop('name5', 'not exists'))
print(d5.popitem())
print(d5)
print("循环删除字典中的元素")
while len(d5.keys())>0:
    print(d5.popitem())
