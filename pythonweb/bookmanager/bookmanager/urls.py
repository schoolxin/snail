"""bookmanager URL Configuration

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
from django.contrib import admin
from django.urls import path, include

from pythonweb.bookmanager.book.views import index

urlpatterns = [
    path('admin/', admin.site.urls),
    # 第一个参数是一个正则表达式，第二参数是视图函数或者是一个列表元组

    # 这个是多级url配置的方法  path 可以换成url
    path('', include('book.urls')),
]
