from rest_framework.response import Response
from rest_framework.views import APIView

from products.models import Product
from products.serializers import ProductsListSerializer, ProductDetailSerializer


class ProductsListView(APIView):

    def get(self, request):
        products = Product.objects.all()
        serializer = ProductsListSerializer(products, many=True)
        return Response(serializer.data)


class ProductDetailView(APIView):

    def get(self, request, pk):
        product = Product.objects.get(id=pk)
        serializer = ProductDetailSerializer(product)
        return Response(serializer.data)
