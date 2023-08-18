# 通过yield实现协程 （消费者-生产者）


def  consumer():
    r = ''
    while True:
        n = yield r
        if not n:
            return
        print('消费者正在消费{}'.format(n))
        r = '200 ok'

def producer(c):

    c.send(None) # 预激活生成器

    n = 0
    while n < 5:
        n = n + 1
        print("生产者正在生产{}".format(n))
        r = c.send(n)
        print("生产者消费者返回值{}".format(r))


c = consumer()

producer(c)