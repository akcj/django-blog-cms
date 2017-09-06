# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from .models import *
#from .forms import RegForm
    

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
