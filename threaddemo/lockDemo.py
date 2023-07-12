# -*- coding:utf-8 -*-
# @FileName  :lockDemo.py
# @Time      :2023/7/12 9:29
# @Author    :dzz
# @Function  :
import threading

money = 0
lock = threading.Lock() # 锁对象

def deposit():
    global money
    for i in range(1000000):
        # 操作共享变量时 需要先锁
        lock.acquire() # 获取锁
        money += 1  # 4个步骤，如果这四个步骤中 整好超过100个字节 如果整好被操作了一半，另外一个线程继续对共享变量进行操作 这个时候就会造成冲突



def withdraw():
    global money
    for i in range(1000000):
        money -= 1


if __name__ == "__main__":
    # run_code = 0
    t1 = threading.Thread(target=deposit)
    t2 = threading.Thread(target=withdraw)
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    print(money)
