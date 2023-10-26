# Generated by Django 3.2.22 on 2023-10-26 03:12

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BookInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='书名')),
                ('pub_date', models.DateField(default=datetime.datetime(2023, 10, 26, 11, 12, 44, 612841), null=True, verbose_name='发布日期')),
                ('readcount', models.IntegerField(default=0, verbose_name='阅读量')),
                ('commentcount', models.IntegerField(default=0, verbose_name='评论量')),
                ('is_delete', models.BooleanField(default=False, verbose_name='逻辑删除')),
            ],
            options={
                'db_table': 'bookinfo',
            },
        ),
        migrations.CreateModel(
            name='PeopleInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='名称')),
                ('gender', models.IntegerField(choices=[(1, '男'), (2, '女')], default=1, verbose_name='性别')),
                ('description', models.CharField(max_length=200, null=True, verbose_name='描述信息')),
                ('is_delete', models.BooleanField(default=False, verbose_name='逻辑删除')),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='library.bookinfo', verbose_name='图书')),
            ],
            options={
                'verbose_name': '人物信息',
                'db_table': 'peopleinfo',
            },
        ),
    ]
