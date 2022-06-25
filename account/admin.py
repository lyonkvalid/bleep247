from django.contrib import admin
from .models import Profile, User

class UserAdmin(admin.ModelAdmin):
    list_display = ("username", "uid", "email")

admin.site.register(User, UserAdmin)
admin.site.register(Profile)