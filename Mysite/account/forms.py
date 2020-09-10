from django import forms


class LoginForm(forms.Form):
    """ 登录的form表单 """
    username = forms.CharField(required=True, max_length=16, min_length=8)
    password = forms.CharField(
        required=True, max_length=16, min_length=8, widget=forms.PasswordInput)
