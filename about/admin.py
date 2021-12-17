from django.contrib import admin
from django.utils.safestring import mark_safe

from . import models


@admin.register(models.AboutUnit)
class AboutUnitAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'get_image')

    def get_image(self, obj):
        try:
            img = obj.image.image.url
        except:
            return None
        return mark_safe(f'<img src="{img}" width="100" height="100">')
    get_image.short_description = "Image"


@admin.register(models.Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = (
        'firstName', 
        'lastName', 
        'get_image', 
        'jobTitle', 
        'nickname'
    )

    def get_image(self, obj):
        try:
            img = obj.photo.image.url
        except:
            return None
        return mark_safe(f'<img src="{img}" width="100" height="100">')
    get_image.short_description = "Image"