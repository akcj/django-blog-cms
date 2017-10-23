from django.conf.urls import url
from .views import *
urlpatterns = [
    url(r'^verifyAjax/$',verifyAjax, name='verifyAjax'),
    url(r'^user/login/$',login, name='login'),
    url(r'^user/register/$',register, name='register'),
    url(r'^user/nicknameAjax/$',nicknameAjax, name='nicknameAjax'),
    url(r'^user/emailAjax/$',emailAjax, name='emailAjax'),
]