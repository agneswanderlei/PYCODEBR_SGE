from django.urls import path
from .views import OutflowListView, OuflowCreateView, OutflowDetailView

urlpatterns = [
    path(
        'outflows/list/',
        OutflowListView.as_view(),
        name='outflow_list'
    ),
    path(
        'outflows/create/',
        OuflowCreateView.as_view(),
        name='outflow_create'
    ),
    path(
        'outflow/<int:pk>/detail',
        OutflowDetailView.as_view(),
        name='outflow_detail'
    )
]
