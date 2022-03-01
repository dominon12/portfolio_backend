from django.contrib import admin
from django.utils.safestring import mark_safe

from . import models, forms


@admin.register(models.Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = (
        'title', 
        'get_image', 
        'description', 
        'dateCreated', 
        'dateEdited'
    )
    list_filter = ('dateCreated', 'dateEdited')
    readonly_fields = ('viewers', 'dateCreated', 'dateEdited')
    prepopulated_fields = {'slug': ('title',)}
    form = forms.ArticleAdminForm

    def get_image(self, obj):
        try:
            img = obj.image.image.url
        except:
            return None
        return mark_safe(f'<img src="{img}" width="100" height="100">')
    get_image.short_description = "Image"