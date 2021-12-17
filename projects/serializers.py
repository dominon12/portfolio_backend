from rest_framework import serializers

from . import models
from components import serializers as components_serializers


class TechnologySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Technology
        fields = ('pk', 'name', 'level', 'isRelevant')


class TechStackSerializer(serializers.ModelSerializer):
    backend = TechnologySerializer(read_only=True, many=True)
    frontend = TechnologySerializer(read_only=True, many=True)
    devops = TechnologySerializer(read_only=True, many=True)

    class Meta:
        model = models.TechStack
        fields = ('backend', 'frontend', 'devops')


class ProjectSerializer(serializers.ModelSerializer):
    image = components_serializers.ImageSerializer(read_only=True)
    technologies = TechStackSerializer(read_only=True)

    class Meta:
        model = models.Project
        fields = (
            'pk',
            'name',
            'image',
            'shortDescription',
            'description',
            'type',
            'date',
            'implementationTime',
            'link',
            'repository',
            'technologies'
        )