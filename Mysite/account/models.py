from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, unique=True, verbose_name='用户')
    birth = models.DateField(blank=True, null=True, verbose_name='生日')
    phone = models.CharField(max_length=20, null=True, verbose_name='手机号码')

    class Meta:

        verbose_name = '用户资料'
        verbose_name_plural = verbose_name

    def __str__(self):
        return 'user {}'.format(self.user.username)


class UserInfo(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, unique=True, verbose_name='用户')
    school = models.CharField(max_length=100, blank=True, verbose_name='学校')
    company = models.CharField(max_length=100, blank=True, verbose_name='公司')
    profession = models.CharField(
        max_length=100, blank=True, verbose_name='职业')
    address = models.CharField(max_length=100, blank=True, verbose_name='地址')
    aboutme = models.TextField(blank=True, verbose_name='个人介绍')

    def __str__(self):
        return "user:{}".format(self.user.username)

    class Meta:
        verbose_name = '用户信息'
        verbose_name_plural = '用户信息'
