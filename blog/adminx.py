#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2019-07-13 19:07
# @Author  : Tanheyi
# @Email   : Tanheyii@gamil.com
# @File    : adminx.py
# @Software: PyCharm

import xadmin
from xadmin import views
from blog import models


# X admin的全局配置信息设置
class BaseSetting(object):
    # 主题功能开启
    enable_themes = True
    use_bootswatch = True


# X admin全局设置 设置后台标题和页脚显示信息
class GlobalConfig:
    site_title = "谈何易!的博客后台"
    site_footer = "谈何易!"


# 设置Host在后台的显示信息
class HostInfoConfig:
    # 后台显示字段
    list_display = ['name', 'email', 'detail']
    # 搜索字段
    search_fields = ['name', 'email', 'detail']
    # 排序字段
    list_filter = ['name', 'email', 'detail']


class BlogConfig:
    list_display = ['title', 'cate', 'watch', 'create_time']
    search_fields = ['title', 'cate', 'watch']
    list_filter = ['title', 'cate', 'watch', 'create_time']


xadmin.site.register(models.HostInfo, HostInfoConfig)
xadmin.site.register(models.Blog, BlogConfig)
xadmin.site.register(models.Cate)
xadmin.site.register(models.Tag)
xadmin.site.register(views.BaseAdminView, BaseSetting)
xadmin.site.register(views.CommAdminView, GlobalConfig)

