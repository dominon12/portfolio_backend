from django.contrib import admin

from . import models, forms


class TechStackInline(admin.StackedInline):
    model = models.TechStack
    extra = 1;


@admin.register(models.Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('name', 'type', 'shortDescription', 'date')
    list_filter = ('type', 'date')
    search_fields = ('name', 'shortDescription', 'description')
    inlines = (TechStackInline,)
    form = forms.ProjectAdminForm


@admin.register(models.Technology)
class TechnologyAdmin(admin.ModelAdmin):
    list_display = ('name', 'level', 'isRelevant')
    list_filter = ('level', 'isRelevant')
    search_fields = ('name',)


class TechnologyInline(admin.StackedInline):
    model = models.Technology
    extra = 1


@admin.register(models.TechStack)
class TechStackAdmin(admin.ModelAdmin):
    list_display = ('__str__',)