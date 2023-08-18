# -*- coding:utf-8 -*-
# @FileName  :threademo01.py
# @Time      :2023/7/11 11:26
# @Author    :dzz
# @Function  :
import threading
import urllib.request
import requests


def get_web(url):
    user_agent = r"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36"
    headers = {
        "User-Agent": user_agent,
        "Content-Type": "application/json;charset=UTF-8"
    }
    req = urllib.request.Request(url, headers=headers)
    resp = urllib.request.urlopen(req)
    print(resp.read().decode()[:50])

class MyThread(threading.Thread):
    def __init__(self,name,url):
        super().__init__() #调用父类初始化方法 保证父类初始化成功
        self.name = name
        self.url = url
    def run(self): # 重写父类的run方法，定义在新的线程类中要完成的任务
        print("我是线程{}".format(self.name))
        user_agent = r"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36"
        headers = {
            "User-Agent": user_agent,
            "Content-Type": "application/json;charset=UTF-8"
        }
        req = urllib.request.Request(self.url, headers=headers)
        resp = urllib.request.urlopen(req)
        print(resp.read().decode()[:50])


if __name__ == "__main__":
    # t1 = threading.Thread(target=get_web, args=("https://www.hao123.com/",))
    # t2 = threading.Thread(target=get_web, args=("https://www.baidu.com/",))
    # t1.start()
    # t1.join()
    # t2.start()

    # t2.join()
    # print("程序运行结束")  # 主线程
    t1 = MyThread('线程1',"https://www.hao123.com/")
    t2 = MyThread('线程2',"https://www.baidu.com/")
    t1.start()
    t1.join()
    t2.start()
    t2.join()
