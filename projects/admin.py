from django.contrib import admin

from . import models, forms


@admin.register(models.Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('name', 'type', 'shortDescription', 'date')
    list_filter = ('type', 'date')
    search_fields = ('name', 'shortDescription', 'description')
    form = forms.ProjectAdminForm
