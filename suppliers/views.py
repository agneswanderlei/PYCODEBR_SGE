from django.views.generic import (
    ListView,
    CreateView,
    UpdateView,
    DeleteView,
    DetailView
)
from .models import Supplier
from .forms import SuppliersForm
from django.urls import reverse_lazy


class SuppliersListView(ListView):

    model = Supplier
    template_name = 'suppliers_list.html'
    context_object_name = 'suppliers_list'
    paginate_by = 3

    def get_queryset(self):
        queryset = super().get_queryset()
        name = self.request.GET.get('name')

        if name:
            queryset = queryset.filter(name__icontains=name)
        return queryset


class SuppliersCreateView(CreateView):
    model = Supplier
    template_name = 'suppliers_create.html'
    form_class = SuppliersForm
    success_url = reverse_lazy('suppliers_list')


class SuppliersDetailView(DetailView):
    model = Supplier
    template_name = 'suppliers_detail.html'


class SuppliersUpdateView(UpdateView):
    model = Supplier
    template_name = 'suppliers_update.html'
    form_class = SuppliersForm
    success_url = reverse_lazy('suppliers_list')


class SuppliersDeleteView(DeleteView):
    model = Supplier
    template_name = 'suppliers_delete.html'
    success_url = reverse_lazy('suppliers_list')
