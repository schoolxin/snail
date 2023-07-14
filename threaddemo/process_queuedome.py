# -*- coding:utf-8 -*-
# @FileName  :process_queuedome.py
# @Time      :2023/7/14 9:07
# @Author    :dzz
# @Function  :

import multiprocessing
import time


def producer(q):
    kind = ('猪肉', '牛肉', '白菜')
    for i in range(3):
        print(multiprocessing.current_process().name + ":开始包子生产")
        time.sleep(1)
        q.put(kind[i % 3])
        print(multiprocessing.current_process().name + ":包子完成生产")


def consumer(q):
    while True:
        print(multiprocessing.current_process().name + ":准备消费包子")
        time.sleep(1)
        t = q.get()  # 每次从队列中获取一个 队列长度都会减1
        print("消费的包子为{}".format(t))


if __name__ == '__main__':
    q = multiprocessing.Queue(maxsize=1)  # 创建多进程队列
    p1 = multiprocessing.Process(target=producer,args=(q,))
    p2 = multiprocessing.Process(target=producer,args=(q,))
    p1.start()
    p2.start()

    c = multiprocessing.Process(target=consumer,args=(q,))

    c.start()
