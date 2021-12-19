from django.contrib import admin
from django.utils.safestring import mark_safe

from . import models


@admin.register(models.DonationMethod)
class DonationMethodAdmin(admin.ModelAdmin):
    list_display = ('name', 'link', 'isLink', 'get_image')
    list_filter = ('isLink',)
    search_fields = ('name', 'link')

    def get_image(self, obj):
        try:
            img = obj.image.image.url
        except:
            return None
        return mark_safe(f'<img src="{img}" width="100" height="100">')
    get_image.short_description = "Image"