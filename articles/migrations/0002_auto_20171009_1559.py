# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-09 15:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='collection_count',
            field=models.IntegerField(default=0, verbose_name='\u6536\u85cf\u6570'),
        ),
        migrations.AddField(
            model_name='article',
            name='like_count',
            field=models.IntegerField(default=0, verbose_name='\u559c\u6b22\u6570'),
        ),
    ]