from rest_framework.generics import ListAPIView

from . import models, serializers


class AboutUnitList(ListAPIView):
    queryset = models.AboutUnit.objects.all()
    serializer_class = serializers.AboutUnitSerializer
