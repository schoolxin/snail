import time


def timer(timer_type):
    def outer(func): # 加入一层嵌套函数，并且接收被装饰函数名作为参数
        def inner(*args, **kwargs):
            start_time = time.time()
            res = func(*args, **kwargs)
            end_time = time.time()
            print("运行fun的时间为{}".format(end_time - start_time))
            return res

        return inner # 返回inner的引用

    return outer # 返回outer的引用


@timer(timer_type='minutes')  # foo = timer(timer_type='minutes')(foo)
def foo(name, age):
    time.sleep(3)
    print("in foo", name, age)
    return name


# foos = timer(foo)
# foos()

# foo('woniu')  # 相当于将foo函数传递给timer函数(装饰器)
print(foo('woniu', 98))  # inner(*args, **kwargs)
