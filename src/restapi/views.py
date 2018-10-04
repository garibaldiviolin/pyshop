from rest_framework.generics import CreateAPIView

from website.models import Category, Product
from .serializers import CategorySerializer, ProductSerializer


class CategoryCreateView(CreateAPIView):
    """ Create view for Category objects """

    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    lookup_field = 'description'


class ProductCreateView(CreateAPIView):
    """ Create view for Product objects """

    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'barcode'
