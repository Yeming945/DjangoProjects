from django.shortcuts import render, get_object_or_404

from .models import BlogArticles


def blog_title(request):
    blogs = BlogArticles.objects.all()
    return render(request, 'blog/titles.html', {'blogs': blogs})


def blog_article(request, article_id):
    article = get_object_or_404(BlogArticles, id=article_id) # 避免访问出现不存在的ID值报错
    pub = article.publish
    return render(request, "blog/content.html", {"article": article, 'publish': pub})
