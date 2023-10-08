'''
IP 代理池技术点
反射

'''


class DemoClass:
    def __init__(self):
        self.name = "zhangsan"

    def test1(self):
        print("this is test1")

    def test2(self):
        print("hello is test2")

    def demo(self):
        print("a demo")


funct_list = []
for k, v in DemoClass.__dict__.items():
    if 'test' in k:
        funct_list.append(k)

dc = DemoClass()

for func in funct_list:
    eval(f'dc.{func}()')
