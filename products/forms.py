from django import forms
from .models import Product


class ProductForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = [
            'title',
            'category',
            'brand',
            'description',
            'serie_number',
            'cost_price',
            'selling_prince',
            'quantity'
        ]
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'category': forms.Select(attrs={'class': 'form-control'}),
            'brand': forms.Select(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control',
                                                 'rows': 3}),
            'serie_number': forms.TextInput(attrs={'class': 'form-control'}),
            'cost_price': forms.NumberInput(attrs={'class': 'form-control'}),
            'selling_prince': forms.NumberInput(attrs={
                'class': 'form-control'
            }),
            'quantity': forms.NumberInput(attrs={'class': 'form-control'})
        }
        labels = {
            'title': 'Nome do Produto',
            'category': 'Categoria',
            'brand': 'Marca',
            'description': 'Descrição',
            'serie_number': 'Número de Série',
            'cost_price': 'Preço de Custo',
            'selling_prince': 'Preço de Venda',
            'quantity': 'Quantidade'
        }
