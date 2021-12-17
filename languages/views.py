from rest_framework.generics import ListAPIView

from . import models, serializers 


class LanguageList(ListAPIView):
    queryset = models.Language.objects.all()
    serializer_class = serializers.LanguageSerializer