from django import forms
from django.contrib.auth.models import User

from .models import UserProfile


class LoginForm(forms.Form):
    """ 
    登录的form表单 
    提交表单之后，不会对数据库进行修改，则继承Form类
    """
    username = forms.CharField(required=True, max_length=16, min_length=8)
    password = forms.CharField(
        required=True, max_length=16, min_length=8, widget=forms.PasswordInput)


class ResgitrationForm(forms.ModelForm):
    """
    注册的表单
    如果要将表单中的数据写入数据库表或者修改某些记录的值，就要让表单类继承ModelForm类
    """
    password = forms.CharField(
        label='Password', widget=forms.PasswordInput, required=True, max_length=16, min_length=8)
    password2 = forms.CharField(
        label='Confirm Password', widget=forms.PasswordInput, required=True, max_length=16, min_length=8)

    class Meta:
        model = User
        fields = ('username', 'email')  # 引用默认User模型中的字段

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('passwords do not match.')
        return cd['password2']


class UserProfileForm(forms.ModelForm):

    class Meta:
        model = UserProfile
        fields = ('phone', 'birth')
