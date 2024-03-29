# -*- coding:utf-8 -*-
# @FileName: Ip_proxypool_Coroutine.py
# @Time:2023/10/9 22:49
# @Author    :dengzz
'''
协程：
在同一线程中不同的子程序之间可以中断执行去执行其他子程序，并且在中断后回来后，可以从中断的地方继续执行，这种调度模式叫做协程
yield 实现协程，完成生产者和消费者模型
协程的优势：
1.没有多线程程序中上下文切换的开销，避免无意义的调度，提高性能，线程越多 协程的性能优势越明显
2.不需要多线程的锁机制，因为只有一个线程，也不存在同时写变量的冲突，在协程中控制共享资源不需要加锁，只需要状态就可以
3.方便切换控制流，简化编程模型
4.高并发+高扩展性+低成本
缺点：
无法利用多核资源，协程本质是一个单线程，协程一般要配合进程才能运行在多个cpu上，要充分利用资源，最好是使用多进程+协程
python3.4之后  asyncio.coroutine 和 yield from 后面必须跟iterable对象(可以是生成器也可以是迭代器)
python3.5之后，async/await 关键字  替换原则 将asyncio.coroutine 替换成async   yield from 替换成await
'''


def consumer():
    r = ''
    while True:
        n = yield r
        if not n:
            return
        print('[Consumer]消费者正在消费{}'.format(n))
        r = "200 ok"


def producer(c):
    # 激活生成器
    c.send(None)
    n = 0
    while n < 5:
        n = n + 1
        print("[Producer]生产者生产了{}".format(n))
        res = c.send(n)
        print('[Producer]消费者返回的消息{}'.format(res))
    c.close()


c = consumer()
# c1 = consumer()

producer(c)
# producer(c1)
