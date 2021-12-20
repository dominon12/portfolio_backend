from rest_framework import serializers

from . import models 


class ErrorFeedbackSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ErrorFeedback
        fields = ('comment',)