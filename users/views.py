# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from .forms import RegisterForm
    

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
    return HttpResponse('OK')

def register(request):
    try:
        if request.method == 'POST':

            reg_form = RegisterForm(request.POST)
            #return HttpResponse(reg_form)
            if reg_form.is_valid():
                return HttpResponse(1)
                reg_data = reg_form.cleaned_data
                
                nickname = reg_data['nickname']
                email = reg_data['email']
                password = reg_data['password2']
                user = CmsUser.objects.create_user(
                    password = password,
                    nickname = nickname,
                    email = email,
                    )
                user.set_password(password)
                user.save()
                #return HttpResponse(reg_info)
        else:
            reg_form = RegisterForm()

    except Exception as e:
        print e
    return render(request, 'user/rege.html', {"form":reg_form,})     
def captcha(request):
    ca =  Captcha(request)
    #ca.words = ['1111','2222','3333']
    ca.mode = 'word'
    ca.img_width    = 100
    ca.img_height   = 30
    return ca.display()


#验证，提交的验证码是否正确  
def verifyAjax(request):  
    result = 'false'  
    _code = request.GET.get('code') or ''
    return HttpResponse(_code)
    if not _code:  
        return HttpResponse(json.dumps([result]), content_type='application/json')  
    ca = Captcha(request)  
    if ca.check(_code):  
        result = 'true'  
    else:  
        result = 'false'  
    return HttpResponse(json.dumps([result]), content_type='application/json')  