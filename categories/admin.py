from django.contrib import admin
from unfold.admin import ModelAdmin

# Register your models here.
from . import models


class CategoryAdmin(ModelAdmin):
    list_display = [
        'name',
        'url',
        'is_active'
    ]

    list_editable = [
        'is_active'
    ]

    class Meta:
        verbose_name = 'category'
        verbose_name_plural = 'categories'


admin.site.register(models.Category, CategoryAdmin)
