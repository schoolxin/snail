import datetime
import json

from django.http import HttpRequest, HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import View


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


def set_cookie(request: HttpRequest):
    # 浏览器第一次请求某个服务器的时候，是不带 Cookie 信息的
    # 服务器收到http请求后，会先检查http请求的 cookie 请求头，获取 cookie 信息
    # 如果没有想要的 cookie 信息，服务器会生成一个 key-value 数据，名称和值都由服务器端自己定义，通过 http 响应的 set-cookie 响应头返回给浏览器
    # 浏览器将响应中的 set-cookie 响应头里面的 key-value 提取出来，在本地保存起来，比如保存到某个目录下的文件中或者 sqlite 数据库中
    # 浏览器下次请求同一个网站时就自动在 http 请求头中带上 key-value 键值对，放在 cookie 请求头里面
    print(request.headers)
    print(request.COOKIES)  # request.COOKIES 可以获取cookies 属性中获取cookies请求头 是一个字典
    cookies = request.COOKIES
    response = HttpResponse("set_cookie")
    if 'user_id' in cookies:
        print(cookies.get('user_id'))
        response.delete_cookie('user_id')
    else:
        response.set_cookie("user_id",
                            "99999100010")  # 可以给响应设置Set-cookie 响应头  返回给浏览器 max_age 以秒为单位 默认值表示 cookie的值的保存时间为当前会话 会话关闭  自动删除
    return response


# session
def set_session(request: HttpRequest):
    # 浏览器第一次访问服务器的时候，cookie 里面没有 session 相关信息，如果是用户登录，请求会携带用户名和密码的信息
    # 当我们的服务器收到这个请求后，处理请求，返回 http 响应，并且会在响应中添加 set-cookie 响应头，里面返回 session_id 和 session_key 这个键值对
    # session 中间件先从 cookie 里面获取 session_id 这个cookie的值，这个值就是 session_key，如果获取不到 session_key 就随机生成一个 32 位的由小写字母和数字组成的字符串作为 session_key
    # 视图会进行用户名和密码验证，验证没有问题，一般会把 user_id 从用户表里面取出来，保存到 session 里面，以 'user_id' 为 key，数据库中查询到的 user_id 值为 value，存储在 session 里面

    # 视图返回 response 后，session 中间件还会在 response 上设置一个 session_id 这个 cookie 值，这个 cookie 值的 key 是 ‘session_id’，value 是第1步产生的 session_key
    # session 中间件把 session 这个字典数据保存在数据库中，session_key 是主键的值，session 字典转换为字符串后保存为 data 的值
    # 在浏览器收到响应数据后，会从 cookie 里面获取到 session_id 这个 cookie 的 key-value，并且保存起来
    # 浏览器第二次访问服务器的时候，cookie 里面就自动带上 session_id 这个 cookie 的 key-value
    # 服务器第二次收到请求后，就可以从 cookie 里面获取到 session_id 这个 key-value，也可以得到前面的 session_key，然后从数据库中加载查询 session 的数据，并且转换为字典
    username = request.GET.get('username')
    passwd = request.GET.get('passwd')
    # 设置session
    request.session['user_id'] = 123456

    return HttpResponse("set_session")


def get_session(request: HttpRequest):
    print(request.session.get('user_id'))
    return HttpResponse("get_session")


def register(request: HttpRequest):
    if request.method == 'GET':
        return render(request, 'register.html')
    elif request.method == 'POST':
        # 处理注册请求逻辑
        return HttpResponse("register")
    else:
        pass

    return HttpResponse("register")


# 类视图
class Register(View):
    def get(self, request):
        return render(request, 'register.html')

    def post(self, request):
        return HttpResponse("post")


def test_middleware(request: HttpRequest):
    print("视图函数处理")
    return HttpResponse("middleware")


def test_template(request: HttpRequest):
    username = request.GET.get('name', 'wangwu')
    contexts = {
        "username": username
    }
    return render(request, "index.html", context=contexts)


def home(request: HttpRequest):
    contexts = {
        'school': 'woniuxy',
        'assets': 100000000,
        'is_accept': True,
        'areas': ['成都校区', '重庆校区', '武汉校区', '天府校区'],
        'subject': {
            'name': 'python',
            'count': 600,
            'price': 20000,
            # "description":"<script>alert('tt')</script>"
            'create_date': datetime.datetime.now()
        }
    }
    return render(request, "home.html", context=contexts)


def detail(request: HttpRequest):
    return render(request, 'detail.html')
