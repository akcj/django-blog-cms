# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-31 15:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CmsUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('username', models.CharField(db_index=True, max_length=32, unique=True, verbose_name='\u7528\u6237\u540d')),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='\u90ae\u7bb1')),
                ('nickname', models.CharField(blank=True, max_length=50, verbose_name='\u6635\u79f0')),
                ('sex', models.SmallIntegerField(choices=[(0, '\u4fdd\u5bc6'), (1, '\u7537'), (2, '\u5973')], default=0, verbose_name='\u6027\u522b')),
                ('birth', models.DateTimeField(blank=True, null=True, verbose_name='\u751f\u65e5')),
                ('create_date', models.DateField(auto_now=True, verbose_name='\u521b\u5efa\u65f6\u95f4')),
                ('login_date', models.DateField(verbose_name='\u4e0a\u6b21\u767b\u5f55\u65f6\u95f4')),
                ('is_active', models.BooleanField(default=True)),
                ('is_admin', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name': '\u7528\u6237',
                'verbose_name_plural': '\u7528\u6237',
            },
        ),
    ]