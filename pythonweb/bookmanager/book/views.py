from django.http import HttpRequest, HttpResponse
from django.shortcuts import render


# Create your views here.
# 第一个参数： 里面是httpRequest类型的对象，里面包含了请求的所有数据
# 视图函数的返回值是HttpResponse类型的对象，里面包含了响应的所有数据
def index(request: HttpRequest):
    context = {'content': '模板数据===='}  # 上下文数据需要是一个字段
    return render(request,'book/index.html',context) # 模板引擎
