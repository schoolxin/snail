# -*- coding:utf-8 -*-
# @FileName  :event_demo.py
# @Time      :2023/7/18 9:02
# @Author    :dzz
# @Function  :

import threading
import time


# event = threading.Event()
# event.clear()  # 重置代码中event对象，使得所有该event事件都处于待命的状态
# event.wait()  # 阻塞线程，等待event 指令
# event.set()  # 发送event指令，使得所有设置该event事件的线程执行
class mythread(threading.Thread):
    def __init__(self, event, name):
        super().__init__()
        self.event = event
        self.name = name

    def run(self):
        print("线程{}初始化完成，随时准备启动".format(self.name))
        # 设置线程等待
        self.event.wait()
        print("{}开始执行".format(self.name))


if __name__ == "__main__":
    event = threading.Event()
    threads = []
    # 创建10个自定义线程对象
    [threads.append(mythread(event, i)) for i in range(11)]
    event.clear()
    [t.start() for t in threads]
    time.sleep(5)
    event.set()
    [t.join() for t in threads]
