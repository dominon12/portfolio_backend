from rest_framework.generics import ListAPIView

from . import models, serializers


class DonationMethodList(ListAPIView):
    queryset = models.DonationMethod.objects.all()
    serializer_class = serializers.DonationMethodSerializer