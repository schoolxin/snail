# 使用asyncio 原生协程定义
# async 关键字表明当前我们定义的是一个协程对象
from collections import Coroutine
async def hello():
    print("hello")


coro = hello() #生成协程对象，并不会运行函数内部的代码

print(isinstance(coro,Coroutine))