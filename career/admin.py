from django.contrib import admin

from . import models


@admin.register(models.CareerEvent)
class CareerEventAdmin(admin.ModelAdmin):
    list_display = ('title', 'date', 'place', 'isRelevant')
    list_filter = ('date', 'place', 'isRelevant')
    search_fields = ('title', 'description', 'place')