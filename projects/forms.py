from django import forms

from ckeditor_uploader.widgets import CKEditorUploadingWidget

from . import models


class ProjectAdminForm(forms.ModelForm):
    description = forms.CharField(widget=CKEditorUploadingWidget)

    class Meta:
        model = models.Project
        fields = "__all__"