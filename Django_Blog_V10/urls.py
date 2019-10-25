"""Django_Blog_V10 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.views.static import serve
from django.conf.urls.static import static

import xadmin
from blog import views
from Django_Blog_V10 import settings

urlpatterns = [
    url(r'mdeditor/', include('mdeditor.urls')),
    # 后台路由
    url(r'^xadmin/', xadmin.site.urls),
    # 首页路由
    url(r'^$', views.index),
    # 查看文章详情
    url(r'detail/(?P<id>\d+)/$', views.get_blog_detail),
    # 根据分类查看文章路径
    url(r'cate/(?P<name>\w+)/$', views.get_cate),
    # 关于我url
    url(r'about/$', views.about),
    # 归档
    url(r'archives/$', views.archives),
    # 显示图片路径
    url(r'media/(?P<path>.*)', serve, {'document_root': settings.MEDIA_ROOT}),
]
