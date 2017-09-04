# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from .forms import RegForm
    

def do_reg(request):
    try:
        if request.method == 'POST':
            reg_form = RegForm(request.POST)
            if reg_form.is_valid():
                
                reg_info = reg_form.cleaned_data 
                #username = reg_form.cleaned_data.get("username")
                #email = reg_info['email']
                #password = reg_info['password2']
                print username
                return HttpResponse(username)
                user = CmsUser.objects.create_user(
                    username=username,
                    email=email,
                    password=password)
                user.set_password(reg_info["password2"])
                user.save()
                #return HttpResponse(reg_info)
        else:
            reg_form = RegForm()

    except Exception as e:
        print e
    return render(request, 'user/reg.html', {"form":reg_form,})
