from django.contrib import admin

from .models import BlogArticles


class BlogArticlesAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publish')  # 控制显示字段
    list_filter = ('publish', 'author')  # 过滤字段
    search_fields = ('title', 'body')  # 搜索字段
    raw_id_fields = ('author', )
    date_hierarchy = 'publish'  # 日期归档
    ordering = ['-publish', 'author']  # 排序


admin.site.register(BlogArticles, BlogArticlesAdmin)
