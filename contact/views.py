from rest_framework.generics import ListAPIView

from . import models, serializers


class ContactMethodList(ListAPIView):
    queryset = models.ContactMethod.objects.all()
    serializer_class = serializers.ContactMethodSerializer
    