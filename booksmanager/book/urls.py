# -*- coding:utf-8 -*-
# @FileName  :urls.py
# @Time      :2023/10/23 16:06
# @Author    :dzz
# @Function  :
# import os
# import sys
#
# root_path = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
# sys.path.append(root_path)


from django.conf.urls import url


from .views import book_list

urlpatterns = [
    url(r'^booklist/$', book_list)
]
