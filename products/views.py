from rest_framework import status
from rest_framework.generics import RetrieveAPIView
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from django_filters.rest_framework import DjangoFilterBackend

from products.models import Product, Basket, Reviews
from products.permissions import IsOwnerPermission, IsOwnerOrGetPermission
from products.serializers import ProductsListSerializer, ProductDetailSerializer, \
    BasketSerializer, ReviewSerializer
from products.service import ProductFilter


class ProductsModelViewSet(ModelViewSet):
    serializer_class = ProductsListSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_class = ProductFilter
    queryset = Product.objects.all()

    def get_permissions(self):
        if self.action in ('create', 'update', 'destroy'):
            self.permission_classes = (IsAdminUser,)
        return super(ProductsModelViewSet, self).get_permissions()


class ProductDetailView(RetrieveAPIView):
    queryset = Product.objects.filter()
    serializer_class = ProductDetailSerializer


class ReviewModelViewSet(ModelViewSet):
    queryset = Reviews.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = (IsOwnerOrGetPermission,)

    def create(self, request, *args, **kwargs):
        try:
            review = Reviews.objects.create(user=self.request.user, stars=request.data['stars'],
                                            review=request.data['review'], product_id=request.data['product'])
            serializer = self.get_serializer(review)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        except KeyError:
            return Response(status=status.HTTP_400_BAD_REQUEST)


class BasketModelViewSet(ModelViewSet):
    queryset = Basket.objects.all()
    serializer_class = BasketSerializer
    permission_classes = (IsOwnerPermission,)
    pagination_class = None

    def get_queryset(self):
        queryset = super(BasketModelViewSet, self).get_queryset()
        return queryset.filter(user=self.request.user)

    def create(self, request, *args, **kwargs):
        try:
            product_id = request.data['product_id']
            products = Product.objects.filter(id=product_id)
            if not products.exists():
                return Response({'product_id': 'There is no product with this ID.'}, status=status.HTTP_400_BAD_REQUEST)
            obj, is_created = Basket.create_or_update(products.first().id, self.request.user)
            status_code = status.HTTP_201_CREATED if is_created else status.HTTP_200_OK
            serializer = self.get_serializer(obj)
            return Response(serializer.data, status=status_code)
        except KeyError:
            return Response({'product_id': 'This field is required.'}, status=status.HTTP_400_BAD_REQUEST)