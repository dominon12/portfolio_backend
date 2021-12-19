from rest_framework.generics import ListAPIView

from . import models, serializers


class TechGroupList(ListAPIView):
    queryset = models.TechGroup.objects.all()
    serializer_class = serializers.TechGroupSerializer
