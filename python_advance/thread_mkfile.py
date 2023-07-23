import threading, time
from datetime import datetime


def mk_file(path, x):
    print("正在生成{}个文件".format(x))
    with open(path, mode='w') as f:
        f.write('this is file {}'.format(x))


if __name__ == '__main__':
    start = datetime.now()
    threads = []
    for i in range(1, 1001):
        t = threading.Thread(target=mk_file, args=("D:/demo/file" + str(i) + '.txt', i))
        threads.append(t)
        t.start()
    [t.join() for t in threads] # 阻塞主线程

    print("任务消耗事件为", datetime.now() - start)