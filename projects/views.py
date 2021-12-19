from rest_framework.generics import ListAPIView
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response

from . import models, serializers, service


class ProjectsPagination(PageNumberPagination):
    page_size_query_param = "pageSize"
    page_size = 6

    def get_paginated_response(self, data):
        return Response({
            'count': self.page.paginator.count,
            'totalPages': self.page.paginator.num_pages,
            'results': data
        })


class ProjectList(ListAPIView):
    queryset = models.Project.objects.all()
    serializer_class = serializers.ProjectSerializer
    pagination_class = ProjectsPagination

    def get_queryset(self):
        queryset = super().get_queryset();
        queryset = service.filter_projects(queryset, self.request.GET)
        return queryset

    def paginate_queryset(self, queryset):
        if bool(self.request.query_params.get('pageSize', None)) == -1:
            return None
        return super().paginate_queryset(queryset)