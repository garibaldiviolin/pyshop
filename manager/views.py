from django.views.generic import TemplateView


class ProductsManagementView(TemplateView):

    template_name = 'products_management.html'

    def get_context_data(self, *args, **kwargs):
        context = super(ProductsManagementView, self).get_context_data(
            *args, **kwargs
        )
        return context
