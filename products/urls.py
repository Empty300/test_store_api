from django.urls import path

from products.views import ProductsListView, ProductDetailView

app_name = 'products'

urlpatterns = [
    path('products/', ProductsListView.as_view()),
    path('products/<int:pk>', ProductDetailView.as_view()),

]
