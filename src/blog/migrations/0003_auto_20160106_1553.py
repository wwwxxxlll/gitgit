# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20160106_1548'),
    ]

    operations = [
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name': '\u7ec4',
                'verbose_name_plural': '\u7ec4\u540d',
            },
        ),
        migrations.AddField(
            model_name='wenzhang',
            name='dgroup',
            field=models.ManyToManyField(to='blog.Group'),
        ),
    ]
