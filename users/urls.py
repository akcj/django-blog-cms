from django.conf.urls import url
from .views import *
urlpatterns = [
    
    url(r'^captcha/$',captcha, name='captcha'),
    url(r'^user/login/$',login, name='login'),
    url(r'^user/register/$',register, name='register'),
]