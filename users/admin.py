# coding: utf-8
import xadmin
from .models import User

from xadmin.views import BaseAdminView, CommAdminView


class GlobalSetting(object):
    # 给xadmin后台加上一个站名
    site_title = '<site title>'
    # 给xadmin后台footer部分加一个名称
    site_footer = '<site footer>'
    # 让xadmin后台的各种菜单可折叠
    menu_style = 'accordion'


class BaseSetting(object):
    # 打开主题
    enable_themes = True
    # 启用更多主题选项
    use_bootswatch = True

class UserAdmin(object):

    # 在后台中显示的字段
    list_display = ('field1', 'field2', ......)

    # 给字段加上搜索功能
    search_fields = ('field1', 'field2', ......)

    # 给字段加上过滤显示
    list_filter = ('field1', 'field2', ......)


xadmin.site.register(User, UserAdmin)

