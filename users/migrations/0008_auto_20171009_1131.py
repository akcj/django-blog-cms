# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-09 11:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0007_auto_20171009_1125'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='user',
            field=models.CharField(default='\u673d\u5c0f\u8717', editable=False, max_length=64),
        ),
    ]