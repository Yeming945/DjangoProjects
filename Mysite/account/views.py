from cmath import log
from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from .forms import LoginForm


def user_login(request):
    if request.method == 'POST':
        login_form = LoginForm(request.POST)
        if login_form.is_valid():  # 效验数据是否合法
            cd = login_form.cleaned_data  # 取出POST中提交的数据(字典形式)
            user = authenticate(
                username=cd['username'], password=cd['password'])  # 用户认证
            if user:  # 认证通过返回实例对象
                login(request, user)  # 进行登录
                return HttpResponse('Wellcome You. You have been authenticated successfully')
            else:  # 不通过返回None
                return HttpResponse("Sorry. Your username or password is not right.")
        else:
            return HttpResponse('Invalid login')

    if request.method == 'GET':
        login_form = LoginForm()
        return render(request, 'account/login.html', {"form": login_form})
