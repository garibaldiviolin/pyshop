from django.views.generic import ListView

from .models import Product


class ProductsView(ListView):

    template_name = "products.html"
    context_object_name = 'product_list'
    queryset = Product.objects.all()
