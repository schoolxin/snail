# -*- coding:utf-8 -*-
# @FileName: Ip_proxypool_yield.py
# @Time:2023/10/8 16:17
# @Author    :dengzz
'''
yield

可迭代对象和迭代器 生成器
可迭代对象：指实现了__iter__方法的对象，由于实现了__iter__方法，所以可直接用于for循环中，比如常见的dic  list   string都是可迭代对象
迭代器：指任何实现了__iter__ 和__next__()方法的对象(两个方法都必须实现，缺一不可)，其中__iter__返回迭代器本身  __next__()方法返回容器中的下一个值，
如果没有更多的元素则抛出stopIteration异常，有迭代器可以得出一个结论 迭代器肯定是可迭代对象  可迭代对象不一定是迭代器

'''