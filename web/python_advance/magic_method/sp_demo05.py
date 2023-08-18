# -*- coding:utf-8 -*-
# @FileName  :sp_demo05.py
# @Time      :2023/7/27 9:25
# @Author    :dzz
# @Function  :
class person:

    def __init__(self, name):
        self.name = name

    # def __getattribute__(self, item):
    #     # try:
    #     print("__getattribute__ 方法被调用", item)
    #     return super().__getattribute__(item)
    #
    # # except AttributeError as e:
    # #     # print(e)
    # #     print("访问的了未被定义的属性，请检查")
    # # print("调用了{}属性".format(item))
    # # return super(person, self).__getattribute__(item)
    # def __getattr__(self, item):
    #     # 当__getattribute__ 没有处理AttributeError时候python会调用重写的__getattr__
    #     print("__getattr__ 方法被调用")
    #     print("访问的了未被定义的属性，请检查", item)

    def __setattr__(self, key, value):
        print("程序设置属性{}".format(key))
        if key == 'age' and value < 18:
            raise Exception("age的值必须大于18岁")

        else:
            self.__dict__[key] = value
            # super().__setattr__(key,value)
        # self.key = value # 这样调用会造成死循环 不停的调用__setattr__
    def __delattr__(self, item):
        print("__delattr__ 方法被调用 删除的属性为{}".format(item))


if __name__ == "__main__":
    p = person("a")

    del p.name
    del p.age
    # p.age = 19
    # print(p.name)  # 先会调用__getattribute__ 方法，如果在return的时候，发现属性不存在的时候才会调用__getattr__
    # print(p.age)
    # print(p.addr)
