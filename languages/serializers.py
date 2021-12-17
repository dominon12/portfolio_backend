from rest_framework import serializers

from . import models 


class LanguageSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Language
        fields = ('pk', 'name', 'code', 'level', 'learningHistory')