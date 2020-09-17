from django.http import request
from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

from .forms import LoginForm, ResgitrationForm, UserProfileForm, UserInfoForm, UserForm
from .models import UserProfile, UserInfo


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
        userprofile_form = UserProfileForm(request.POST)
        if user_form.is_valid() and userprofile_form.is_valid():
            new_user = user_form.save(commit=False)  # 生成数据对象(并没有保存到数据库)
            new_user.set_password(user_form.cleaned_data['password'])  # 设置密码
            new_user.save()

            new_profile = userprofile_form.save(commit=False)
            new_profile.user = new_user
            new_profile.save()

            return HttpResponse('successfully')
        else:
            return HttpResponse('Sorry, your can not register.')
    else:
        user_form = ResgitrationForm()
        userprofile_form = UserProfileForm()
        return render(request, 'account/register.html', {'form': user_form, 'profile': userprofile_form})


@login_required
def myself(request):
    userprofile = UserProfile.objects.get(user=request.user) if hasattr(
        request.user, 'userprofile') else UserProfile.objects.create(user=request.user)
    userinfo = UserInfo.objects.get(user=request.user) if hasattr(
        request.user, 'userinfo') else UserInfo.objects.create(user=request.user)
    return render(request, 'account/myself.html', {'user': request.user, 'userinfo': userinfo, 'userprofile': userprofile})


@login_required(login_url='/account/login/')
def myself_edit(request):
    userprofile = UserProfile.objects.get(user=request.user) if hasattr(
        request.user, 'userprofile') else UserProfile.objects.create(user=request.user)
    userinfo = UserInfo.objects.get(user=request.user) if hasattr(
        request.user, 'userinfo') else UserInfo.objects.create(user=request.user)
    if request.method == 'POST':
        user_form = UserForm(request.POST)
        userprofile_form = UserProfileForm(request.POST)
        userinfo_form = UserInfoForm(request.POST)
        if user_form.is_valid() * userprofile_form.is_valid() * userinfo_form.is_valid():
            user_cd = user_form.cleaned_data
            userprofile_cd = userprofile_form.cleaned_data
            userinfo_cd = userinfo_form.cleaned_data
            request.user.email = user_cd['email']
            userprofile.birth = userprofile_cd['birth']
            userprofile.phone = userprofile_cd['phone']
            userinfo.school = userinfo_cd['school']
            userinfo.company = userinfo_cd['company']
            userinfo.profession = userinfo_cd['profession']
            userinfo.address = userinfo_cd['address']
            userinfo.aboutme = userinfo_cd['aboutme']
            request.user.save()
            userprofile.save()
            userinfo.save()
        return HttpResponseRedirect('/account/my-information/')
    else:
        user_form = UserForm(instance=request.user)
        userprofile_form = UserProfileForm(initial={"birth": userprofile.birth,
                                                    "phone": userprofile.phone})
        userinfo_form = UserInfoForm(initial={"school": userinfo.school,
                                              "company": userinfo.company,
                                              "profession": userinfo.profession,
                                              "address": userinfo.address,
                                              "aboutme": userinfo.aboutme, })
        return render(request, 'account/myself_edit.html',
                      {"user_form": user_form,
                       "userprofile_form": userprofile_form,
                       "userinfo_form": userinfo_form, })
