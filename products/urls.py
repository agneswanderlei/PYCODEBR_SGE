from django.urls import path
from .views import ProductListView, ProductCreateView, ProductDetailView

urlpatterns = [
    path(
        'products/list/',
        ProductListView.as_view(),
        name='product_list'
    ),
    path(
        'products/create/',
        ProductCreateView.as_view(),
        name='product_create'
    ),
    path(
        'products/<int:pk>/detail',
        ProductDetailView.as_view(),
        name='product_detail'
    )
]
