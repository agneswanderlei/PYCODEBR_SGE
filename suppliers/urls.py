from django.urls import path
from .views import SuppliersListView, SuppliersCreateView

urlpatterns = [
    path(
        'suppliers/list/',
        SuppliersListView.as_view(),
        name='suppliers_list'
    ),
    path(
        'suppliers/creat/',
        SuppliersCreateView.as_view(),
        name='suppliers_create'
    )
]
