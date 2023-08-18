# -*- coding:utf-8 -*-
# @FileName  :processDemo.py
# @Time      :2023/7/13 10:10
# @Author    :dzz
# @Function  :
import multiprocessing  # 引入多进程模块
import os
import urllib.request
import time


def get_web(url):
    time.sleep(10)
    user_agent = r"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36"
    headers = {
        "User-Agent": user_agent,
        "Content-Type": "application/json;charset=UTF-8"
    }
    req = urllib.request.Request(url, headers=headers)
    resp = urllib.request.urlopen(req)
    print(resp.read().decode()[:50])


class myProcess(multiprocessing.Process):
    def __init__(self, name,url):
        super().__init__()
        self.name = name
        self.url = url

    def run(self):
        print("我是进程{}".format(self.name), "当前进程ID{}".format(os.getpid()), "我的父进程{}".format(os.getppid()))
        user_agent = r"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36"
        headers = {
            "User-Agent": user_agent,
            "Content-Type": "application/json;charset=UTF-8"
        }
        req = urllib.request.Request(self.url, headers=headers)
        resp = urllib.request.urlopen(req)
        print(resp.read().decode()[:50],self.url)


if __name__ == "__main__":
    # p1 = multiprocessing.Process(target=get_web, args=('https://www.hao123.com/',))
    # p2 = multiprocessing.Process(target=get_web, args=('https://www.baidu.com/',))
    # p1.start()
    # p1.join()
    # p2.start()
    # p2.join()
    #
    # print("进程执行完成！！！")
    print("当前主进程的ID为{}".format(os.getpid()))
    p1 = myProcess('子进程1', 'https://www.hao123.com/')
    p2 = myProcess('子进程2', 'https://www.baidu.com/')

    p1.start()
    p1.join()
    p2.start()
    p2.join()


    print("进程执行完成！！！")
