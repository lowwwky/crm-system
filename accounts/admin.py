from django.contrib import admin

from accounts.models import UserProfile


class UserProfileCard(admin.ModelAdmin):
    fields = ['photo','notes']

admin.site.register(UserProfile,UserProfileCard)