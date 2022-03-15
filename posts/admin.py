from django.contrib import admin
from django.utils.html import mark_safe
from . import models


class PhotoInline(admin.TabularInline):

    model = models.NoticePhoto


class BnAPhotoInline(admin.TabularInline):

    model = models.BnAPhoto


class NewsPhotoInline(admin.TabularInline):

    model = models.NewsPhoto


@admin.register(models.BnAPost)
class BnAAdmin(admin.ModelAdmin):

    """BnA Admin Definition"""

    inlines = (BnAPhotoInline,)

    list_filter = ("bna_type",)

    list_display = (
        "title",
        "bna_type",
    )


@admin.register(models.QnaPost)
class QnaAdmin(admin.ModelAdmin):

    """Post Admin Definition"""

    list_filter = ("care_type", "branch")

    list_display = ("title", "branch", "care_type", "name", "phone")


@admin.register(models.NoticePost)
class NoticeAdmin(admin.ModelAdmin):

    """NoticePost Admin Definition"""

    inlines = (PhotoInline,)

    list_filter = ("notice_type",)

    list_display = ("title", "notice_type", "host")


@admin.register(models.NoticePhoto)
class NoticePhotoAdmin(admin.ModelAdmin):

    """Notice Photo Admin Definition"""

    list_display = ("__str__", "get_thumbnail")

    def get_thumbnail(self, obj):
        return mark_safe(f'<img width="50px" src="{obj.file.url}" />')

    get_thumbnail.short_description = "Thumbnail"


@admin.register(models.BnAPhoto)
class BnAPhotoAdmin(admin.ModelAdmin):

    """BnAPhoto Admin Definition"""

    list_display = ("__str__", "get_thumbnail")

    def get_thumbnail(self, obj):
        return mark_safe(f'<img width="50px" src="{obj.file.url}" />')

    get_thumbnail.short_description = "Thumbnail"


@admin.register(models.NewsPost)
class NewsAdmin(admin.ModelAdmin):

    """NewsPost Admin Definition"""

    inlines = (NewsPhotoInline,)

    list_display = ("title", "content")


@admin.register(models.NewsPhoto)
class NewsPhotoAdmin(admin.ModelAdmin):

    """News Photo Admin Definition"""

    list_display = ("__str__", "get_thumbnail")

    def get_thumbnail(self, obj):
        return mark_safe(f'<img width="50px" src="{obj.file.url}" />')

    get_thumbnail.short_description = "Thumbnail"
