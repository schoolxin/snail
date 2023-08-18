# -*- coding:utf-8 -*-
# @FileName  :sp_demo04.py
# @Time      :2023/7/26 9:29
# @Author    :dzz
# @Function  :

class person:
    # 类属性
    has_body = True

    def __init__(self, name, age):
        self.name = name
        self.__age = age


    def say_hello(self):
        print("----")


if __name__ == "__main__":
    p1 = person('22', 22)
    # print(p1.__dict__)  # 作用于对象时，只打印该对象拥有的所有属性和属性值，包含私有属性
    # print(person.__dict__) # 作用于类时，只打印共享的类属性和方法

    p1.height = 1000
    print(p1.height)
    p1.__dict__['height2'] = 100
    print(p1.__dict__)

    p2 = person('22', 22)

    print(p2.__dict__)
    print(dir(person))
