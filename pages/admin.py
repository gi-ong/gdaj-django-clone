from django.contrib import admin
from . import models


@admin.register(models.Branch)
class PageAdmin(admin.ModelAdmin):

    """Page Admin Definition"""

    list_display = ("__str__",)
