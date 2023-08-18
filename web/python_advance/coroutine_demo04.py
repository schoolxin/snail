import asyncio
import datetime
import time


async def do_some_work(x):
    print("等待", x)
    await asyncio.sleep(x)  # 模拟等待一个耗时操作
    return '等待时间:{}'.format(x)

if __name__ == '__main__':
    start_time = datetime.datetime.now()
    # 定义多个协程对象
    coro1 = do_some_work(1)
    coro2 = do_some_work(2)
    coro3 = do_some_work(3)

    # 将协程对象转化为task 并组成一个list
    tasks = [
        asyncio.ensure_future(coro1),
        asyncio.ensure_future(coro2),
        asyncio.ensure_future(coro3)
    ]

    # 将tasks 注册到事件循环中
    # 两个方法 asyncio.wait asyncio.gather
    loop = asyncio.get_event_loop()
    # loop.run_until_complete(asyncio.wait(tasks))  # wait方法只接受列表作为参数
    loop.run_until_complete(asyncio.gather(*tasks))  # * 相当于一个解包符号
    for task in tasks:
        print("任务返回的结果是:", task.result())

    print("运行耗时",datetime.datetime.now()-start_time)
