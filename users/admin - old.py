# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django import forms
from django.urls import reverse
from django.contrib import admin,messages
from django.contrib.auth import update_session_auth_hash
from django.http import Http404, HttpResponseRedirect
from django.conf.urls import url
from django.contrib.admin.utils import unquote
from django.utils.translation import ugettext, ugettext_lazy as _
from django.utils.html import escape
from django.contrib.admin.options import IS_POPUP_VAR
from django.template.response import TemplateResponse
from django.contrib.auth.models import Group,Permission
from django.contrib.auth.admin import UserAdmin as UserBaseAdmin
from django.contrib.auth.admin import GroupAdmin 
from django.contrib.auth.forms import ReadOnlyPasswordHashField
# Register your models here.
from .models import User
from django.utils.decorators import method_decorator
from django.views.decorators.debug import sensitive_post_parameters

from users.forms import AdminEmailChangeForm,UserChangeForm

sensitive_post_parameters_m = method_decorator(sensitive_post_parameters())

# class UserCreationForm(forms.ModelForm):
#     password1 = forms.CharField(label='密码', widget=forms.PasswordInput)
#     password2 = forms.CharField(label='重复密码', widget=forms.PasswordInput)
#     class Meta:
#         model = CmsUser
#         fields = ('username','email',)
#     def clean_password2(self):
#         # Check that the two password entries match
#         password1 = self.cleaned_data.get("password1")
#         password2 = self.cleaned_data.get("password2")
#         if password1 and password2 and password1 != password2:
#             raise forms.ValidationError("Passwords don't match")
#         return password2
#     def save(self, commit=True):
#         # Save the provided password in hashed format
#         user = super(UserCreationForm, self).save(commit=False)
#         user.set_password(self.cleaned_data["password1"])
#         if commit:
#             user.save()
#         return user

class UserAdmin(UserBaseAdmin):
    form = UserChangeForm
    list_display = ('username', 'email','nickname','sex','telephone','birth','create_date','last_login','is_active',)
    list_filter = ('create_date',)
    
    fieldsets = (
        (None, {'fields': ('password','email')}),
        (U'个人信息', {'fields': ('avatar','nickname','sex','birth')}),
        ('权限', {'fields': ( 'is_active','groups',)}),
    )
    add_fieldsets = (
        (U'添加用户', {
            'classes': ('wide',),
            'fields': ('username', 'password1', 'password2')}
         ),
    )
    search_fields = ('username','email',)
    ordering = ('-id',)
    # = ('groups',)
    filter_horizontal = ('groups','user_permissions',)

    def get_queryset(self, request):
        qs = super(UserAdmin, self).get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(author=request.user)

    def get_urls(self):
        return [
            url(
                r'^(.+)/password/$',
                self.admin_site.admin_view(self.user_change_password),
                name='auth_user_password_change',
            ),
            url(
                r'^(.+)/email/$',
                self.admin_site.admin_view(self.user_change_email),
                name='auth_user_email_change',
            ),

        ] + super(UserAdmin, self).get_urls()

    @sensitive_post_parameters_m
    def user_change_email(self, request, id, form_url=''):
        if not self.has_change_permission(request):
            raise PermissionDenied
        user = self.get_object(request, unquote(id))
        if user is None:
            raise Http404(_('%(name)s object with primary key %(key)r does not exist.') % {
                'name': force_text(self.model._meta.verbose_name),
                'key': escape(id),
            })
        if request.method == 'POST':
            form = AdminEmailChangeForm(user, request.POST)
            if form.is_valid():
                form.save()
                change_message = self.construct_change_message(request, form, None)
                self.log_change(request, user, change_message)
                msg = ugettext(u'邮箱地址修改成功！')
                messages.success(request, msg)
                update_session_auth_hash(request, form.user)
                return HttpResponseRedirect(
                    reverse(
                        '%s:%s_%s_change' % (
                            self.admin_site.name,
                            user._meta.app_label,
                            user._meta.model_name,
                        ),
                        args=(user.pk,),
                    )
                )
        else:
            form = AdminEmailChangeForm(user)

        fieldsets = [(None, {'fields': list(form.base_fields)})]
        adminForm = admin.helpers.AdminForm(form, fieldsets, {})

        context = {
            'title': (u'修改邮箱: %s') % escape(user.get_username()),
            'adminForm': adminForm,
            'form_url': form_url,
            'form': form,
            'is_popup': (IS_POPUP_VAR in request.POST or
                         IS_POPUP_VAR in request.GET),
            'add': True,
            'change': False,
            'has_delete_permission': False,
            'has_change_permission': True,
            'has_absolute_url': False,
            'opts': self.model._meta,
            'original': user,
            'save_as': False,
            'show_save': True,
        }
        context.update(self.admin_site.each_context(request))

        request.current_app = self.admin_site.name

        return TemplateResponse(
            request,
            'admin/auth/user/change_email.html',
            context,
        )
admin.site.register(User,UserAdmin)
#admin.site.register(Group,GroupAdmin)