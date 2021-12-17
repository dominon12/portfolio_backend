from django.contrib import admin

from . import models


@admin.register(models.Technology)
class TechnologyAdmin(admin.ModelAdmin):
    list_display = ('techGroup', 'name', 'level', 'isRelevant')
    list_filter = ('techGroup', 'level', 'isRelevant')
    search_fields = ('name',)


class TechnologyInline(admin.StackedInline):
    model = models.Technology
    extra = 1


@admin.register(models.TechGroup)
class TechGroupAdmin(admin.ModelAdmin):
    list_display = ('name', 'order')
    search_fields = ('name',)
    inlines = (TechnologyInline,)

