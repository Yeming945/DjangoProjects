from django.contrib import admin

from .models import UserProfile, UserInfo


class UserProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'birth', 'phone']
    list_filter = ('phone',)


class UserInfofileAdmin(admin.ModelAdmin):
    list_display = ['user', 'school', 'company', 'profession', 'address']
    list_filter = ('school', 'company', 'profession', 'address')


admin.site.register(UserProfile, UserProfileAdmin)
admin.site.register(UserInfo, UserInfofileAdmin)
