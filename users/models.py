# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, PermissionsMixin
from django.http import HttpResponse
import os
# Create your models here.
class CmsUserManager(BaseUserManager):
    """自定义用户管理器"""
    def create_user(self, username , password=None):
        if not username:
            raise ValueError('Users must have an username')

        user = self.model(
            username=username,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, password):

        user = self.create_user(username = username,
                                password=password,
                                )
        user.is_admin = True  # 比创建用户多的一个字段
        user.save(using=self._db)
        return user

class CmsUser(AbstractBaseUser,PermissionsMixin):

    SEX_STATUS = (
        (0, '保密'),
        (1, '男'),
        (2, '女'),
    )

    username = models.CharField(max_length=32, unique=True, db_index=True,verbose_name='用户名')
    avatar = models.ImageField(max_length=200,upload_to='avatar/%Y/%m/%d' ,default='default.png', verbose_name=u'用户头像')
    email = models.EmailField(unique=True,verbose_name='邮箱')
    nickname = models.CharField(verbose_name='昵称', max_length=50, blank=True)
    profile = models.TextField(max_length=200,verbose_name=u'个人简介',blank=True,null=True)
    sex = models.SmallIntegerField(verbose_name='性别', default=0, choices=SEX_STATUS)
    telephone = models.CharField(max_length=50,null=True,verbose_name='电话')
    birth = models.DateField(blank=True, null=True,verbose_name ='生日')
    create_date = models.DateTimeField(auto_now=True, verbose_name='创建时间')    
    is_active = models.BooleanField(default=True,verbose_name='是否启用')
    is_admin = models.BooleanField(default=False,verbose_name='是否为超级管理员')
    
    objects = CmsUserManager()

    USERNAME_FIELD = 'username'  #必须有一个唯一标识
    EMAIL_FIELD = 'email'
    #REQUIRED_FIELDS = ['email']  # 创建superuser时的必须字段

    def get_full_name(self):
        # The user is identified by their email address
        return self.nickname

    def get_short_name(self):
        # The user is identified by their email address
        return self.username

    def __str__(self):              # __unicode__ on Python 2
        return self.username

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True


    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin
        
    class Meta:
        verbose_name = '用户'
        verbose_name_plural = '用户'
        
    def __unicode__(self):
        return self.username