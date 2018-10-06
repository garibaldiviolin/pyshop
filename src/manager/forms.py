""" Manager app forms module """

from django import forms

from website.models import Category, Product


class CategoryEditForm(forms.ModelForm):

    class Meta:
        model = Category
        fields = ['description']


class ProductEditForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = [
            'barcode', 'title', 'description',
            'image', 'price', 'category'
        ]
