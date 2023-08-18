# def foo():
#     print("foo")
#     boo()
#
#
# def boo():
#     print("in boo")
#
# foo()


# def foo():
#     print("in foo")
#
# def gf(func):
#     print(func)
#     func()
#
# gf(foo)
import time


def foo():
    time.sleep(3)
    print("in foo")


def gf(func):
    start_time = time.time()  # 记录函数运行开始时间
    func()
    end_time = time.time()  # 记录结束时间
    print("运行fun的时间为{}".format(end_time - start_time))


gf(foo)
