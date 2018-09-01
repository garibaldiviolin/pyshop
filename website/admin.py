from django.contrib import admin

from .models import Product, PaymentMethod, PurchaseOrder, PurchaseItem, \
    PurchasePaymentMethod


admin_models = [
    Product, PaymentMethod, PurchaseOrder,
    PurchaseItem, PurchasePaymentMethod
]


for item in admin_models:
    admin.site.register(item)
