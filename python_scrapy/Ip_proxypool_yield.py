# -*- coding:utf-8 -*-
# @FileName: Ip_proxypool_yield.py
# @Time:2023/10/8 16:17
# @Author    :dengzz
'''
yield

可迭代对象和迭代器 生成器
可迭代对象：指实现了__iter__方法的对象，由于实现了__iter__方法，所以可直接用于for循环中，比如常见的dic  list   string都是可迭代对象
迭代器：指任何实现了__iter__ 和__next__()方法的对象(两个方法都必须实现，缺一不可)，其中__iter__返回迭代器本身  __next__()方法返回容器中的下一个值，
如果没有更多的元素则抛出stopIteration异常，有迭代器可以得出一个结论 迭代器肯定是可迭代对象  可迭代对象不一定是迭代器
迭代器本身其实是定义的一种规则，它不会事先将所有的对象生成(懒加载)，而可迭代对象通常是要把所有的元素生成出来一般有len()方法

生成器：是一种特殊的迭代器，我们只需要在函数体中定义一个yield关键字就可以把当前方法变成一个生成器方法 特点：一定是迭代器(反之不成立) 任何的生成器都是以懒加载的方式生成值
        包含一个yield关键字：这个yield关键字有两个作用：1.每次遇到yield关键字后，该方法会立马返回相应的结果  2.会保留函数当前的运行状态，等待下一次调用  下一次调用时将从
        上一次返回的yield关键处开始执行后面的语句；这意味着程序的控制权的转移是临时和自愿的，我们的函数将来还是要回收控制权， return 意味着彻底交出控制权并运行结束，下一次调用固定从函数第一行开始执行
        有一个内建send 方法，可以使用这个方法给yield语句传递参数，并且send()方法跟next()方法比较类似，都是让函数体向下继续运行，直到遇到一个yield语句挂起
        send(msg) 方法会给生成器发送变量msg 并作为yield表达式的返回值赋值给其前面的变量
'''
from itertools import count

counter = count(start=3)
for i in range(1):
    print(next(counter))

a = [1, 2, 3, 4, 6]
# print(len(a))


## 生成器

def h():
    print("hello")
    yield 5
    print("jack")


# c = h()

# next(c)


def gen():
    value = 0
    while True:
        receive = yield value
        if receive == 'e':
            break
        value = 'got:%s' % receive

g = gen()
# send 之前需要先激活生成器
print(g.send(None)) # 激活

print(g.send("hello"))
# print(next(g))
# print(next(g))
# print(next(g))


