from django.contrib import admin

from . import models


@admin.register(models.ErrorFeedback)
class ErrorFeedbackAdmin(admin.ModelAdmin):
    list_display = ('comment', 'date')
    list_filer = ('date',)
    search_fields = ('comment',)
    readonly_fields = ('comment', 'date')