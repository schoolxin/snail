### MVT

* M全拼model 与mvc中的model是一样的 负责与数据库打交道
* V全拼View 与mvc中的Controller一样，接收请求 进行业务处理 返回应答
* T全拼Template 与mvc中的V相同，负责封装构造要返回的html

### 虚拟环境

* pip install virtualenv
* pip install virtualenvwrapper-win
* 创建虚拟环境：mkvirtualenv  虚拟环境的名字  如果要指定Python解释器创建虚拟环境：mkvirtualenv -p python3(或者python的可执行路径) 虚拟环境名字 eg：mkvirtualenv -p python3 py3_django
* workon 查看虚拟环境列表，后面跟上虚拟环境的名称，就会进行虚拟环境的切换
* 退出虚拟环境 deactivate
* 删除虚拟环境：rmvirtualenv  虚拟环境名称

### 创建Djang项目和应用

* 创建项目

> django-admin startproject （项目名称）
> manage.py 项目管理文件 通过这个文件进行项目管理，比如启动项目服务，创建应用，数据库迁移等
> settings.py 对整个项目进行设置
> urls.py  路由配置文件  给视图配置路由
> wsgi.py wsgi应用入口，可以创建wsgi应用实例，提供给wsgi服务调用
> python manage.py runserver 启动Django项目

* 创建应用(一个项目中多个应用，每个应用表示一个模块)

> python manage.py startapp 应用名称 或者django-admin startapp 应用名称
> admin.py 进行应用的站点管理相关的配置
> apps.py 应用独有的配置文件 比如配置应用的名字
> models.py 该应用所有模型的定义
> tests.py 定义测试案例和测试单元
> views.py 应用的所有视图都定义在此文件中
> migrations: 数据库迁移产生的迁移文件

* 注册应用

> 在bookmanager中的settings.py文件中的INSTALLED_APPS 填写book.apps.BookConfig

### 模型类

* python manage.py makemigrations 根据模型类生成数据库迁移文件
* python manage.py migrate 执行数据库迁移文件

### 站点管理

* admin.py 里面注册模型类

### 视图和URL

* 直接处理用户的http请求的视图，视图主要可以：

> 接收http请求
> 处理http请求
> 调用模型操作数据库
> 调用模板生成html页面
> 返回响应数据

* 使用视图的两个步骤

> 定义视图函数(视图就是一个python函数)
> 配置视图url()
> 视图必须定义在wiews.py文件中

* 单级URL配置文件
  
  > 一个 URL 配置就一个 django.conf.urls.url() 函数调用
  > url() 函数的第二个参数是 view 函数，或者一个列表/元组
  > url() 函数的第一个参数是 url 匹配的正则表达式字符串
* 多级URL配置文件

> **在项目中定义URLconf**
> url('正则表达式', include('应用名.urls模块名字'))
> ![在项目中定义URLconf](file:///C:/Users/order/Desktop/day4/Django%E8%B5%84%E6%96%99/%E6%8E%88%E8%AF%BE%E8%B5%84%E6%96%99/%E6%8E%88%E8%AF%BE%E8%B5%84%E6%96%99/%E8%AE%B2%E4%B9%89publish/Django%E5%9F%BA%E7%A1%80%E6%A8%A1%E7%89%88%E8%AE%B2%E4%B9%89-html%E7%89%88%E6%9C%AC/Django%E5%9F%BA%E7%A1%80%E6%A8%A1%E7%89%88%E8%AE%B2%E4%B9%89-html%E7%89%88%E6%9C%AC/1Django%E5%BC%80%E5%8F%91%E6%B5%81%E7%A8%8B/6.%E8%A7%86%E5%9B%BE%E5%92%8CURL/image-20191223195607969.png)
> **在应用中定义URLconf**
> url('正则表达式', view函数对象)
> ![在应用中定义URLconf](file:///C:/Users/order/Desktop/day4/Django%E8%B5%84%E6%96%99/%E6%8E%88%E8%AF%BE%E8%B5%84%E6%96%99/%E6%8E%88%E8%AF%BE%E8%B5%84%E6%96%99/%E8%AE%B2%E4%B9%89publish/Django%E5%9F%BA%E7%A1%80%E6%A8%A1%E7%89%88%E8%AE%B2%E4%B9%89-html%E7%89%88%E6%9C%AC/Django%E5%9F%BA%E7%A1%80%E6%A8%A1%E7%89%88%E8%AE%B2%E4%B9%89-html%E7%89%88%E6%9C%AC/1Django%E5%BC%80%E5%8F%91%E6%B5%81%E7%A8%8B/6.%E8%A7%86%E5%9B%BE%E5%92%8CURL/image-20191223195638421.png)

### 模板

### 配置文件和静态文件

* settings配置文件

> BASE_DIR:当前工程的根目录，Django会依此来定位工程中的相关文件，我们也可以使用该参数来构建文件路径 eg：BASE_DIR F:\study\python\snail\pythonweb\bookmanager
> Debug：调试模式，工程创建后默认是True，作用：1.修改代码，程序自动重启；2.Django程序出现异常时，先前端页面显示详细的错误信息，在发布上线的时候该参数要修改为false 并且ALLOWED_HOSTS需要修改，修改为主机的域名，当该值被设置为False的时候，ALLOWED_HOSTS必须修改，当程序出错的时候前端页面只会显示 Server Error (500)

* 静态文件

> 为了提供静态文件，需要配置两个参数：1.STATICFILES_DIRS 存放查找静态文件的目录；2。STATIC_URL 访问静态文件的URL前缀，Django默认的静态文件服务器需要在调试模式才能起作用

### 应用的配置类

* 在每个应用目录中都包含了 apps.py 文件，用于保存该应用的配置信息,在创建应用时，Django 会向 apps.py 文件中写入一个该应用的配置类，如
  UNIX[Unix 时间戳（Unix Timestamp）定义为从UTC/GMT的1970年1月1日0时0分0秒开始所经过的秒数，不考虑闰秒](https://so.csdn.net/so/search?q=%E6%97%B6%E9%97%B4%E6%88%B3&spm=1001.2101.3001.7020)概念：因为UNIX时间戳只是一个秒数，一个UNIX时间戳在不同时区看来，时间是不同的。
  如UNIX时间戳0，在0时区看来是1970-01-01 00:00:00，在东八区看来是1970-01-01 08:00:00

```
from django.apps import AppConfig


class BookConfig(AppConfig):
    name = 'book'
```

> **AppConfig.name** 属性表示这个配置类是加载到哪个应用的，每个配置类必须包含此属性，默认自动生成。

> **AppConfig.verbose\_name** 属性用于设置该应用的直观可读的名字，此名字在 Django 提供的 Admin 管理站点中会显示这个名字，如

```
from django.apps import AppConfig


class UsersConfig(AppConfig):
    name = 'book'
    verbose_name = '图书管理'
```

* 我们将此类添加到工程 settings.py 中的 INSTALLED\_APPS 列表中，表明注册安装具备此配置属性的应用。

### 模型完整讲解

* 配置MySQL数据库
* 修改settings.py中的配置数据库信息

