from django.urls import path
from .views import (
    SuppliersListView,
    SuppliersCreateView,
    SuppliersDetailView,
    SuppliersUpdateView,
    SuppliersDeleteView
)

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
    ),
    path(
        'suppliers/<int:pk>/detail/',
        SuppliersDetailView.as_view(),
        name='suppliers_detail'
    ),
    path(
        'suppliers/<int:pk>/update/',
        SuppliersUpdateView.as_view(),
        name='suppliers_update'
    ),
    path(
        'suppliers/<int:pk>/delete',
        SuppliersDeleteView.as_view(),
        name='suppliers_delete'
    )
]
