from rest_framework import serializers

from . import models 


class CareerEventSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.CareerEvent
        fields = (
            'pk',
            'title',
            'description',
            'date',
            'place',
            'isRelevant'
        )