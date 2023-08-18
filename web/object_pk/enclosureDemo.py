# -*- coding:utf-8 -*-
# @FileName  :enclosureDemo.py
# @Time      :2023/6/29 9:50
# @Author    :dzz
# @Function  :


class Demo:
    def __init__(self):
        self.__x = 10  # 隐藏属性
        self.y = 20  # 普通属性

    def printHello(self):
        print("ho")

    def getx(self):  # 对外获取属性
        return self.__x

    def setx(self, x):  # 对外的设置属性
        self.__x = x
    def __hidefunc(self):
        print("我是隐藏方法")


if __name__ == "__main__":
    # print(dir(Demo()))
    d1 = Demo()
    d1.y
    # print(d1.__x)
    d1._Demo__x
