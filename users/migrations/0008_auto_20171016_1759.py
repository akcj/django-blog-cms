# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-16 17:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0007_auto_20171016_1754'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='create_date',
            field=models.DateTimeField(auto_now_add=True, verbose_name='\u521b\u5efa\u65f6\u95f4'),
        ),
    ]
