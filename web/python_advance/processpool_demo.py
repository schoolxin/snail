import multiprocessing
import time


def get_html(n):
    time.sleep(n)
    print('{}子进程获取内容成功'.format(n))
    return n


if __name__ == '__main__':
    pool = multiprocessing.Pool(multiprocessing.cpu_count())  # cpu_count 自动获取当前设备上的cpu的核心数
    # result = pool.apply_async(get_html,args=(3,)) # 异步执行
    # pool.close() # 这个方法必须要在join之前调用
    # pool.join() # 主进程要等待子进程执行完 才能执行
    #
    # print(result.get()) # get 方法是一个阻塞方法 获取到子进程的执行结果
    # print("end")

    for result in pool.imap_unordered(get_html, [5, 2, 3, 4]):  # imap_unordered 先执行完的先输出   imap 按任务提交顺序输出结果

        print("{}休眠执行成功".format(result))
