from rest_framework import serializers

from . import models
from components import serializers as components_serializers


class AboutUnitSerializer(serializers.ModelSerializer):
    image = components_serializers.ImageSerializer(read_only=True)
    button = components_serializers.ButtonSerializer(read_only=True)

    class Meta:
        model = models.AboutUnit
        fields = (
            'pk',
            'title',
            'description',
            'image',
            'button'
        )


class ProfileSerializer(serializers.ModelSerializer):
    aboutUnits = AboutUnitSerializer(read_only=True, many=True)
    photo = components_serializers.ImageSerializer(read_only=True)

    class Meta:
        model = models.Profile
        fields = (
            'firstName',
            'lastName',
            'jobTitle',
            'nickname',
            'cvDescription',
            'photo',
            'aboutUnits',
        )