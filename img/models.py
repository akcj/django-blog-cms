# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils import timezone
# Create your models here.

#图片标签模型
class ImgsTag(models.Model):  
    name = models.CharField(max_length=30, verbose_name='标签名称')  
    sort = models.SmallIntegerField(verbose_name='分类排序',default=1)

    class Meta:  
        verbose_name = '标签'  
        verbose_name_plural = verbose_name  
        ordering = ['sort']

    def __unicode__(self):  
        return self.name  

class Imgs(models.Model):
    img_url = models.ImageField(upload_to='imgage/',verbose_name='图片')
    title = models.CharField(max_length=30,blank=True, null=True, verbose_name='标题')
    desc = models.TextField(verbose_name ='简单描述',blank=True, null=True)
    upload_date = models.DateTimeField(verbose_name ='上传时间',blank=True, null=True)
    tags = models.ManyToManyField(ImgsTag, blank=True,verbose_name = '图片标签')
    user_id = models.IntegerField(default=0,verbose_name ='作者',editable=False)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    class Meta:  
        verbose_name = '图片资源'  
        verbose_name_plural = verbose_name  

    def __unicode__(self):  
        return self.title 