from django.contrib import admin
from unfold.admin import ModelAdmin

# Register your models here.

from . import models


class PostAdmin(ModelAdmin):
    list_display = [
        'title',
        'author',
        'category',

        'views',
        'summary',

        'published',
        'published_date'
    ]

    list_editable = [
        'published',
    ]


class ImageAdmin(ModelAdmin):
    list_display = [
        'name',
        'image'
    ]


class VideoAdmin(ModelAdmin):
    list_display = [
        'title'
    ]

    class Meta:
        verbose_name = 'video'
        verbose_name_plural = 'videos'


admin.site.register(models.Post, PostAdmin)
admin.site.register(models.Images, ImageAdmin)
admin.site.register(models.Videos, VideoAdmin)
