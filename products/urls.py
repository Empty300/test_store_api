from django.urls import path, include
from rest_framework import routers

from products.views import ProductDetailView, ReviewCreateView, ProductsModelViewSet, BasketModelViewSet

app_name = 'products'

router = routers.DefaultRouter()
router.register(r'products', ProductsModelViewSet)
router.register(r'baskets', BasketModelViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('products/<int:pk>', ProductDetailView.as_view()),
    path('review/', ReviewCreateView.as_view()),


]
