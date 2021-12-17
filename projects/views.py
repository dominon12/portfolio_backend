from rest_framework.generics import ListAPIView

from . import models, serializers


class ProjectList(ListAPIView):
    queryset = models.Project.objects.all()
    serializer_class = serializers.ProjectSerializer
