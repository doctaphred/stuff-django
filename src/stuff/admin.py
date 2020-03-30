from django.contrib.admin import ModelAdmin, register
from . import models


@register(models.Thing)
class ThingAdmin(ModelAdmin):
    date_hierarchy = 'added'

    list_display = [
        '__str__',
        'sha256',
        'length',
        'preview',
        'added',
        'modified',
    ]

    list_filter = [
        'full',
        'added',
        'modified',
    ]

    search_fields = [
        'sha256',
        'length',
        'preview',
        'content',
        'added',
        'modified',
    ]
