from django.db import models


# Create your models here.

# 模型类对应的表名：默认是：应用名_模型小写   book_bookinfo 也可以自己定义在数据库中的表名称
class BookInfo(models.Model):
    name = models.CharField(max_length=20, verbose_name="书籍名称")  # verbose_name 站点管理显示的名称
    pub_date = models.DateField(null=False, verbose_name="发布日期")  # null 字段是否可以为空
    readcount = models.IntegerField(default=0, verbose_name="阅读总数")
    commentcount = models.IntegerField(default=0, verbose_name="评论总量")
    is_delete = models.BooleanField(default=0, verbose_name="是否被删除")

    # 定义模型类在数据库中的表名
    class Meta:
        db_table = 'bookinfo'

    def __str__(self):
        return self.name


class PeopleInfo(models.Model):
    GENDER_CHOICES = (
        (0, "male"),
        (1, "female")
    )
    name = models.CharField(max_length=20, verbose_name="作者名")
    gender = models.IntegerField(choices=GENDER_CHOICES, default=0, verbose_name='性别')
    description = models.CharField(max_length=1000, null=True, verbose_name="人物描述")
    book = models.ForeignKey(BookInfo, on_delete=models.CASCADE, verbose_name="书籍ID")
    is_delete = models.BooleanField(default=0, verbose_name="是否被删除")

    class Meta:
        db_table = 'peopleinfo'

    def __str__(self):
        return self.name
