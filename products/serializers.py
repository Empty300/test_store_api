from rest_framework import fields, serializers

from products.models import Basket, Product, ProductCategory, Reviews


class ProductsListSerializer(serializers.ModelSerializer):
    category = serializers.SlugRelatedField(slug_field='name', queryset=ProductCategory.objects.all())

    class Meta:
        model = Product
        fields = ('name', 'category', 'price_now', 'price_old',
                  'image1', 'brand')


class ReviewSerializer(serializers.ModelSerializer):
    user = serializers.SlugRelatedField(slug_field='username', read_only=True)

    class Meta:
        model = Reviews
        fields = ('stars', 'product', 'review', 'created_timestamp', 'user')


class ProductDetailSerializer(serializers.ModelSerializer):
    category = serializers.SlugRelatedField(slug_field='name', read_only=True)
    reviews = ReviewSerializer(many=True)

    class Meta:
        model = Product
        fields = ('name', 'specifications', 'price_now', 'price_old', 'quantity', 'reviews',
                  'image1', 'image2', 'image3', 'category', 'description', 'colors', 'discount', 'brand')


class BasketSerializer(serializers.ModelSerializer):
    product = ProductsListSerializer()
    sum = fields.FloatField(required=False)
    total_sum = fields.SerializerMethodField()
    total_quantity = fields.SerializerMethodField()

    class Meta:
        model = Basket
        fields = ('id', 'user', 'product', 'quantity', 'sum', 'total_sum', 'total_quantity', 'created_timestamp')
        read_only_fields = ('created_timestamp',)

    def get_total_sum(self, obj):
        return Basket.objects.filter(user_id=obj.user.id).total_sum()

    def get_total_quantity(self, obj):
        return Basket.objects.filter(user_id=obj.user.id).total_quantity()
