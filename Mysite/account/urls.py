from django.contrib.auth.context_processors import auth
from django.contrib.auth.views import LogoutView
from django.urls import path
from django.contrib.auth import views as auth_views

from . import views
app_name = 'account'
urlpatterns = [
    # path('login/', views.user_login, name='user_login'),
    # 使用Django内置的登陆/登出视图(类视图)
    path('login/', auth_views.LoginView.as_view(template_name='account/login2.html'), name='user_login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='account/logout.html'), name='user_logout'),
    path('register/', views.register, name='user_register'),
]
