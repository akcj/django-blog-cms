# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
from articles.models import *
from django.core.paginator import Paginator, InvalidPage, EmptyPage, PageNotAnInteger
from django.http import HttpResponse
# 分页处理
def get_page(request,lists,page):
    paginator = Paginator(plist, 1)  # 一页最多显示4篇文章
    try:
        lists = paginator.page(page)
        plist = paginator.page_range
    except (EmptyPage, InvalidPage, PageNotAnInteger):
        lists = paginator.page(1)  #出现异常就返回第一页
    return lists

def article_list_all(request,page):
    #return HttpResponse(cat)
    try:
        article_list = Article.objects.filter(status=1).values('id', 'title')
        #page = request.GET.get('page', 1)
        paginator = Paginator(article_list, 2)
        article_list = paginator.page(page)
        plist = paginator.page_range
    except Exception as e:
        logging.error(e)
    return render(request, 'art/list.html', {"article_list": article_list,'plist':plist,'page':page})

def article_list_by_category(request, cat, page):
    #return HttpResponse(cat)
    try:
        article_list = Article.objects.filter(categories=int(cat), status=1).values('id', 'title')
        #page = request.GET.get('page', 1)
        paginator = Paginator(article_list, 1)
        article_list = paginator.page(page)
        plist = paginator.page_range
    except Exception as e:
        logging.error(e)
    return render(request, 'art/list.html', {"article_list": article_list,'plist':plist,'page':int(page),'cat':cat})
"""
分页例子
curPage - 当前页
"""
def pageTest(request,curPage):
    try:
        lists = ['aa','bb','cc','dd']
        paginator = Paginator(lists, 2)  # 一页最多显示2条
        lists = paginator.page(page)
        pagelist = paginator.page_range #页码列表
    except (EmptyPage, InvalidPage, PageNotAnInteger):
        lists = paginator.page(1)  #出现异常就返回第一页
    
    return render(request, 'pageTest.html', {"lists": lists,'pagelist':pagelist,'curPage':curPage})

