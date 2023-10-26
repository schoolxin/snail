import json

from django.http import HttpRequest, HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from django.urls import reverse


# Create your views here.

def test(request: HttpRequest):
    return HttpResponse("test")


# 其中num1,num2 匹配view 中 正则匹配url的分组数据 url(r'(\d+)/(\d+)', index)  URL路径参数 在路由中使用正则表达式并且分组的形式获取
def index(request: HttpRequest, num1, num2):
    # test_url = reverse('library1:test_1')  # reverse函数，可以根据路由名称，返回具体的 URL 路径  对于未指明 namespace 的，reverse("路由name") 对于指明 namespace 的，reverse("命名空间namespace:路由name")

    # GET 返回的是一个QueryDict 类型，里面的键是可以重复的  如果想获取重复键的值 可以使用getlist
    # bookname = request.GET.get('bookname')
    booknames = request.GET.getlist('bookname', '默认值')  # 查询字符串 获取请求路径中的查询字符串参数（形如?k1=v1&k2=v2

    # 请求体 中的参数

    return HttpResponse('num2:' + num2 + 'num1:' + num1 + "bookname:" + str(booknames))


def post_form(request: HttpRequest):
    books = request.POST.getlist('name')
    readcount = request.POST.get('readcount')
    print('readcount:' + readcount + "books:" + str(books))
    return HttpResponse('readcount:' + readcount + "books:" + str(books))


def post_json(request: HttpRequest):
    body = request.body
    body_dict = json.loads(body)
    print(body_dict)
    # print(body.decode('utf-8'))
    # 可以通过request.META 属性获取请求头headers中的数据，request.META为字典类型
    print(request.META.get('CONTENT_TYPE'))
    print(request.META.get('HTTP_HOST'))
    return HttpResponse("tt")


def create_response(request: HttpRequest):
    # content 响应体数据 以接受字节码类型的数据或者字符串数据
    # content_type 响应体数据类型 application/json 返回json
    book = {
        'name': '天龙八部',
        'readcount': 20000,
        'peoples': ['乔峰', '虚竹', '段誉']
    }
    # dumps 字典转json字符串
    # loads json转为字符串
    book_json = json.dumps(book)
    print(book_json)
    return HttpResponse(content=book_json, content_type='application/json', status=200)

def create_jsonresponse(request: HttpRequest):
    book = {
        'name': '天龙八部',
        'readcount': 20000,
        'peoples': ['乔峰', '虚竹', '段誉']
    }
    # 自动帮助我们将数据转换为json字符串
    # 自动设置响应头
    # Content - Type    为    application / json
    return JsonResponse(book)