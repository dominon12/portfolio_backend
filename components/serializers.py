from rest_framework import serializers

from portfolio_backend.service import build_absolute_uri
from . import models


class ButtonSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Button
        fields = (
            'pk',
            'text',
            'link',
        )


class ImageSerializer(serializers.ModelSerializer):
    src = serializers.SerializerMethodField()

    class Meta:
        model = models.Image
        fields = (
            'pk',
            'src',
            'alt',
            'width',
            'height'
        )

    def get_src(self, obj):
        return build_absolute_uri(
            request=self.context.get('request'),
            relative_url=obj.image.url
        )