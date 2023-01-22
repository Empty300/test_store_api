from django_filters import rest_framework as filters

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
