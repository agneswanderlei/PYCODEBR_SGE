from django.contrib import admin
from .models import Supplier


class SuppliersAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', )
    search_fields = ('name', )


admin.site.register(Supplier, SuppliersAdmin)
