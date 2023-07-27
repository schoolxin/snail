def walk():
    print("二哈走走")


class Dog:

    def __init__(self, name):
        self.name = name

    def eat(self):
        print("{}在吃东西".format(self.name))

    def sleep(self):
        print("{}正在睡觉".format(self.name))


# print(dir(Dog))
# print(Dog.__dict__)
#
# d = Dog("二哈")
# print("___________________")
# print(dir(d))
# print(d.__dict__)

# chioce = input("输入要执行的方法名称")
d = Dog("二哈")
# print(hasattr(d, chioce))

# if hasattr(d, chioce):
#     try:
#         func = getattr(d, chioce)  # getattr 返回方法的引用
#         func()
#     except TypeError as e:
#         print(func)
# else:
#     print("输入的方法不存在，请重新输入")


chioce = input("请输入要输入的方法名")

setattr(d, chioce, walk)  # 通过choice指向实际要绑定的函数
getattr(d, chioce)()

delattr(d,chioce) # 删除对象的方法或属性
