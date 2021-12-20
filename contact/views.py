from rest_framework.generics import ListAPIView, CreateAPIView

from . import models, serializers


class ContactMethodList(ListAPIView):
    queryset = models.ContactMethod.objects.all()
    serializer_class = serializers.ContactMethodSerializer
    

class ContactRequestCreate(CreateAPIView):
    queryset = models.ContactRequest.objects.all()
    serializer_class = serializers.ContactRequestSerializer