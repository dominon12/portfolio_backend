from rest_framework.generics import ListAPIView
from rest_framework.views import APIView
from rest_framework.response import Response

from . import models, serializers


class AboutUnitList(ListAPIView):
    queryset = models.AboutUnit.objects.all()
    serializer_class = serializers.AboutUnitSerializer


class ProfileDetail(APIView):

    def get(self, request):
        profile = models.Profile.objects.first()
        serializer = serializers.ProfileSerializer(profile, context={"request": request})
        return Response(serializer.data)