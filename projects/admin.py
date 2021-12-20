from django.contrib import admin
from django.utils.safestring import mark_safe

from . import models, forms


@admin.register(models.Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('name', 'get_image', 'shortDescription', 'date')
    list_filter = ('date',)
    search_fields = ('name', 'shortDescription', 'description')
    form = forms.ProjectAdminForm

    def get_image(self, obj):
        try:
            img = obj.previewImage.image.url
        except:
            return None
        return mark_safe(f'<img src="{img}" width="100" height="100">')
    get_image.short_description = "Image"