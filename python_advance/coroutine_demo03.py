import asyncio
import time


# async def hello(x):
#     # time.sleep() # 是一个同步操作语句，无法达到异步结果
#     await asyncio.sleep(x)
#     return '暂停了{}秒'.format(x)
#
#
# coro = hello(2)
#
# loop = asyncio.get_event_loop()
#
# task = asyncio.ensure_future(coro)
#
# loop.run_until_complete(task)
#
# # 通过task.result() 获取返回结果
# print("返回结果是:{}".format(task.result()))

# 第二种方法，通过asyncio自带的添加回调函数功能来实现
async def hello(x):
    # time.sleep() # 是一个同步操作语句，无法达到异步结果
    await asyncio.sleep(x)
    return x


def callback(future):
    sum = 10 + future.result()
    print("回调返回结果相加的结果为:{}".format(sum))


coro = hello(4)

loop = asyncio.get_event_loop()

task = asyncio.ensure_future(coro)
task.add_done_callback(callback)
loop.run_until_complete(task)
