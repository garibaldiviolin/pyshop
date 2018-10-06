""" website models registered in admin (Django) """

from django.contrib import admin

from .models import Category, Product, PaymentMethod, PurchaseOrder, \
    PurchaseItem, PurchasePaymentMethod


admin_models = [
    Category, Product, PaymentMethod, PurchaseOrder,
    PurchaseItem, PurchasePaymentMethod
]


for item in admin_models:
    admin.site.register(item)
