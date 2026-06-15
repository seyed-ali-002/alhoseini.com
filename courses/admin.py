from django.contrib import admin
from unfold.admin import ModelAdmin

# Register your models here.
from . import models


class CourseAdmin(ModelAdmin):
    list_display = [
        'title',
        'teacher',
        'category',
        'is_active',
        'course_key'
    ]
    list_editable = [
        'is_active'
    ]

    class Meta:
        verbose_name = 'course'
        verbose_name_plural = 'courses'


admin.site.register(models.Course, CourseAdmin)
