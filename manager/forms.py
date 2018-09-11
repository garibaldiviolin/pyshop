from django import forms

from website.models import Product


class ProductManagementForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = [
            'barcode', 'title', 'description', 'image', 'price', 'category'
        ]
