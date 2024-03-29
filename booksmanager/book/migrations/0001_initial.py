# Generated by Django 3.2.22 on 2023-10-23 15:26

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
                ('name', models.CharField(max_length=20, verbose_name='书籍名称')),
                ('pub_date', models.DateField(verbose_name='发布日期')),
                ('readcount', models.IntegerField(default=0, verbose_name='阅读总数')),
                ('commentcount', models.IntegerField(default=0, verbose_name='评论总量')),
                ('is_delete', models.BooleanField(default=0, verbose_name='是否被删除')),
            ],
            options={
                'db_table': 'bookinfo',
            },
        ),
        migrations.CreateModel(
            name='PeopleInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='作者名')),
                ('gender', models.IntegerField(choices=[(0, 'male'), (1, 'female')], default=0, verbose_name='性别')),
                ('description', models.CharField(max_length=1000, null=True, verbose_name='人物描述')),
                ('is_delete', models.BooleanField(default=0, verbose_name='是否被删除')),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='book.bookinfo', verbose_name='书籍ID')),
            ],
            options={
                'db_table': 'peopleinfo',
            },
        ),
    ]
