# -*- coding:utf-8 -*-
# @FileName  :QueueDemo.py
# @Time      :2023/7/13 9:19
# @Author    :dzz
# @Function  :
import threading
from queue import Queue
import time


def producer(q):
    kind = ('猪肉', '牛肉', '白菜')
    for i in range(3):
        print(threading.current_thread().name+":开始包子生产")
        time.sleep(1)
        q.put(kind[i % 3])
        print(threading.current_thread().name+":包子完成生产")


def consumer(q):
    while True:
        print(threading.current_thread().name+":准备消费包子")
        time.sleep(1)
        t = q.get()  # 每次从队列中获取一个 队列长度都会减1
        print("消费的包子为{}".format(t))


if __name__ == "__main__":
    q = Queue(maxsize=1)  # 队列中最多只能有一个包子
    threading.Thread(target=producer, args=(q,)).start()
    threading.Thread(target=producer, args=(q,)).start()

    # 启动消费者线程
    threading.Thread(target=consumer, args=(q,)).start()
