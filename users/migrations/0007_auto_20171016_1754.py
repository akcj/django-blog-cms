# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-16 17:54
from __future__ import unicode_literals

from django.db import migrations, models
import users.models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_auto_20171012_1810'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='user',
            managers=[
                ('objects', users.models.UserManager()),
            ],
        ),
        migrations.AddField(
            model_name='user',
            name='update_date',
            field=models.DateTimeField(auto_now=True, verbose_name='\u4fee\u6539\u65f6\u95f4'),
        ),
        migrations.AlterField(
            model_name='user',
            name='nickname',
            field=models.CharField(error_messages={'unique': '\u8be5\u6635\u79f0\u88ab\u5360\u7528'}, max_length=50, unique=True, verbose_name='Nickname'),
        ),
    ]
