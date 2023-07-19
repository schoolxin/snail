# -*- coding:utf-8 -*-
# @FileName  :threadpool_demo.py
# @Time      :2023/7/19 9:18
# @Author    :dzz
# @Function  :
import time
from concurrent.futures import ThreadPoolExecutor

executor = ThreadPoolExecutor(max_workers=3)  # 创建了一个线程池


def get_html(times, param1, param2):
    time.sleep(times)  # 模拟网页请求
    print("获取网页信息{}".format(param1))
    return times


if __name__ == "__main__":
    # 通过submit方法提交执行的函数到线程池，submit 函数会立即返回，不会阻塞主线程
    task1 = executor.submit(get_html, 5, "task1", 3)  # 返回task1 就是任务的句柄
    task2 = executor.submit(get_html, 2, 'task2', 3)
    task3 = executor.submit(get_html, 1, 'task3', 3)
    task4 = executor.submit(get_html, 5, 'task4', 3)
    # time.sleep(5)
    print(task1.done())  # 检查任务是否完成，并返回结果
    print("task4取消", task4.cancel())  # 取消任务的执行 未被放入到线程池中的任务才能取消成功
    print("task1result",task1.result(timeout=6)) # 拿到任务执行的结果 该方法是一个阻塞方法
    print("task3result",task3.result()) # 拿到任务执行的结果 该方法是一个阻塞方法
    print("end")
