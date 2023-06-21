def my_cycle(n):
    '''
    :param n: 循环次数
    :return: 无返回值
    '''
    # 文档字符串 需要写在函数的第一行才可以
    for i in range(n):
        print(i)
        if i == 3:
            return  # 返回None 然后结束整个函数


print(my_cycle.__doc__)
print(my_cycle(10))


def foo(name, address, age=100):
    print("name-->", name, "address-->", address)


foo('li', 'beijing')
# foo('li',name='wu') 这种调用会报错

print("可变参数")


def foo1(numbers, *args, **kwargs):
    print("numbers", numbers)
    print("args的长度", len(args))
    for i in args:
        print(i)
    print("kwargs的长度", len(kwargs))
    for k, v in kwargs.items():
        print("k-->", k, "v--->", v)


foo1(1, 2, 3, 4, 5, 6, name="lishi", age=100, address="china")


def fun2(name):
    name += "lishi"
    print(name)


n1 = "6666"
fun2(n1)
print(n1)

def fun3(al):
    al.append("33")
    print(al)

als = [1,2,3,4,4]
fun3(als)
print(als)