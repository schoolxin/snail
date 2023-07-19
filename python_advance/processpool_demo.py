import multiprocessing
import time


def get_html(n):
    time.sleep(n)
    print('{}子进程获取内容成功'.format(n))
    return n


if __name__ == '__main__':
    pool = multiprocessing.Pool(multiprocessing.cpu_count()) # cpu_count 自动获取当前设备上的cpu的核心数