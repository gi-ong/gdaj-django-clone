from django.contrib import admin
from django.utils.html import mark_safe
from . import models


@admin.register(models.QnaPost)
class QnaAdmin(admin.ModelAdmin):

    """Post Admin Definition"""

    list_filter = ("care_type", "branch")

    list_display = ("title", "branch", "care_type", "name", "phone")


@admin.register(models.NoticePost)
class NoticeAdmin(admin.ModelAdmin):

    """NoticePost Admin Definition"""

    list_filter = ("notice_type",)

    list_display = ("title", "notice_type", "host")


@admin.register(models.NoticePhoto)
class NoticePhotoAdmin(admin.ModelAdmin):

    """Photo Admin Definition"""

    list_display = ("__str__", "get_thumbnail")

    def get_thumbnail(self, obj):
        return mark_safe(f'<img width="50px" src="{obj.file.url}" />')

    get_thumbnail.short_description = "Thumbnail"
