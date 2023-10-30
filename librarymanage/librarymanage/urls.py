"""librarymanage URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    # url(r'^admin/', admin.site.urls),
    # 只要不是admin/ 都算匹配成功
    # http://127.0.0.1:8000/test/
    url(r'^', include(('library.urls','library'), namespace='library1')),  # 项目名.urls
    # url(r'^test/', include('library.urls')), # 项目名.urls   用请求地址后面的test/ 和正则表达式匹配 匹配上之后 将剩余字符串的和应用中的url匹配 即项目这里匹配上了test/ 后剩余就是空的了 所以和应用中的/test路径匹配不上了
]
