# -*- coding:utf-8 -*-
# @FileName: urls.py
# @Time:2023/10/22 17:51
# @Author    :dengzz
from django.conf.urls import url
from django.urls import path

from pythonweb.bookmanager.book.views import index

urlpatterns = [
    # 第一个参数是一个正则表达式，第二参数是视图函数或者是一个列表元组 也可以使用path()  但是path的第一个参数不是正则表达式 全匹配
    # ^ 严格开始   $严格结束
    url(r'^index/$', index),
]
