from django.contrib import admin

from . import models 


@admin.register(models.ContactMethod)
class ContactMethodAdmin(admin.ModelAdmin):
    list_display = ('name', 'link', 'order')


@admin.register(models.ContactRequest)
class ContactRequestAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'comment', 'date')
    list_filter = ('date',)
    search_fields = ('name', 'email', 'comment')
    readonly_fields = ('name', 'email', 'comment', 'date')