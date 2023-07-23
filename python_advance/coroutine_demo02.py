import asyncio


# 定义协程对象
async def hello(name):
    print("hello", name)


# 创建协程对象
coro = hello('北京')

# 获取事件循环对象容器
loop = asyncio.get_event_loop()

# 将协程对象转换为task

# task = loop.create_task(coro)
task1 = asyncio.ensure_future(coro)

# 将task任务扔进事件循环对象中触发

loop.run_until_complete(task1)
# loop.run_until_complete(task1)
