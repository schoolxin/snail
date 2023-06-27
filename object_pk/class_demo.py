# -*- coding:utf-8 -*-
# @FileName  :class_demo.py
# @Time      :2023/6/27 9:29
# @Author    :dzz
# @Function  :

class Student(object):
    # 定义属性 类的魔术方法，对象实例化时自动调用 其中的self  表示调用这个方法的实例
    # def __init__(self, name, age, stuno):
    #     self.names = name
    #     self.ages = age
    #     self.stunos = stuno



    # def __init__(self, name, age):
    #     self.names = name
    #     self.ages = age
    #
    # def __init__(self):
    #     print("无参初始化")

    def study(self):
        print("我正在学习1")

    def study(self):
        print("我正在学习2")


if __name__ == "__main__":
    stus = Student()
    stus.study()
    # print(stus.stunos)