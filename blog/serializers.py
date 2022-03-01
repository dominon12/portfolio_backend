from rest_framework import serializers

from . import models
from components import serializers as components_serializers


class ArticleListSerializer(serializers.ModelSerializer):
    image = components_serializers.ImageSerializer(read_only=True)
    views = serializers.SerializerMethodField()

    class Meta:
        model = models.Article
        fields = (
            'pk',
            'title',
            'slug',
            'image',
            'views',
            'description',
            'dateCreated',
        )

    def get_views(self, obj):
        return obj.viewers.count()


class ArticleSerializer(serializers.ModelSerializer):
    image = components_serializers.ImageSerializer(read_only=True)
    views = serializers.SerializerMethodField()

    class Meta:
        model = models.Article
        fields = (
            'title',
            'description',
            'image',
            'body',
            'views',
            'dateCreated',
            'dateEdited',
        )

    def get_views(self, obj):
        return obj.viewers.count()