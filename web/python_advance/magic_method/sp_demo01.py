# -*- coding:utf-8 -*-
# @FileName  :sp_demo01.py
# @Time      :2023/7/24 9:47
# @Author    :dzz
# @Function  :
import re



class ob1:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __repr__(self):
        return "姓名{nm}和年龄{ag}".format(nm=self.name, ag=self.age)


if __name__ == "__main__":
    o1 = ob1('zhan', 1000)
    print(o1)
    # print(o1.__repr__())
    str = "https://api.klarna.com/settlements/v1/transactions?start_date=2023-06-28&end_date=2023-07-28T00%3A00%3A00Z&offset=4000&size=500"

    pattern = re.compile(r'.*offset=(\d+)')
    print(pattern.match(str).groups())

