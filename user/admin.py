from django.contrib import admin
from unfold.admin import ModelAdmin

from . import models


# Register your models here.

class UserAdmin(ModelAdmin):
    list_display = [
        'first_name',
        'last_name',
        'phone',
        'email',
        'permission',
    ]

    list_editable = [
        'permission'
    ]


admin.site.register(models.User, UserAdmin)
