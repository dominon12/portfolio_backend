from django.contrib import admin
from django.utils.safestring import mark_safe

from . import models


@admin.register(models.Button)
class ButtonAdmin(admin.ModelAdmin):
    list_display = ('text', 'link')


@admin.register(models.Image)
class ImageAdmin(admin.ModelAdmin):
    list_display = ("alt", 'get_image')

    def get_image(self, obj):
        try:
            img = obj.image.url
        except:
            return None
        return mark_safe(f'<img src="{img}" width="100" height="100">')
    get_image.short_description = "Image"