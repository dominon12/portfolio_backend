from rest_framework import serializers

from . import models
from components import serializers as components_serializers
from skills import serializers as skills_serializers



class ProjectSerializer(serializers.ModelSerializer):
    image = components_serializers.ImageSerializer(read_only=True)
    technologies = skills_serializers.TechnologySerializer(read_only=True, many=True)

    class Meta:
        model = models.Project
        fields = (
            'pk',
            'name',
            'image',
            'shortDescription',
            'description',
            'date',
            'implementationTime',
            'link',
            'repository',
            'technologies'
        )