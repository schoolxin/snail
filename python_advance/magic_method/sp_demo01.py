# -*- coding:utf-8 -*-
# @FileName  :sp_demo01.py
# @Time      :2023/7/24 9:47
# @Author    :dzz
# @Function  :
class ob1:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __repr__(self):
        return "姓名{nm}和年龄{ag}".format(nm=self.name, ag=self.age)


if __name__ == "__main__":
    o1 = ob1('zhan', 1000)
    print(o1)
    # print(o1.__repr__())
