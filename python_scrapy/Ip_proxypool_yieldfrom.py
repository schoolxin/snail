# -*- coding:utf-8 -*-
# @FileName  :Ip_proxypool_yieldfrom.py
# @Time      :2023/10/10 9:19
# @Author    :dzz
# @Function  :
import random
import time


def g1():
    yield range(5)


def g2():
    yield from range(5)


# a1 = g1()
#
# a2 = g2()
#
# for x in a1:
#     print(x)
#
#
# for x in a2:
#     print(x)

import asyncio


# @asyncio.coroutine
async def mygen(list):
    while len(list) > 0:
        value = random.randint(0, len(list) - 1)
        print(list.pop(value))
        # time.sleep(1)
        # yield from asyncio.sleep(1)
        await asyncio.sleep(1)


strlist = ['a', 'b', 'c']
intlist = [1, 2, 3]
c1 = mygen(strlist)
c2 = mygen(intlist)
try:
    loop = asyncio.get_event_loop()
    tasks = [c1, c2]
    loop.run_until_complete(asyncio.wait(tasks))
    loop.close()
except RuntimeError as e:
    pass

# print(type(asyncio.sleep(1)))