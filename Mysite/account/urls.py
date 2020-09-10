from django.contrib.auth.views import LogoutView, LoginView
from django.urls import path

from . import views
app_name = 'account'
urlpatterns = [
    # path('login/', views.user_login, name='user_login'),
    # 使用Django内置的登陆/登出视图(类视图)
    path('login/', LoginView.as_view(template_name='account/login2.html'),
         name='user_login'),
    path('logout/', LogoutView.as_view(template_name='account/logout.html'),
         name='user_logout'),
    path('register/', views.register, name='user_register'),
]
