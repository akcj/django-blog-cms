# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from articles.models import Article,Category,Tag
from users.models import User
from img.upload import delete_image_to_qiniu
from django.db.models.signals import post_delete
# Register your models here.
class ArticleAdmin(admin.ModelAdmin):
    list_display = ['title','nickname','published_date','status','comments_count','view_count',]
    list_filter = ['published_date']
    # 删除对象后删除七牛云的图片资源
    def delete_file(sender,instance,**kwargs):
        url = 'media/' + str(instance.img)
        delete_image_to_qiniu(url)

    post_delete.connect(delete_file,sender=Article)

    #超级用户则展示全部，非超级用户只展示和登录用户相关的信息
    def get_queryset(self,request):
        qs = super(ArticleAdmin,self).get_queryset(request)
        if request.user.is_superuser:
            return qs
        #此处user为当前model的related object的related object， 正常的外键只要filter(user=request.user)
        return qs.filter(user_id=request.user.id)

    def save_model(self, request, obj, form, change):
        if not obj.id:
            obj.user_id = request.user.id
        obj.save()   

    def nickname(self,obj):
        return User.objects.get(id=obj.user_id).nickname
    nickname.short_description = u'作者'
        
admin.site.register(Article,ArticleAdmin)
admin.site.register(Category)
admin.site.register(Tag)