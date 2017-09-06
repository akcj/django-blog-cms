# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django import forms
from django.contrib import admin
from django.contrib.auth.models import Group,Permission
from django.contrib.auth.admin import UserAdmin as UserBaseAdmin
from django.contrib.auth.forms import ReadOnlyPasswordHashField
# Register your models here.
from .models import User

# class UserCreationForm(forms.ModelForm):
#     password1 = forms.CharField(label='密码', widget=forms.PasswordInput)
#     password2 = forms.CharField(label='重复密码', widget=forms.PasswordInput)
#     class Meta:
#         model = CmsUser
#         fields = ('username','email',)
#     def clean_password2(self):
#         # Check that the two password entries match
#         password1 = self.cleaned_data.get("password1")
#         password2 = self.cleaned_data.get("password2")
#         if password1 and password2 and password1 != password2:
#             raise forms.ValidationError("Passwords don't match")
#         return password2
#     def save(self, commit=True):
#         # Save the provided password in hashed format
#         user = super(UserCreationForm, self).save(commit=False)
#         user.set_password(self.cleaned_data["password1"])
#         if commit:
#             user.save()
#         return user

class UserChangeForm(forms.ModelForm):
    password = ReadOnlyPasswordHashField(label=("密码"),
      help_text=("在这里，<a href=\"../password/\">重置密码</a>."))

    class Meta:
        model = User
        fields = ('password',)
    
    def clean_password(self):
        return self.initial["password"]

class UserAdmin(UserBaseAdmin):
    form = UserChangeForm
    #add_form = UserCreationForm
    list_display = ('username', 'email','nickname','sex','telephone','birth','create_date','last_login','is_active',)
    list_filter = ('is_admin','create_date',)
    
    fieldsets = (
        (None, {'fields': ('password',)}),
        ('个人信息', {'fields': ('avatar','nickname','sex','birth')}),
        ('权限', {'fields': ( 'is_active','groups','Permission',)}),
    )
    add_fieldsets = (
        ('添加用户', {
            'classes': ('wide',),
            'fields': ('username', 'password1', 'password2')}
         ),
    )
    search_fields = ('username','email',)
    ordering = ('-id',)
    # = ('groups',)
    filter_horizontal = ()

admin.site.register(User)
#admin.site.register(Group)