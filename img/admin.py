# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from img.models import Imgs,ImgsTag
from users.models import User
from django.http import HttpResponse
from img.upload import delete_image_to_qiniu
from django.db.models.signals import post_delete
from django.utils.safestring import mark_safe
from django.conf import settings
# Register your models here.
class ImgsAdmin(admin.ModelAdmin):
    list_display = ['id','image_img','title','nickname','upload_date']
    list_filter = ['upload_date']
    # 删除对象后删除七牛云的图片资源
    def delete_file(sender,instance,**kwargs):
        url = 'media/'+str(instance.img_url)
        delete_image_to_qiniu(url)

    post_delete.connect(delete_file,sender=Imgs)

    # 图片展示
    def image_img(self,obj):
        if obj:
            return mark_safe('<img src="%s" />' % (settings.MEDIA_URL+str(obj.img_url)+settings.IMG_THUMB))
        else:
            return '(no image)'
 
    image_img.short_description = '缩略图'
    #超级用户则展示全部，非超级用户只展示和登录用户相关的信息
    # def get_queryset(self,request):
    #     qs = super(ImgsAdmin,self).get_queryset(request)
    #     if request.user.is_superuser:
    #         return qs
    #     #此处user为当前model的related object的related object， 正常的外键只要filter(user=request.user)
    #     return qs.filter(user_id=request.user.id)

    def save_model(self, request, obj, form, change):
        if not obj.id:
            obj.user_id = request.user.id
        obj.save()   

    def nickname(self,obj):
        return User.objects.get(id=obj.user_id).nickname
    nickname.short_description = u'作者'
        
admin.site.register(Imgs,ImgsAdmin)
admin.site.register(ImgsTag)