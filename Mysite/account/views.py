from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login

from .forms import LoginForm, ResgitrationForm


def user_login(request):
    if request.method == 'POST':
        login_form = LoginForm(request.POST)
        if login_form.is_valid():  # 效验数据是否合法
            cd = login_form.cleaned_data  # 取出POST中提交的数据(字典形式)
            user = authenticate(
                username=cd['username'], password=cd['password'])  # 用户认证
            if user:  # 认证通过返回实例对象
                login(request, user)  # 进行登录
                return HttpResponseRedirect(reverse('blog'))  # 认证成功后重定向到主页
            else:  # 不通过返回None
                return HttpResponse("Sorry. Your username or password is not right.")
        else:
            return HttpResponse('Invalid login')

    if request.method == 'GET':
        login_form = LoginForm()
        return render(request, 'account/login.html', {"form": login_form})


def register(request):
    if request.method == 'POST':
        user_form = ResgitrationForm(request.POST)
        if user_form.is_valid():
            new_user = user_form.save(commit=False)  # 生成数据对象(并没有保存到数据库)
            new_user.set_password(user_form.cleaned_data['password'])  # 设置密码
            new_user.save()
            return HttpResponse('successfully')
        else:
            return HttpResponse('Sorry, your can not register.')
    else:
        user_form = ResgitrationForm()
        return render(request, 'account/register.html', {'form': user_form})
