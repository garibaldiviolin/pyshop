""" Manager app views module """

from django.shortcuts import get_object_or_404

from django.urls import reverse_lazy
from django.views.generic import ListView, UpdateView, TemplateView, \
    DeleteView

from website.models import Category, Product
from .forms import CategoryEditForm, ProductEditForm


class IndexView(TemplateView):
    """ Manager app view for the main page """

    template_name = 'index.html'


class CategoriesManagementView(ListView):
    """ ListView for the Category model administration """

    template_name = 'categories_management.html'
    context_object_name = 'categories'

    def get_queryset(self):
        """ Returns the list of category instances """

        queryset = Category.objects.all()
        return queryset


class CategoryEditView(UpdateView):
    """ ListView for editing a specific category instance """

    template_name = 'category_edit.html'
    form_class = CategoryEditForm
    success_url = reverse_lazy('manager:categories')

    def form_valid(self, form):
        """ Verify if the form is valid, and then save it """

        form.save()
        return super(CategoryEditView, self).form_valid(form)

    def get_object(self, queryset=None):
        id = self.kwargs.get('id', None)
        instance = get_object_or_404(Category, id=id)
        return instance


class CategoryDeleteView(DeleteView):
    template_name = 'confirm_delete.html'
    model = Category
    success_url = reverse_lazy('manager:categories')


class ProductsManagementView(ListView):
    template_name = 'products_management.html'
    context_object_name = 'products'

    def get_queryset(self):

        queryset = Product.objects.all()
        return queryset


class ProductEditView(UpdateView):
    template_name = 'product_edit.html'
    form_class = ProductEditForm
    success_url = reverse_lazy('manager:products')

    def form_valid(self, form):
        form.save()
        return super(ProductEditView, self).form_valid(form)

    def get_object(self, queryset=None):
        slug = self.kwargs.get('slug', None)
        instance = get_object_or_404(Product, slug=slug)
        return instance


class ProductDeleteView(DeleteView):
    template_name = 'confirm_delete.html'
    model = Product
    success_url = reverse_lazy('manager:products')
