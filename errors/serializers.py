from rest_framework import serializers

from portfolio_backend import service
from . import models 


class ErrorFeedbackSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ErrorFeedback
        fields = ('comment',)


class ClientErrorSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ClientError
        fields = (
            'name',
            'message',
            'componentStack',
            'stack',
            'url',
            'userAgent',
        )

    def create(self, validated_data):
        ip_address = service.get_client_ip(self.context.get('request'))
        validated_data['ipAddress'] = ip_address
        created_error = models.ClientError.objects.create(**validated_data)
        return created_error