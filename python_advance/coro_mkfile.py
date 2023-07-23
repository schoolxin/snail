import asyncio
from datetime import datetime


# 定义一个协程对象
async def mk_file(path, x):
    print("正在生成{}个文件".format(x))
    with open(path, mode='w') as f:
        f.write('this is file {}'.format(x))


if __name__ == '__main__':

    start = datetime.now()
    # 定义一个事件循环
    loop = asyncio.get_event_loop()

    # 生成若干个协程
    tasks = []

    for i in range(1, 1001):
        tasks.append(mk_file("D:/demo/file" + str(i) + '.txt', i))

    loop.run_until_complete(asyncio.wait(tasks))  # 将task 扔进事件循环中执行

    print("任务消耗事件为", datetime.now() - start)
