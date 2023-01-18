from rest_framework import serializers

from products.models import Product


class ProductsListSerializer(serializers.ModelSerializer):
    category = serializers.SlugRelatedField(slug_field='name', read_only=True)
    class Meta:
        model = Product
        fields = ('name', 'category', 'price_now', 'price_old',
                  'image1', 'brand')


class ProductDetailSerializer(serializers.ModelSerializer):
    category = serializers.SlugRelatedField(slug_field='name', read_only=True)

    class Meta:
        model = Product
        fields = ('name', 'specifications', 'price_now', 'price_old', 'quantity',
                  'image1', 'image2', 'image3', 'category', 'description', 'colors', 'discount', 'brand')
