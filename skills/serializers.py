from rest_framework import serializers

from . import models


class TechnologySerializer(serializers.ModelSerializer):
    techGroup = serializers.CharField(source="techGroup.name")

    class Meta:
        model = models.Technology
        fields = (
            'pk', 
            'techGroup', 
            'name', 
            'level', 
            'isRelevant', 
            'showAsFilter'
        )


class TechGroupSerializer(serializers.ModelSerializer):
    skills = TechnologySerializer(read_only=True, many=True)

    class Meta:
        model = models.TechGroup
        fields = ('pk', 'name', 'skills', 'showAsSkill')