# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-29 16:39
from __future__ import unicode_literals

from django.db import migrations, models
import users.models
import users.validators


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0008_alter_user_username_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[users.validators.ASCIIUsernameValidator()], verbose_name='username')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('avatar', models.ImageField(default='default.png', max_length=200, upload_to='avatar/%Y/%m/%d', verbose_name='\u7528\u6237\u5934\u50cf')),
                ('nickname', models.CharField(blank=True, max_length=50, verbose_name='\u6635\u79f0')),
                ('profile', models.TextField(blank=True, max_length=200, null=True, verbose_name='\u4e2a\u4eba\u7b80\u4ecb')),
                ('sex', models.SmallIntegerField(choices=[(0, '\u4fdd\u5bc6'), (1, '\u7537'), (2, '\u5973')], default=0, verbose_name='\u6027\u522b')),
                ('telephone', models.CharField(blank=True, max_length=50, null=True, verbose_name='\u7535\u8bdd')),
                ('birth', models.DateField(blank=True, null=True, verbose_name='\u751f\u65e5')),
                ('create_date', models.DateField(auto_now=True, verbose_name='\u521b\u5efa\u65f6\u95f4')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'users',
                'verbose_name_plural': 'users',
            },
            managers=[
                ('objects', users.models.UserManager()),
            ],
        ),
    ]
