from django.urls import path, include
from rest_framework import routers

from orders.views import OrderModelViewSet
from products.views import ProductDetailView, ProductsModelViewSet, BasketModelViewSet, \
    ReviewModelViewSet

app_name = 'products'

router = routers.DefaultRouter()
router.register(r'products', ProductsModelViewSet)
router.register(r'baskets', BasketModelViewSet)
router.register(r'review', ReviewModelViewSet)
router.register(r'order', OrderModelViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('products/<int:pk>', ProductDetailView.as_view()),
]
