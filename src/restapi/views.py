""" restapi views """

from rest_framework.generics import CreateAPIView

from website.models import Category, Product, PaymentMethod, PurchaseOrder
from .serializers import (
    CategorySerializer,
    ProductSerializer,
    PaymentMethodSerializer,
    PurchaseOrderSerializer
)


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


class PaymentMethodCreateView(CreateAPIView):
    """ Create view for PaymentMethod objects """

    queryset = PaymentMethod.objects.all()
    serializer_class = PaymentMethodSerializer
    lookup_field = 'description'


class PurchaseOrderCreateView(CreateAPIView):
    """ Create view for PurchaseOrder objects """

    queryset = PurchaseOrder.objects.all()
    serializer_class = PurchaseOrderSerializer
    lookup_field = 'id'
