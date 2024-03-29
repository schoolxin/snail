# -*- coding:utf-8 -*-
# @FileName  :urls.py
# @Time      :2023/10/26 9:29
# @Author    :dzz
# @Function  :

from django.conf.urls import url

from library.views import test, index, post_form, post_json, create_response, create_jsonresponse, set_cookie, \
    set_session, get_session, register, Register, test_middleware, test_template, home, detail

urlpatterns = [
    # http://127.0.0.1:8000/test/项目中匹配完  剩下test/ 用于匹配
    url(r'^test/$', test, name='test_1'),  # 第二个参数 views模块的中的方法名
    url(r'^index/$', index),  # 第二个参数 views模块的中的方法名
    # http://127.0.0.1:8000/18/188/  在项目中匹配完之后 到应用中之后就只剩18/188/
    # url(r'(\d+)/(\d+)', index),  # 第二个参数 views模块的中的方法名
    url(r'(?P<num1>\d+)/(?P<num2>\d+)', index),
    # 第二个参数 views模块的中的方法名 给正则表达式的分组起名字?P<num1>  url 路径中的参数提取 一般需要使用正则表达式并且分组
    # http://127.0.0.1:8000/post_form/
    url(r'^post_form/$', post_form),
    url(r'^post_json/$', post_json),
    url(r'^create_response/$', create_response),
    url(r'^set_cookie/$', set_cookie),
    url(r'^set_session/$', set_session),
    url(r'^get_session/$', get_session),
    # url(r'^register/$', register),
    url(r'^register/$', Register.as_view()),
    url(r'^test_middleware/$', test_middleware),
    url(r'^test_template/$', test_template),
    url(r'^home/$', home),
    url(r'^detail/$', detail),
]
