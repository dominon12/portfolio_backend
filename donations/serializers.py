from rest_framework import serializers

from . import models 
from components import serializers as components_serializers

class DonationMethodSerializer(serializers.ModelSerializer):
    image = components_serializers.ImageSerializer(read_only=True)

    class Meta:
        model = models.DonationMethod
        fields = (
            'pk', 
            'name', 
            'comment', 
            'link', 
            'isLink', 
            'image'
        )