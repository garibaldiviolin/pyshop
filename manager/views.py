from django.shortcuts import get_object_or_404

from django.urls import reverse_lazy
from django.views.generic import ListView, UpdateView, TemplateView, \
    DeleteView

from website.models import Product
from .forms import ProductEditForm


class IndexView(TemplateView):

    template_name = 'index.html'


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
        # pdb.set_trace()
        slug = self.kwargs.get('slug', None)
        if slug is not None:
            instance = get_object_or_404(Product, slug=slug)
            return instance
        else:
            return None


class ProductDeleteView(DeleteView):
    template_name = 'product_confirm_delete.html'
    model = Product
    success_url = reverse_lazy('manager:products')
