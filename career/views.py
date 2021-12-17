from rest_framework.generics import ListAPIView

from . import models, serializers 


class CareerEventList(ListAPIView):
    queryset = models.CareerEvent.objects.all()
    serializer_class = serializers.CareerEventSerializer