def my_cycle(n):
    '''
    :param n: 循环次数
    :return: 无返回值
    '''
    # 文档字符串 需要写在函数的第一行才可以
    for i in range(n):
        print(i)
        if i == 3:
            return # 返回None 然后结束整个函数


print(my_cycle.__doc__)
print(my_cycle(10))