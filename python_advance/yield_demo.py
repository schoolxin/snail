# -*- coding:utf-8 -*-
# @FileName  :yield_demo.py
# @Time      :2023/7/22 9:12
# @Author    :dzz
# @Function  :
def demo():
    print("hello")
    t = yield 5  # 这里不是将5 赋值给t yield 右边是返回给调用方的，左边的t是调用方每次通过send方法调用时传递的数据
    print(t)
    print("world")


if __name__ == "__main__":
    c = demo()  # 生成器函数 这样调用的时候不会直接执行 只有在迭代的时候 才开始运行
    # print(next(c)) # 预激活生成器
    print(c.send(None))  # 预激活生成器
    # next(c)
    c.send('test')  # send 方法调用生成器 并把字符串传递到生成器内部  只有激活生成器后才能传递参数进去
