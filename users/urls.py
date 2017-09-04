from django.conf.urls import url
from .views import *
urlpatterns = [
    
    url(r'^reg/$',do_reg, name='do_reg'),
]