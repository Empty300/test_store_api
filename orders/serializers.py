from rest_framework import serializers, fields

from orders.models import Order


class OrderListSerializer(serializers.ModelSerializer):
    initiator = serializers.SlugRelatedField(slug_field='username', read_only=True)
    status = serializers.CharField()
    class Meta:
        model = Order
        fields = ("__all__")


