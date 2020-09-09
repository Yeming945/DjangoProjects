from django.urls import path

from . import views

urlpatterns = [
    path('', views.blog_title, name='blog_title'),

]
