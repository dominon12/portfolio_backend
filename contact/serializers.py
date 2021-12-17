from rest_framework import serializers

from . import models 


class ContactMethodSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ContactMethod
        fields = ('pk', 'name', 'link')