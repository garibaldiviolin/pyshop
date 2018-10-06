""" Manager app forms module """

from django import forms

from website.models import Category, Product


class CategoryEditForm(forms.ModelForm):
    """ ModelForm for the Category model administration """

    class Meta:
        model = Category
        fields = ['description']


class ProductEditForm(forms.ModelForm):
    """ ModelForm for the Product model administration """

    class Meta:
        model = Product
        fields = [
            'barcode', 'title', 'description',
            'image', 'price', 'category'
        ]
