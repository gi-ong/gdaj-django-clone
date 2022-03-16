from django.contrib import admin
from . import models


@admin.register(models.Branch)
class BranchAdmin(admin.ModelAdmin):

    """Page Admin Definition"""

    list_display = ("__str__",)


@admin.register(models.BranchWithUrl)
class BranchUrlAdmin(admin.ModelAdmin):

    """BranchUrl Admin Definition"""

    list_display = ("branch_name", "url_name")
