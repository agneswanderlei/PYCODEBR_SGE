from django.urls import path
from .views import (
    CategoryListView,
    CategoryCreateView,
    CategoryDetailView,
    CategoryUpdateView,
    CategoryDeleteView
)

urlpatterns = [
    path(
        'category/list/',
        CategoryListView.as_view(),
        name='category_list'
    ),
    path(
        'category/create/',
        CategoryCreateView.as_view(),
        name='category_create'
    ),
    path(
        'category/<int:pk>/detail/',
        CategoryDetailView.as_view(),
        name='category_detail'
    ),
    path(
        'category/<int:pk>/update/',
        CategoryUpdateView.as_view(),
        name='category_update'
    ),
    path(
        'category/<int:pk>/delete/',
        CategoryDeleteView.as_view(),
        name='category_delete'
    )
]
