from django.contrib import admin

from .models import Category, Product, PaymentMethod, PurchaseOrder, \
    PurchaseItem, PurchasePaymentMethod, CartOrder, CartItem


admin_models = [
    Category, Product, PaymentMethod, PurchaseOrder,
    PurchaseItem, PurchasePaymentMethod, CartOrder, CartItem
]


for item in admin_models:
    admin.site.register(item)
