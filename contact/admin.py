from django.contrib import admin

from . import models 


@admin.register(models.ContactMethod)
class ContactMethodAdmin(admin.ModelAdmin):
    list_display = ('name', 'link', 'order')