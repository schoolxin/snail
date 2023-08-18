# -*- coding:utf-8 -*-
# @FileName  :threadpool_demo.py
# @Time      :2023/7/19 9:18
# @Author    :dzz
# @Function  :
import time
from concurrent.futures import ThreadPoolExecutor, as_completed, wait, ALL_COMPLETED,FIRST_COMPLETED

executor = ThreadPoolExecutor(max_workers=3)  # 创建了一个线程池


def get_html(times, param1):
    time.sleep(times)  # 模拟网页请求
    print("获取网页信息{}".format(param1))
    return times


if __name__ == "__main__":
    # 通过submit方法提交执行的函数到线程池，submit 函数会立即返回，不会阻塞主线程
    # task1 = executor.submit(get_html, 5, "task1", 3)  # 返回task1 就是任务的句柄
    # task2 = executor.submit(get_html, 2, 'task2', 3)
    # task3 = executor.submit(get_html, 1, 'task3', 3)
    # task4 = executor.submit(get_html, 5, 'task4', 3)
    # # time.sleep(5)
    # print(task1.done())  # 检查任务是否完成，并返回结果
    # print("task4取消", task4.cancel())  # 取消任务的执行 未被放入到线程池中的任务才能取消成功
    # print("task1result",task1.result(timeout=6)) # 拿到任务执行的结果 该方法是一个阻塞方法
    # print("task3result",task3.result()) # 拿到任务执行的结果 该方法是一个阻塞方法
    # print("end")
    urls = [4, 2, 3]  # 模拟抓取网页的地址
    # 通过列表推导式构造多线程任务
    all_tasks = [executor.submit(get_html, url, "task" + str(url)) for url in urls]
    #
    # for item in as_completed(all_tasks):  # as_completed 是一个生成器
    #     data = item.result()
    #     print("任务返回值是{}".format(data))
    # 相当于把每一个任务映射到方法上 然后自动提交到线程池中
    # for data in executor.map(get_html, urls, ['a', 'b', 'c']):  # 按任务的输入顺序输出结果  而as_completed 时按任务的执行时长来输出结果
    #     print("任务返回值是{}".format(data))
    # wait方法 主要时用来阻塞主线程
    wait(all_tasks, return_when=FIRST_COMPLETED)  # 让主线程阻塞 直到指定的条件成立（等待子线程全部执行完之后 才开始执行主线程）
    print("代码执行完毕")
