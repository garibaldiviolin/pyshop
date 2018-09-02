from django.views.generic import ListView
from django.db.models import Q

from .models import Product


class ProductsView(ListView):

    template_name = "products.html"
    context_object_name = 'product_list'

    def get_queryset(self):
        queryset = Product.objects.all()

        q = self.request.GET.get('q', '')

        if len(q) > 0:
            queryset = queryset.filter(
                Q(title__icontains=q) |
                Q(description__icontains=q)
            )
        return queryset
