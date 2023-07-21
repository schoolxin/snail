# -*- coding:utf-8 -*-
# @FileName  :semaphore_demo.py
# @Time      :2023/7/20 9:26
# @Author    :dzz
# @Function  :
import threading
import time



class htmlSpider(threading.Thread):
    # 获取抓取到的url地址的内容
    def __init__(self, url, sem):
        super().__init__()
        self.url = url
        self.sem = sem

    def run(self):
        time.sleep(10)  # 模拟网络等待
        print('获取网页内容成功{}'.format(self.url))
        self.sem.release()  # 爬取完成之后释放锁


class urlProducer(threading.Thread):
    # 负责抓取页面的url地址
    def __init__(self, sem):
        super(urlProducer, self).__init__()
        self.sem = sem

    def run(self):
        for i in range(20):
            self.sem.acquire()  # 先获取锁再执行
            html_thread = htmlSpider('http://www.baidu.com{}'.format(i),self.sem)
            html_thread.start()


if __name__ == "__main__":
    sem = threading.Semaphore(value=3)  # 一次只有4个线程可以获取到锁
    url_Producer = urlProducer(sem)
    url_Producer.start()
