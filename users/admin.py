# -*- coding: utf-8 -*-
from __future__ import unicode_literals


from django.urls import reverse
from django.contrib import admin,messages
from django.http import Http404, HttpResponseRedirect
from django.conf.urls import url

from django.utils.translation import ugettext, ugettext_lazy as _
from django.template.response import TemplateResponse
from django.contrib.auth.models import Group,Permission
from django.contrib.auth.admin import UserAdmin as UserBaseAdmin
from django.contrib.auth.admin import GroupAdmin 
# Register your models here.
from .models import User
from users.forms import AdminEmailChangeForm,UserChangeForm,UserCreationForm



class UserAdmin(UserBaseAdmin):
    #form = UserChangeForm
    add_form = UserCreationForm
    list_display = ('username', 'email','nickname','sex','telephone','birth','create_date','last_login','is_active','is_staff','group_name',)
    list_filter = ('create_date','last_login',)
    
    fieldsets = (
        (None, {'fields': ('password','email')}),
        (U'个人信息', {'fields': ('avatar','nickname','sex','birth')}),
        ('权限', {'fields': ( 'is_active','is_staff','groups',)}),
    )
    add_fieldsets = (
        (U'添加用户', {
            'classes': ('wide',),
            'fields': ('username','email', 'password1', 'password2')}
         ),
    )
    #raw_id_fields = ("groups",)
    search_fields = ('username','email',)
    ordering = ('-id',)
    # = ('groups',)
    filter_horizontal = ('groups','user_permissions',)

    def group_name(self,obj):
        return obj.groups.name
    group_name.short_description = u'组别'

    def get_queryset(self, request):
        qs = super(UserAdmin, self).get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(author=request.user)

    def get_urls(self):
        return [
            url(
                r'^(.+)/password/$',
                self.admin_site.admin_view(self.user_change_password),
                name='auth_user_password_change',
            ),
            # url(
            #     r'^(.+)/email/$',
            #     self.admin_site.admin_view(self.user_change_email),
            #     name='auth_user_email_change',
            # ),

        ] + super(UserAdmin, self).get_urls()

    
admin.site.register(User,UserAdmin)
admin.site.register(Permission)
