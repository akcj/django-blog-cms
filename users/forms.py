#-*- coding:utf-8 -*-
from django import forms
from .models import *

# class RegForm(forms.Form):
#     username = forms.CharField(
#         label=(u"账号"),
#         max_length=30,
#         min_length=6,
#         error_messages={"required": u"账号不能为空",'min_length':u'用户名长度不能小于6','max_length':u'用户名长度不能超过30',},
#         widget=forms.TextInput(attrs={"placeholder": u"用户名","size":"20","class":"form-control",}),
#         help_text=u"请输入您的别名!",
#         )

#     email = forms.EmailField(
#         label=(u"邮箱"),
#         widget=forms.TextInput(attrs={"placeholder": u"邮箱","size":"20","class":"form-control",}),
#         error_messages={"required": u"email不能为空",'invalid':u"邮箱格式错误"}
#         )
    
#     password1 = forms.CharField(
#         label=(u"密码"),
#         widget=forms.PasswordInput(attrs={"placeholder": u"密码","size":"20","class":"form-control",}), 
#         max_length=30,
#         min_length=8, 
#         error_messages={"required": u"密码不能为空",'min_length':u'用户名长度不能小于8','max_length':u'用户名长度不能超过30',}
#         )

#     password2 = forms.CharField(
#         max_length=30,
#         min_length=8, 
#         label=(u"重复密码"),
#         widget=forms.PasswordInput(attrs={"placeholder": u"重复密码","size":"20","class":"form-control",}), 
#         error_messages={"required": u"密码不能为空",'min_length':u'用户名长度不能小于8','max_length':u'用户名长度不能超过30',}
#         )

#     class Meta:
#         model = CmsUser
#         fields = ['username', 'email', 'password']

#     def clean_username(self):
#         '''验证账号'''
#         username = CmsUser.objects.filter(username__iexact=self.cleaned_data["username"])
#         if not username:
#             return self.cleaned_data["username"];
#         raise forms.ValidationError(u"该昵称已经被使用");

#     def clean_email(self):
#         '''验证email'''
#         email = CmsUser.objects.filter(email__iexact=self.cleaned_data["email"])
#         if not email:
#             return self.cleaned_data["email"];
#         raise forms.ValidationError(u"该邮箱已经被使用");
    
#     def clean_password2(self):
#         '''验证密码'''
#         password1 = self.cleaned_data.get("password1")
#         password2 = self.cleaned_data.get("password2")
#         if password1 and password2 and password1 != password2:
#             raise forms.ValidationError(u"两次密码输入不一致！")
#         return password2

#     # def clean(self):
#     #     return self.cleaned_data
        
#     