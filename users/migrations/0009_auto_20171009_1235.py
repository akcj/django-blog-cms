# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-09 12:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0008_auto_20171009_1131'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='user',
        ),
        migrations.AddField(
            model_name='article',
            name='user_id',
            field=models.IntegerField(default=0, editable=False, verbose_name='\u4f5c\u8005'),
        ),
    ]
