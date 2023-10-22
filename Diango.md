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

### 模板

* 



