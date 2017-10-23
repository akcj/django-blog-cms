# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect,JsonResponse
from .models import *
from .forms import RegisterForm,LoginForm
from django.contrib.auth.forms import ReadOnlyPasswordHashField,AuthenticationForm
from django.contrib.auth import (
    authenticate, get_user_model, password_validation,
)    
import json
from django.contrib import auth
# def do_reg(request):
#     try:
#         if request.method == 'POST':
#             reg_form = RegForm(request.POST,request.FILES)
#             if reg_form.is_valid():
#                 reg_data = reg_form.cleaned_data
#                 username = reg_data['username']
#                 email = reg_data['email']
#                 password = reg_data['password2']
#                 user = CmsUser.objects.create_user(
#                     password = password,
#                     username = username,
#                     email = email,
#                     )
#                 user.set_password(password)
#                 user.save()
#                 #return HttpResponse(reg_info)
#         else:
#             reg_form = RegForm()

#     except Exception as e:
#         print e
#     return render(request, 'user/reg.html', {"form":reg_form,})


from DjangoCaptcha import Captcha


def login(request):
    #return HttpResponse(request)
    try:
        if request.method == 'POST':
            email = request.POST['email']
            password = request.POST['password']
            user = auth.authenticate(email=email, password=password)
            if user is not None and user.is_active:
                auth.login(request, user)
            # Redirect to a success page.
            return HttpResponseRedirect("/admin")

    except Exception as e:
        print e
    return render(request, 'user/login.html',) 

def register(request):
    try:
        if request.method == 'POST':
            nickname = request.POST['nickname']
            email = request.POST['email']
            password = request.POST['password']
            User.objects.create_user(nickname=nickname,password=password,email=email)
    except Exception as e:
        print e
    return render(request, 'user/register.html')     



#验证，提交的验证码是否正确  
def verifyAjax(request):  
    result = 'false'  
    _code = request.GET.get('code') or ''
    #return HttpResponse(_code)
    if not _code:  
        return HttpResponse(json.dumps([result]), content_type='application/json')  
    ca = Captcha(request)  
    if ca.check(_code):  
        result = 'true'  
    else:  
        result = 'false'  
    return HttpResponse(json.dumps([result]), content_type='application/json')  

#ajax验证昵称是否被注册
def nicknameAjax(request):
    nickname = request.GET.get('nickname')
    user = User.objects.filter(nickname=nickname)
    if user:
        result = False
    else:
        result = True
    return JsonResponse({'valid': result})

#ajax验证邮箱是否被注册
def emailAjax(request):
    email = request.GET.get('email')
    user = User.objects.filter(email=email)
    if user:
        result = False
    else:
        result = True
    return JsonResponse({'valid': result}) 