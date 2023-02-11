from django_filters import rest_framework as filters

from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response

from products.models import Product


class CharFilterInFilter(filters.BaseInFilter, filters.CharFilter):
    pass


class ProductFilter(filters.FilterSet):
    category = CharFilterInFilter(field_name='category__name', lookup_expr='in')
    brand = CharFilterInFilter()
    price_now = filters.RangeFilter()

    class Meta:
        model = Product
        fields = ['category', 'price_now', 'brand']


class PaginationMovies(PageNumberPagination):
    page_size = 10
    max_page_size = 1000

    def get_paginated_response(self, data):
        return Response({
            'links': {
                'next': self.get_next_link(),
                'previous': self.get_previous_link()
            },
            'count': self.page.paginator.count,
            'results': data
        })
