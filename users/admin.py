from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from . import models


@admin.register(models.User)
class CustomUserAdmin(UserAdmin):

    admin.autodiscover()
    admin.site.enable_nav_sidebar = False

    list_filter = UserAdmin.list_filter + ("superhost",)

    list_display = UserAdmin.list_display + ("superhost",)
