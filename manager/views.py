from django.views.generic import FormView

from .forms import ProductManagementForm


class ProductsManagementView(FormView):
    template_name = 'products_management.html'
    form_class = ProductManagementForm
    success_url = 'manager:index/'

    def form_valid(self, form):
        return super().form_valid(form)
