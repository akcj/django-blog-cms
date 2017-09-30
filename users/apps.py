# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _

class UsersConfig(AppConfig):
    name = 'users'
    verbose_name = u'用户管理'
    verbose_name_plural =u'用户管理'