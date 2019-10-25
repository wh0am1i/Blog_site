from django.db import models

from mdeditor.fields import MDTextField


class HostInfo(models.Model):
    """
    博主信息
    """
    name = models.CharField(max_length=64, verbose_name="姓名")
    email = models.EmailField(verbose_name="邮箱")
    head_img = models.ImageField(upload_to='head_img', verbose_name="头像")
    tag = models.ManyToManyField(to='Tag', verbose_name="标签")
    detail = MDTextField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '博主信息'
        verbose_name_plural = verbose_name


class Blog(models.Model):
    """
    博客内容
    """
    title = models.CharField(max_length=128, verbose_name="标题")
    intro = models.CharField(max_length=255, verbose_name="简介")
    content = MDTextField(verbose_name='编写文章')
    cate = models.ManyToManyField(to='Cate', verbose_name="分类")
    watch = models.IntegerField(verbose_name="访问次数")
    img = models.ImageField(upload_to="blog/%m-%d", default='default/default.jpeg')
    create_time = models.DateTimeField(verbose_name="创建时间", auto_now_add=True)

    class Meta:
        verbose_name = '博客列表'
        verbose_name_plural = verbose_name
        ordering = ['-create_time']

    def __str__(self):
        return self.title


class Cate(models.Model):
    """
    分类
    """
    name = models.CharField(max_length=64, verbose_name="分类")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '博客分类'
        verbose_name_plural = verbose_name


class Tag(models.Model):
    name = models.CharField(max_length=64, verbose_name="标签名称")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '个人标签'
        verbose_name_plural = verbose_name
