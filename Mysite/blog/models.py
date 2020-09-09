from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class BlogArticles(models.Model):
    title = models.CharField(max_length=300, verbose_name='文章标题')
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="blog_posts", verbose_name='作者')
    body = models.TextField(verbose_name='文章内容')
    publish = models.DateTimeField(default=timezone.now, verbose_name='发布时间')

    class Meta:
        ordering = ("-publish",)  # 以发布时间倒序排序

    def __str__(self):
        return self.title
