from django.contrib import admin
from . import models


@admin.register(models.Post)
class PostAdmin(admin.ModelAdmin):

    """Post Admin Definition"""

    list_filter = ("care_type", "branch")

    list_display = ("title", "branch", "care_type", "name", "phone")
