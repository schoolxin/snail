# class stu:
#
#     # def __init__(self):  # 负责初始化类的实例，实例是有__new__方法传递过来，也就是这里的self
#     #     print("init方法")
#
#     # cls 表示的是类
#     def __new__(cls, *args, **kwargs):  # 负责创建类的实例
#         print("new方法",args)
#         return object.__new__(cls) # 只有返回了实例 __init__ 方法才会被调用
#
#     def show(self, *args):
#         print(args)
#
#
# if __name__ == '__main__':
#     al = [i for i in range(10)]
#     st = stu(11,11)
#     st.show(al)

# class newInt(int):
#
#     def __new__(cls, value):
#         print("new 方法被调用")
#         return int.__new__(cls, abs(value))
#
#
# a = newInt(-4.55)
#
# print(a)


# 实现单例模式 new方法的用途

class stu:

    def __init__(self, name, age):  # 负责初始化类的实例，实例是有__new__方法传递过来，也就是这里的self
        print("我是{}".format(name))
        self.__age = age
        self.name = name

    # cls 表示的是类
    # 类属性
    __isinstancess = False  # 保存我们已经创建好的实例

    def __new__(cls, *args, **kwargs):  # 负责创建类的实例
        if not cls.__isinstancess:  # 没有创建过任何实例
            cls.__isinstancess = object.__new__(cls)
        return cls.__isinstancess  # 如果有实例，则直接返回实例


s = stu('www', 90)
print(dir(s))
print(dir(stu)) # 不包含实例属性
print(s.__dir__())
print(s._stu__age)
