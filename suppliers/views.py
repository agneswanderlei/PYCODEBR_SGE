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
from django.contrib.auth.mixins import (
    LoginRequiredMixin,
    PermissionRequiredMixin
)


class SuppliersListView(LoginRequiredMixin,
                        PermissionRequiredMixin,
                        ListView):

    model = Supplier
    template_name = 'suppliers_list.html'
    context_object_name = 'suppliers_list'
    paginate_by = 3
    permission_required = 'suppliers.view_supplier'

    def get_queryset(self):
        queryset = super().get_queryset()
        name = self.request.GET.get('name')

        if name:
            queryset = queryset.filter(name__icontains=name)
        return queryset


class SuppliersCreateView(LoginRequiredMixin,
                          PermissionRequiredMixin,
                          CreateView):
    model = Supplier
    template_name = 'suppliers_create.html'
    form_class = SuppliersForm
    success_url = reverse_lazy('suppliers_list')
    permission_required = 'suppliers.add_supplier'


class SuppliersDetailView(LoginRequiredMixin,
                          PermissionRequiredMixin,
                          DetailView):
    model = Supplier
    template_name = 'suppliers_detail.html'
    permission_required = 'suppliers.view_supplier'


class SuppliersUpdateView(LoginRequiredMixin,
                          PermissionRequiredMixin,
                          UpdateView):
    model = Supplier
    template_name = 'suppliers_update.html'
    form_class = SuppliersForm
    success_url = reverse_lazy('suppliers_list')
    permission_required = 'suppliers.change_supplier'


class SuppliersDeleteView(LoginRequiredMixin,
                          PermissionRequiredMixin,
                          DeleteView):
    model = Supplier
    template_name = 'suppliers_delete.html'
    success_url = reverse_lazy('suppliers_list')
    permission_required = 'suppliers.delete_supplier'
