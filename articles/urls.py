from django.conf.urls import url,include
from .views import *
urlpatterns = [
    url(r'^page/(?P<page>[0-9]*)/$', article_list_all, name='article_list_all'),
    url(r'^cat/(?P<cat>[0-9]*)/page/(?P<page>[0-9]*)/$', article_list_by_category, name='article_list_by_category'),
    url(r'^simditor/', include('simditor.urls'))   # add this line
    #url(r'^reg/$',do_reg, name='do_reg'),
]