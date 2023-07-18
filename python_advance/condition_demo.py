# -*- coding:utf-8 -*-
# @FileName  :condition_demo.py
# @Time      :2023/7/18 9:22
# @Author    :dzz
# @Function  :
import threading
import time

# 创建一个condition对象
cond = threading.Condition()


# cond.acquire()
# cond.notify()

class KongBaiGe(threading.Thread):
    def __init__(self, cond, name):
        super().__init__(name=name)
        self.cond = cond

    def run(self):
        self.cond.acquire()  # 获取锁

        print(self.getName() + ":一支穿云箭")  # 空白哥说第一句话
        self.cond.notify()  # 唤醒其他wait状态的线程(通知西米哥说话)
        self.cond.wait()  # 进入wait线程挂起状态，等待notify通知
        print(self.getName() + ":山无棱天地合乃敢与君绝")  # 空白哥说第一句话
        self.cond.notify()  # 唤醒其他wait状态的线程(通知西米哥说话)
        self.cond.wait()  # 进入wait线程挂起状态，等待notify通知
        print(self.getName() + ":微微")  # 空白哥说第三句句话
        self.cond.notify()  # 唤醒其他wait状态的线程(通知西米哥说话)
        self.cond.wait()  # 进入wait线程挂起状态，等待notify通知

        print(self.getName() + ":借点钱")  # 空白哥说的最后一句话
        self.cond.notify()  # 唤醒其他wait状态的线程(通知西米哥说话)
        self.cond.release()  # 释放锁


class XimiGe(threading.Thread):

    def __init__(self, cond, name):
        super().__init__(name=name)
        self.cond = cond

    def run(self):
        self.cond.acquire()
        self.cond.wait()  # 先等待 等待空白哥先说

        print(self.getName() + ": 千军万马来相见")
        self.cond.notify()
        self.cond.wait()
        print(self.getName() + ": 海可枯 石可烂，激情永不烂")
        self.cond.notify()
        self.cond.wait()
        print(self.getName() + ": 尔康")
        self.cond.notify()
        self.cond.wait()
        print(self.getName() + ": 滚")
        self.cond.release()
        # self.cond.notify()
        # self.cond.wait()


if __name__ == "__main__":
    kongbaige = KongBaiGe(cond, '空白哥')
    ximige = XimiGe(cond, '西米哥')

    # time.sleep(3)
    # kongbaige.join()
    ximige.start()
    kongbaige.start()  # 因为空白哥启动后 发出notify指令，而西米哥还未启动，导致notify指令无法接收，西米哥会一直处于等待状态
    # ximige.join()
