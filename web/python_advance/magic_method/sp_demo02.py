import time


class ob2:

    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.f = open('demo.txt')

    def __repr__(self):
        return "name:{}".format(self.name)

    def __del__(self):
        print("对象销毁")
        self.f.close()


if __name__ == '__main__':
    ob = ob2('lishi', 100)
    a = ob
    # del a
    del ob
    # del ob # 手动销毁对象
    # print(ob)
    print("程序在执行完成后自动销毁对象")
