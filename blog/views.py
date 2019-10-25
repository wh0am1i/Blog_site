from django.shortcuts import render, HttpResponse
from django.views.decorators.cache import cache_page
from django.db.models import Count
from django.db.models import F
from django.http import JsonResponse
from blog import models
from django import forms
from utils.pagination import Pagination
import markdown


# 首页加载数据
def index(request):
    # 从请求中过去页码，如果没有获取到默认显示第一页
    current_page = int(request.GET.get('page', 1))
    # 总数据量
    total_count = models.Blog.objects.count()
    # 生成实例，传入当前页码，总数据量，路径
    page_obj = Pagination(current_page, total_count, request.path_info)
    # 数据显示开始行数 结束行数
    data = models.Blog.objects.all()[page_obj.start:page_obj.end]
    # 生成前端代码
    page_html = page_obj.page_html()
    # 返回渲染
    return render(request, "index.html", locals())


# 查看指定分类下的所有文章
def get_cate(request, name):
    # 从请求中过去页码，如果没有获取到默认显示第一页
    current_page = int(request.GET.get('page', 1))
    # 总数据量
    total_count = models.Blog.objects.filter(cate__blog__cate__name=name).distinct().count()
    # 生成实例，传入当前页码，总数据量，路径
    page_obj = Pagination(current_page, total_count, request.path_info)
    # 数据显示开始行数 结束行数
    cate_blog = models.Blog.objects.filter(cate__blog__cate__name=name).distinct()[page_obj.start:page_obj.end]
    # 生成前端代码
    page_html = page_obj.page_html()
    # 返回渲染
    return render(request, 'cate_detail.html', locals())


# 查看文章详细内容
def get_blog_detail(request, id):
    # 防止与原来的数据冲突，
    try:
        # 根据传入的ID获取信息
        blog_detail = models.Blog.objects.get(id=id)
        blog_detail.content = markdown.markdown(blog_detail.content, extensions=[
            'markdown.extensions.extra',
        ])
    except Exception:
        blog_detail = models.Blog.objects.get(id=id)
    # 访问一次访问量加1
    models.Blog.objects.filter(id=id).update(watch=F('watch')+1)
    # 校验对象
    return render(request, 'detail.html', {'blog_detail': blog_detail})


# 关于我
def about(request):
    author_info = models.HostInfo.objects.all()
    return render(request, 'about.html', locals())


def archives(request):
    # 按日期归档
    archive_list = models.Blog.objects.all()
    print(archive_list)
    return render(request, 'archive.html', locals())


