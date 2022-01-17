from rest_framework.generics import ListAPIView, CreateAPIView
from rest_framework.views import APIView
from rest_framework.response import Response

from . import models, serializers, tasks


class ContactMethodList(ListAPIView):
    queryset = models.ContactMethod.objects.all()
    serializer_class = serializers.ContactMethodSerializer
    

class ContactRequestCreate(CreateAPIView):
    queryset = models.ContactRequest.objects.all()
    serializer_class = serializers.ContactRequestSerializer


class ReportOrder(APIView):
    def post(self, request):
        tasks.on_new_order(request.data)
        return Response(
            data={"success": True}
        )