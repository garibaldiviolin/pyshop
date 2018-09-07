from django.contrib import admin

from .models import Category, Product, PaymentMethod, PurchaseOrder, PurchaseItem, \
    PurchasePaymentMethod, CartProduct


admin_models = [
    Category, Product, PaymentMethod, PurchaseOrder,
    PurchaseItem, PurchasePaymentMethod, CartProduct
]


for item in admin_models:
    admin.site.register(item)
