from collections.abc import Iterable

# print(isinstance([], Iterable))


class Student:
    pass


# print(isinstance(Student, Iterable))


class Employee:
    def __init__(self, emps):
        self.emp = emps

    def __getitem__(self, item):  # 其中item是解释器帮我们维护的索引值，当在for循环中时，自动从0开始计数

        return self.emp[item]


emp = Employee(['zhang', 'li', 'sun'])
# for items in emp:
#     print(items)


emp_iter = iter(emp)

for i in emp_iter:
    print(i)

for i in emp_iter:
    print(i)