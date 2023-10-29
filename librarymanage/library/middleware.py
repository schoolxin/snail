# -*- coding:utf-8 -*-
# @FileName: middleware.py
# @Time:2023/10/27 22:26
# @Author    :dengzz
from django.http import HttpRequest


def my_middleware(get_response):
    print("init 被调用")

    def middleware(request: HttpRequest):
        # print(get_response)
        print("before request 被调用")
        res = get_response(request)
        print('after response 被调用')
        return res

    return middleware
def my_middleware2(get_response):
    print("init2 被调用")

    def middleware(request: HttpRequest):
        # print(get_response)
        print("before request 被调用2")
        res = get_response(request)
        print('after response 被调用2')
        return res

    return middleware


