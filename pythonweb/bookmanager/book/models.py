from django.db import models


# Create your models here.
# 类 -数据库表
# 属性 - 数据库字段
# 根据模型类 在数据库中生成表 也就是数据库迁移

class BookInfo(models.Model):
    # id 模型这边会自动创建
    name = models.CharField(max_length=20)
    def __str__(self):
        return  self.name


class PeopleInfo(models.Model,):
    # id 自动创建
    name = models.CharField(max_length=20)
    gender = models.BooleanField()
    book = models.ForeignKey(BookInfo,on_delete=models.CASCADE)  # 表示跟bookinfo相关联了
    def __str__(self):
        return self.name
