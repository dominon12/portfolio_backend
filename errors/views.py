from rest_framework.generics import CreateAPIView

from . import models, serializers 


class ErrorFeedbackCreate(CreateAPIView):
    queryset = models.ErrorFeedback.objects.all()
    serializer_class = serializers.ErrorFeedbackSerializer


class ClientErrorCreate(CreateAPIView):
    queryset = models.ClientError.objects.all()
    serializer_class = serializers.ClientErrorSerializer