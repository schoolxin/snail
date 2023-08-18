# -*- coding:utf-8 -*-
# @FileName  :class_demo.py
# @Time      :2023/6/27 9:29
# @Author    :dzz
# @Function  :

class Student(object):

    # 定义类属性
    a = 0
    # 定义属性 类的魔术方法，对象实例化时自动调用 其中的self  表示调用这个方法的实例
    def __init__(self, name, age, stuno):
        self.names = name
        self.ages = age
        self.stunos = stuno



    # def __init__(self, name, age):
    #     self.names = name
    #     self.ages = age
    #
    # def __init__(self):
    #     print("无参初始化")

    def study(self):
        print("我正在学习2")
        self.classmethodDemo1()
        self.staticDemo()
    @classmethod
    def classmethodDemo1(cls):
        print("这是一个类方法",cls.a)

    @staticmethod
    def staticDemo():
        print("这是一个静态方法",Student.a)

class woniuStudent(Student):
    def __init__(self,name, age, stuno,adress):
        # super().__init__(name,age,stuno)
        Student.__init__(self,name,age,stuno)
        self.address = adress
        pass
    def study(self):
        print("在子类中study方法被调用")
    # pass

if __name__ == "__main__":
    # stus = Student('1',2,'222')
    # stus.study()
    # Student.classmethodDemo1()
    # stus.classmethodDemo1()
    # # print(stus.stunos)
    # Student.staticDemo()
    # stus.staticDemo()
    ws = woniuStudent('1',22,'223','beijig')
    ws.classmethodDemo1()
    print(ws.address)
    print(ws.names)
    ws.study()