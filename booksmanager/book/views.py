from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

from .models import BookInfo
from book.models import PeopleInfo


# Create your views here.

def book_list(request: HttpRequest):
    books = BookInfo.objects.all()
    print(books)
    return HttpResponse("booklist")


# 插入数据  save  通过创建模型类对象，执行对象的save()方法保存到数据库中。


bookinfo = BookInfo(name="Python入门", pub_date="2023-01-01")
# bookinfo.save()
# 通过 模型类.objects.create() 插入数据
PeopleInfo.objects.create(name="蜗牛学院", book=BookInfo(id=6))

# 修改数据
# 1.save  get()返回的是一个实例对象
p = PeopleInfo.objects.get(name="蜗牛学院")  # get方法只能获取一行数据
p.name = "蜗牛学院2"
p.save()
# 2.update  可以批量修改数据
# filter 返回的数据类型是QuerySet
PeopleInfo.objects.filter(book_id=1).update(is_delete=1)
# 3.删除数据
# delete 删除数据
PeopleInfo.objects.get(name="蜗牛学院2").delete()
# 2.QuerySet 中的delete方法删除数据
PeopleInfo.objects.filter(book_id=10).delete()

# 查询
# get 查询单一结果，模型类实例，如果不存在会抛出模型类 DoesNotExist 异常
BookInfo.objects.get(name="天龙八部")
BookInfo.objects.exclude(id=1)
# filter 过滤出多个结果，返回 QuerySet 类型对象
# exclude 排除掉符合条件剩下的结果，返回 QuerySet 类型对象
# all 查询多个结果，返回 QuerySet 类型对象
# count 查询结果数量
