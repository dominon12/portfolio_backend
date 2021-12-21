from django.contrib import admin

from . import models


@admin.register(models.ErrorFeedback)
class ErrorFeedbackAdmin(admin.ModelAdmin):
    list_display = ('comment', 'date')
    list_filer = ('date',)
    search_fields = ('comment',)
    readonly_fields = ('comment', 'date')


@admin.register(models.ClientError)
class ClientErrorAdmin(admin.ModelAdmin):
    list_display = (
        'name', 
        'message', 
        'url', 
        'userAgent', 
        'ipAddress', 
        'date'
    )
    list_filter = (
        'name',
        'url',
        'ipAddress',
        'date'
    )
    search_fields = (
        'name',
        'message',
        'componentStack',
        'stack',
        'url',
        'userAgent',
        'ipAddress'
    )
    readonly_fields = (
        'name',
        'message',
        'componentStack',
        'stack',
        'url',
        'userAgent',
        'ipAddress',
        'date'
    )