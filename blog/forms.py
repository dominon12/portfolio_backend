from django import forms

from ckeditor_uploader.widgets import CKEditorUploadingWidget

from . import models


class ArticleAdminForm(forms.ModelForm):
    body = forms.CharField(widget=CKEditorUploadingWidget)

    class Meta:
        model = models.Article
        fields = "__all__"