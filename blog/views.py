from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response

from . import models, serializers, service



class ArticlesPagination(PageNumberPagination):
    page_size_query_param = "pageSize"
    page_size = 12

    def get_paginated_response(self, data):
        return Response({
            'count': self.page.paginator.count,
            'totalPages': self.page.paginator.num_pages,
            'results': data
        })



class ArticleList(ListAPIView):
    queryset = models.Article.objects.all()
    serializer_class = serializers.ArticleListSerializer
    pagination_class = ArticlesPagination


class ArticleDetail(RetrieveAPIView):
    queryset = models.Article.objects.all()
    serializer_class = serializers.ArticleSerializer
    lookup_field = 'slug'

    def get_object(self):
        article = super().get_object()
        return service.add_article_visitor(self.request, article)
