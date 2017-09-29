# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils import six, timezone
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser,PermissionsMixin,Group,Permission
from django.http import HttpResponse
from django.core.mail import send_mail
from .validators import ASCIIUsernameValidator, UnicodeUsernameValidator
import os

class UserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, username, email, password, **extra_fields):
        """
        Creates and saves a User with the given username, email and password.
        """
        if not username:
            raise ValueError(_('The given username must be set'))
        email = self.normalize_email(email)
        #username = self.username
        user = self.model(username=username, email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, username, email=None, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(username, email, password, **extra_fields)

    def create_superuser(self, username, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError(_('Superuser must have is_staff=True.'))
        if extra_fields.get('is_superuser') is not True:
            raise ValueError(_('Superuser must have is_superuser=True.'))

        return self._create_user(username, email, password, **extra_fields)

class User(AbstractBaseUser,PermissionsMixin):
    SEX_STATUS = (
        (0, u'保密'),
        (1, u'男'),
        (2, u'女'),
    )

    username_validator = UnicodeUsernameValidator() if six.PY3 else ASCIIUsernameValidator()

    username = models.CharField(
        _('username'),
        max_length=150,
        unique=True,
        help_text=_('Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.'),
        validators=[username_validator],
        error_messages={
            'unique': _("A user with that username already exists."),
        },
    )

    email = models.EmailField(_('email address'), blank=True,null=True)

    avatar = models.ImageField(max_length=200,upload_to='avatar/%Y/%m/%d' ,default='default.png', verbose_name=u'用户头像')
    nickname = models.CharField(verbose_name=u'昵称', max_length=50, blank=True)
    profile = models.TextField(max_length=200,verbose_name=u'个人简介',blank=True,null=True)
    sex = models.SmallIntegerField(verbose_name=u'性别', default=0, choices=SEX_STATUS)
    telephone = models.CharField(max_length=50,blank=True, null=True,verbose_name=u'电话')
    birth = models.DateField(blank=True, null=True,verbose_name =u'生日')
    create_date = models.DateTimeField(auto_now=True, verbose_name=u'创建时间')

    is_staff = models.BooleanField(
        _('staff status'),
        default=False,
        help_text=_('Designates whether the user can log into this admin site.'),
    )
    
    is_active = models.BooleanField(
        _('active'),
        default=True,
        help_text=_(
            'Designates whether this user should be treated as active. '
            'Unselect this instead of deleting accounts.'
        ),
    )

    objects = UserManager()

    EMAIL_FIELD = 'email'
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    class Meta:
        verbose_name = _('users')
        verbose_name_plural = _('users')

    def clean(self):
        super(User, self).clean()
        self.email = self.__class__.objects.normalize_email(self.email)

    def get_full_name(self):
        return self.username

    def get_short_name(self):
        return self.username

    def email_user(self, subject, message, from_email=None, **kwargs):
        send_mail(subject, message, from_email, [self.email], **kwargs)

    def __unicode__(self):              # __unicode__ on Python 2
        return self.username

    # def email_user(self, subject, message, from_email=None, **kwargs):
    #     send_mail(subject, message, from_email, [self.email], **kwargs)
# Create your models here.



