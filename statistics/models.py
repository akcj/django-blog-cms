# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils import timezone
# Create your models here.
#标签模型
class Statistic(models.Model):  
    url  = models.CharField(max_length=30, verbose_name='受到访问页面')  
    ip   = models.CharField(verbose_name='访问ip',max_length=30)
    start_time = models.DateTimeField(verbose_name='访问时间')
    end_time = models.DateTimeField(verbose_name='离开时间')
    class Meta:  
        verbose_name = '统计'  
        verbose_name_plural = verbose_name  
        ordering = ['sort']

    def __unicode__(self):  
        return self.name  