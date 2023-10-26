import datetime

from django.db import models


# Create your models here.
# 一个模型类 对应一个表  类中的属性对应表中的字段  一个实例 代表一行数据
class BookInfo(models.Model):
    name = models.CharField(max_length=20, null=False, verbose_name="书名")
    pub_date = models.DateTimeField(null=True, verbose_name="发布日期", default=datetime.datetime.now())
    readcount = models.IntegerField(default=0, verbose_name="阅读量")
    commentcount = models.IntegerField(default=0, verbose_name="评论量")
    is_delete = models.BooleanField(default=False, verbose_name="逻辑删除")

    def __str__(self):
        return self.name

    class Meta:
        db_table = "bookinfo"  # 自己定义数据库中的表 如果不指定默认是 应用名作为前缀


class PeopleInfo(models.Model):
    CHOICES = [
        (1, '男'),  # 1 会存入数据库中
        (2, '女')
    ]
    name = models.CharField(max_length=20, verbose_name='名称')
    gender = models.IntegerField(choices=CHOICES, default=1, verbose_name="性别")
    description = models.CharField(max_length=200, null=True, verbose_name='描述信息')
    book = models.ForeignKey(BookInfo, on_delete=models.CASCADE, verbose_name='图书')  # 外键
    is_delete = models.BooleanField(default=False, verbose_name='逻辑删除')

    class Meta:
        db_table = 'peopleinfo'
        verbose_name = '人物信息'  # 在admin站点中显示的名称

    def __str__(self):
        return self.name
