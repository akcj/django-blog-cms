# coding: utf-8
import xadmin
from .models import *

from xadmin.views import BaseAdminView, CommAdminView


class GlobalSetting(object):
    # 给xadmin后台加上一个站名
    site_title  = 'aaaaa'
    # 给xadmin后台footer部分加一个名称
    site_footer = 'bbbb'
    # 让xadmin后台的各种菜单可折叠
    menu_style  = 'accordion'


class BaseSetting(object):
    # 打开主题
    enable_themes = True
    # 启用更多主题选项
    use_bootswatch = True

# class UserAdmin(object):

#     # 在后台中显示的字段
#     list_display = ('', '', )

#     # 给字段加上搜索功能
#     search_fields = ('', '', )

    #     # 给字段加上过滤显示
#     list_filter = ('', '', )


# xadmin.site.register(User, UserAdmin)

