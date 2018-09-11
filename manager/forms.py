from django import forms

from website.models import Product


class ProductEditForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = [
            'barcode', 'slug', 'title', 'description',
            'image', 'price', 'category'
        ]
