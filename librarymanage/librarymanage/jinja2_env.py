from django.contrib.staticfiles.storage import staticfiles_storage
from django.template.defaultfilters import date, safe
from django.urls import reverse
from jinja2 import Environment


def environment(**options):
    env = Environment(**options)
    env.filters['date'] = date  # 增加过滤器 将Django自带的过滤器添加到Jinja2中
    env.filters['list_reverse'] = list_reverse # 自己定义过滤器
    env.filters['safe'] = safe # 自己定义过滤器
    env.globals.update({
        'static': staticfiles_storage.url,
        'url': reverse,
    })
    return env


def list_reverse(li):
    if isinstance(li, list):
        # li.reverse()
        return li[::-1] # 列表反转
    else:
        raise Exception("li type error")

