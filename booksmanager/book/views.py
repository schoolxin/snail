from django.db.models import F, Q, Sum, Count
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
BookInfo.objects.filter(id=1)
# exclude 排除掉符合条件剩下的结果，返回 QuerySet 类型对象
# all 查询多个结果，返回 QuerySet 类型对象
BookInfo.objects.all()
# count 查询结果数量
BookInfo.objects.count()

# 查询条件
# 查询编号为2的图书
BookInfo.objects.filter(id__exact=2)  # 返回的结果是一个QuerySet 相等运算符exact 可以省略 变成filter(id=1)
# 查询书名包含'湖'的图书
BookInfo.objects.filter(name__contains="湖")
# 查询书名以'部'结尾的图书
BookInfo.objects.filter(name__endswith="湖")
# 查询书名为空的图书
BookInfo.objects.filter(name__isnull=False)
# 查询编号为2或3或5的图书
BookInfo.objects.filter(id__in=[2, 3, 5])
# 查询编号大于3的图书
BookInfo.objects.filter(id__gt=3)
BookInfo.objects.exclude(id__gt=3)
# 查询1980年发表的图书
BookInfo.objects.filter(pub_date__year='1980')
# 查询1990年1月1日后发表的图书
BookInfo.objects.filter(pub_date__gt='1980-01-01')

# F 对象   两个属性怎么比较

# 案例：
# 查询阅读量大于等于评论量的图书。
BookInfo.objects.filter(readcount__gt=F('commentcount'))
# 查询阅读量大于2倍评论量的图书。
BookInfo.objects.filter(readcount__gt=F('commentcount') * 2)
#
# 查询阅读量大于20，并且编号小于3的图书。
BookInfo.objects.filter(readcount__gt=20, id__lt=3)
BookInfo.objects.filter(readcount__gt=20).filter(id__lt=3)
#
# 查询阅读量大于20的图书。
BookInfo.objects.filter(Q(readcount__gt=20))
# 查询阅读量大于20，或编号小于3的图书。
BookInfo.objects.filter(Q(readcount__gt=20) | Q(id__lt=3))
# 查询编号不等于3的图书。
BookInfo.objects.filter(~Q(id__lt=3))

# 聚合函数
# QuerySet 和 Model.objects 都有 aggregate() 函数
# 查询id大于2的图书的总量和总阅读量。
BookInfo.objects.filter(id__gt=2).aggregate(Sum('readcount'), Count('id'))
BookInfo.objects.aggregate(Sum('readcount'), Count('id'))
# 使用count时一般不使用 aggregate() 过滤器
BookInfo.objects.filter(readcount__gt=10).count()

# 排序
BookInfo.objects.all().order_by('readcount')

# 关联查询
# 基本关联查询
# 1.由一到多
# 语法：一的模型类对象.多的模型类名小写_set
# 查询书籍id为1的所有人物信息
book = BookInfo.objects.get(id=1)
book.peopleinfo_set.all()
# 查询人物id为1的书籍信息  语法:多的模型类对象.多的模型类中的关联类的属性名
PeopleInfo.objects.get(id=1).book
# 查询人物id为1的数据的id
PeopleInfo.objects.get(id=1).book_id
# 查询图书，要求图书人物为"郭靖"
BookInfo.objects.filter(peopleinfo__name='郭靖')
# 查询图书，要求图书中人物的描述包含"八"
BookInfo.objects.filter(peopleinfo__description__contains='八')
# 查询书名为“天龙八部”的所有人物
PeopleInfo.objects.filter(book__name="天龙八部")
# 查询图书阅读量大于30的所有人物

PeopleInfo.objects.filter(book__readcount__gt=30)

BookInfo.objects.filter(readcount__gt=30).order_by('pub_date')
BookInfo.objects.filter(readcount__gt=30).order_by('pub_date').exists()

books = BookInfo.objects.all()
[book.name for book in BookInfo.objects.all()]

# 切片
books[1:2]


#查询数据
books = BookInfo.objects.all()
#导入分页类
from django.core.paginator import Paginator
#创建分页实例
paginator=Paginator(books, 2)
#获取指定页码的数据
page_skus = paginator.page(1)
#获取分页数据
total_page=paginator.num_pages