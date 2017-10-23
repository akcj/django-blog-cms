#-*- coding:utf-8 -*-
from django.utils.translation import ugettext, ugettext_lazy as _
from django import forms
from .models import *
from django.contrib.auth.forms import ReadOnlyPasswordHashField,AuthenticationForm
from django.contrib.auth import (
    authenticate, get_user_model, password_validation,
)
from django.contrib import auth
# class RegisterForm(forms.Form):
#     '''
#     注册 
#     '''
#     nickname = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "请输入昵称", "value": "", "required": "required",}),  
#                               max_length=50,error_messages={"required": "用户名不能为空",})   
#     email = forms.EmailField(widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "请输入邮箱账号", "value": "", "required": "required",}),  
#                               max_length=50,error_messages={"required": "用户名不能为空",})  
#     password = forms.CharField(widget=forms.PasswordInput(attrs={"class": "form-control", "placeholder": "请输入密码", "value": "", "required": "required",}),  
#                               min_length=8, max_length=50,error_messages={"required": "密码不能为空",})  
#     def clean(self): 
#      # 用户名  
#         try:            
#             email=self.cleaned_data['email']  
#         except Exception as e:  
#             print 'except: '+ str(e)  
#             raise forms.ValidationError(u"注册账号需为邮箱格式")

#         try:  
#             password=self.cleaned_data['password']  
#         except Exception as e:  
#             print 'except: '+ str(e)  
#             raise forms.ValidationError(u"请输入至少8位密码")

#         return self.cleaned_data

class LoginForm(forms.Form):
    '''
    登录 
    ''' 
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={"class": "form-control", "placeholder":u"请输入邮箱地址","required": True,}),  
        max_length=50,
        )  
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={"class": "form-control", "placeholder":u"请输入密码","required": True,}),  
        max_length=50,
        )
    code = forms.CharField(
        widget=forms.TextInput(attrs={"class": "form-control", "placeholder":u"请输入验证码","required": True,}),  
        max_length=50,
        )

    def clean(self):
        data = self.cleaned_data
        return data   
# class UserChangeForm(forms.ModelForm):
#     """A form for updating users. Includes all the fields on
#     the user, but replaces the password field with admin's
#     password hash display field.
#     """
#     password = ReadOnlyPasswordHashField(
#         label=_("Password"),
#         help_text=_(
#             "Raw passwords are not stored, so there is no way to see this "
#             "user's password, but you can change the password using "
#             "<a href=\"../password/\">this form</a>."
#         ),
#     )

#     email = forms.EmailField(
#         max_length=50,
#         disabled = True,
#         label=_("email address"),
#         help_text=u"发送邮件<a href=\"../email/\">修改邮箱</a>.",
#         )
 
#     class Meta:
#         model = User
#         #fields = ('email', 'password', 'date_of_birth', 'is_active', 'is_admin')
#         fields = '__all__'

#     def clean_password(self):
#         # Regardless of what the user provides, return the initial value.
#         # This is done here, rather than on the field, because the
#         # field does not have access to the initial value
#         return self.initial["password"]

#     def clean_email(self):
#         # Regardless of what the user provides, return the initial value.
#         # This is done here, rather than on the field, because the
#         # field does not have access to the initial value
#         return self.initial["email"]

# class UserCreationForm(forms.ModelForm):
#     """
#     A form that creates a user, with no privileges, from the given username and
#     password.
#     """
#     error_messages = {
#         'password_mismatch': _("The two password fields didn't match."),
#     }

#     email = forms.EmailField(
#         label=_("email address"),
#         #strip=False,
#         widget=forms.TextInput(attrs={'autofocus': True}),
#         help_text=u'必填。',
#     )
#     password1 = forms.CharField(
#         label=_("Password"),
#         strip=False,
#         widget=forms.PasswordInput,
#         help_text=password_validation.password_validators_help_text_html(),
#     )
#     password2 = forms.CharField(
#         label=_("Password confirmation"),
#         widget=forms.PasswordInput,
#         strip=False,
#         help_text=_("Enter the same password as before, for verification."),
#     )

#     class Meta:
#         model = User
#         fields = ("username",)
#         #field_classes = {'username': uernameField}

#     def __init__(self, *args, **kwargs):
#         super(UserCreationForm, self).__init__(*args, **kwargs)
#         if self._meta.model.USERNAME_FIELD in self.fields:
#             self.fields[self._meta.model.USERNAME_FIELD].widget.attrs.update({'autofocus': True})

#     def clean_password2(self):
#         password1 = self.cleaned_data.get("password1")
#         password2 = self.cleaned_data.get("password2")
#         if password1 and password2 and password1 != password2:
#             raise forms.ValidationError(
#                 self.error_messages['password_mismatch'],
#                 code='password_mismatch',
#             )
#         self.instance.username = self.cleaned_data.get('username')
#         password_validation.validate_password(self.cleaned_data.get('password2'), self.instance)
#         return password2

#     def save(self, commit=True):
#         user = super(UserCreationForm, self).save(commit=False)
#         user.set_password(self.cleaned_data["password1"])
#         if commit:
#             user.save()
#         return user

# class AdminEmailChangeForm(forms.Form):
#     """
#     A form used to change the password of a user in the admin interface.
#     """
#     error_messages = {
#         'Email_mismatch':u"两次邮箱地址不一致！",
#     }
#     required_css_class = 'required'
#     email1 = forms.EmailField(
#         max_length=100,
#         label=u"邮箱地址",
#         widget=forms.TextInput(attrs={'autofocus': True}),
        
#     )
#     email2 = forms.EmailField(
#         label=u"重复邮箱地址",
#         widget=forms.TextInput(attrs={'autofocus': True}),
#         help_text=u"为了校验，请输入与上面相同的邮箱地址。",
#     )

#     def __init__(self, user, *args, **kwargs):
#         self.user = user
#         super(AdminEmailChangeForm, self).__init__(*args, **kwargs)

#     def clean_email2(self):
#         email1 = self.cleaned_data.get('email1')
#         email2 = self.cleaned_data.get('email2')
#         if email1 and email2:
#             if email1 != email2:
#                 raise forms.ValidationError(
#                     self.error_messages['Email_mismatch'],
#                     code='Email_mismatch',
#                 )
#         #password_validation.validate_password(password2, self.user)
#         return email2

#     def save(self, commit=True):
#         """
#         Saves the new password.
#         """
#         email = self.cleaned_data["email1"]
#         self.user.email = email
#         if commit:
#             self.user.save()
#         return self.user

#     @property
#     def changed_data(self):
#         data = super(AdminEmailChangeForm, self).changed_data
#         for name in self.fields.keys():
#             if name not in data:
#                 return []
#         return ['email']

class RegisterForm(forms.Form):
    nickname = forms.CharField(
        label=(u"账号"),
        max_length=10,
        error_messages={"required": u"账号不能为空",'max_length':u'用户名长度不能超过30',},
        widget=forms.TextInput(attrs={"placeholder": u"用户名","size":"20","class":"form-control",}),
        help_text=u"请输入您的别名!",
        )

    email = forms.EmailField(
        label=(u"邮箱"),
        widget=forms.TextInput(attrs={"placeholder": u"邮箱","size":"20","class":"form-control",}),
        error_messages={"required": u"email不能为空",'invalid':u"邮箱格式错误"}
        )
    
    password1 = forms.CharField(
        label=(u"密码"),
        widget=forms.PasswordInput(attrs={"placeholder": u"密码","size":"20","class":"form-control",}), 
        max_length=30,
        min_length=8, 
        error_messages={"required": u"密码不能为空",'min_length':u'用户名长度不能小于8','max_length':u'用户名长度不能超过30',}
        )

    password2 = forms.CharField(
        max_length=30,
        min_length=8, 
        label=(u"重复密码"),
        widget=forms.PasswordInput(attrs={"placeholder": u"重复密码","size":"20","class":"form-control",}), 
        error_messages={"required": u"密码不能为空",'min_length':u'用户名长度不能小于8','max_length':u'用户名长度不能超过30',}
        )

    # class Meta:
    #     model = User
    #     fields = ['nickname', 'email', 'password']

    # def clean_nickname(self):
    #     '''验证昵称'''
    #     nickname = User.objects.filter(nickname__iexact=self.cleaned_data["nickname"])
    #     if not nickname:
    #         return self.cleaned_data["nickname"]
    #     raise forms.ValidationError(u"该昵称已经被使用")

    # def clean_email(self):
    #     '''验证email'''
    #     email = User.objects.filter(email__iexact=self.cleaned_data["email"])
    #     if not email:
    #         return self.cleaned_data["email"]
    #     raise forms.ValidationError(u"该邮箱已经被使用")
    
    # def clean_password2(self):
    #     '''验证密码'''
    #     password1 = self.cleaned_data.get("password1")
    #     password2 = self.cleaned_data.get("password2")
    #     if password1 and password2 and password1 != password2:
    #         raise forms.ValidationError(u"两次密码输入不一致！")
    #     return password2

    # def clean(self):
    #     return self.cleaned_data
        
#     

