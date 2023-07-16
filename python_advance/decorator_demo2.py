import time


def timer(func):
    def gf(*args,**kwargs):
        start_time = time.time()
        func(*args,**kwargs)
        end_time = time.time()
        print("运行fun的时间为{}".format(end_time - start_time))

    return gf


@timer # foo = timer(foo)
def foo(*args,**kwargs):
    time.sleep(3)
    print("in foo",args)


# foos = timer(foo)
# foos()

foo('woniu')  # 相当于将foo函数传递给timer函数(装饰器)
foo('woniu',98)  # 相当于将foo函数传递给timer函数(装饰器)
