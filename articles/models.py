# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.core.urlresolvers import reverse
from django.utils import timezone
from simditor.fields import RichTextField

#文章标签模型
class Tag(models.Model):  
    name = models.CharField(max_length=30, verbose_name='标签名称')  
    sort = models.SmallIntegerField(verbose_name='分类排序',default=1)

    class Meta:  
        verbose_name = '标签'  
        verbose_name_plural = verbose_name  
        ordering = ['sort']

    def __unicode__(self):  
        return self.name  

#文章分类模型
class Category(models.Model):
    name = models.CharField(max_length=30, verbose_name='分类名称') #分类名称 
    sort = models.SmallIntegerField(verbose_name='分类排序',default=1)  #排序 
    pid = models.ForeignKey('self', blank=True, null=True,verbose_name='父级评论')

    class Meta:  
        verbose_name = '分类'  
        verbose_name_plural = verbose_name  
        ordering = ['sort']

    def __unicode__(self):  
        return self.name 

# Create your models here.
class Article(models.Model):
    # 文章发布状态
    CONTENT_STATUS_PUBLISHED = 1
    # 文章草稿箱状态
    CONTENT_STATUS_DRAFT = 2
    # 文章状态选项
    CONTENT_STATUS_CHOICES = (
        (CONTENT_STATUS_PUBLISHED, '发布'),
        (CONTENT_STATUS_DRAFT, '草稿箱'),
    )
    
    IMG_IS_SHOW = (
        (1, '展示'),
        (0, '不展示'),
    )

    title = models.CharField(verbose_name ='标题', max_length=100)
    user_id = models.IntegerField(default=0,verbose_name ='作者',editable=False)
    img = models.ImageField(upload_to='article/',verbose_name='首页展示图片')
    img_is_centent_show = models.SmallIntegerField(verbose_name='首页图片是否在文章顶端展示', default=0, choices=IMG_IS_SHOW)
    desc = models.TextField(verbose_name ='摘要',blank=True)
    content = RichTextField(verbose_name ='文章内容')
    categories = models.ForeignKey(Category,verbose_name ='分类')
    tags = models.ManyToManyField(Tag, blank=True,
                                        verbose_name = '标签'
                                        )
    published_date = models.DateTimeField(verbose_name ='发布时间',blank=True, null=True)    # 发表时间
    status = models.IntegerField(verbose_name ='状态',
                                 choices=CONTENT_STATUS_CHOICES,
                                 default=CONTENT_STATUS_PUBLISHED)      # 状态：1为正式发布，2为草稿箱
    comments_count = models.IntegerField(verbose_name ='评论数',default=0)     # 评论总数
    view_count = models.IntegerField(verbose_name ='浏览数',default=0)         # 浏览总数
    like_count = models.IntegerField(verbose_name ='喜欢数',default=0)
    collection_count = models.IntegerField(verbose_name ='收藏数',default=0)

    # objects = ArticleManager()

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def get_absolute_url(self):
        return reverse('article',args=[self.pk])
    
    class Meta:
        verbose_name = '文章'
        verbose_name_plural = '文章'
        ordering = ['-published_date']

    def __unicode__(self):
        return self.title

    
        