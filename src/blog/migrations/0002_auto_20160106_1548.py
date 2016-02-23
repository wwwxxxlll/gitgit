# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='adminm',
            options={'verbose_name': '\u7528\u6237', 'verbose_name_plural': '\u7528\u6237\u6ce8\u518c'},
        ),
        migrations.AlterModelOptions(
            name='lanmu',
            options={'verbose_name': '\u680f\u76ee', 'verbose_name_plural': '\u6587\u7ae0\u680f\u76ee'},
        ),
        migrations.AlterModelOptions(
            name='pinglun',
            options={'verbose_name': '\u8bc4\u8bba', 'verbose_name_plural': '\u6587\u7ae0\u8bc4\u8bba'},
        ),
        migrations.AlterModelOptions(
            name='wenzhang',
            options={'verbose_name': '\u6587\u7ae0', 'verbose_name_plural': '\u6587\u7ae0'},
        ),
        migrations.AlterField(
            model_name='wenzhang',
            name='author',
            field=models.ForeignKey(verbose_name='\u6587\u7ae0\u4f5c\u8005', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='wenzhang',
            name='date',
            field=models.DateTimeField(auto_now_add=True, verbose_name='\u65e5\u671f'),
        ),
        migrations.AlterField(
            model_name='wenzhang',
            name='lanmu',
            field=models.ForeignKey(verbose_name='\u6587\u7ae0\u680f\u76ee', to='blog.lanmu'),
        ),
        migrations.AlterField(
            model_name='wenzhang',
            name='title',
            field=models.CharField(max_length=100, verbose_name='\u6587\u7ae0\u6807\u9898'),
        ),
    ]
