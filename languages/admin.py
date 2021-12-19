from django.contrib import admin
from django.utils.safestring import mark_safe

from . import models 


@admin.register(models.Language)
class LanguageAdmin(admin.ModelAdmin):
    list_display = (
        'name', 
        'level', 
        'get_image', 
        'learningHistory', 
        'order'
    )

    def get_image(self, obj):
        return mark_safe(f'<img style="border: 1px solid black" src="https://flagcdn.com/w640/{obj.code}.png" width="150" height="100">')
    get_image.short_description = "Image"
