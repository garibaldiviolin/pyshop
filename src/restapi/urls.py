""" restapi urls """

from django.urls import path

from .views import (
    CategoryCreateView,
    ProductCreateView,
    PaymentMethodCreateView,
    PurchaseOrderCreateView,
    PurchaseItemCreateView
)


app_name = 'restapi'

urlpatterns = [
    path(
        'v1/categories/',
        CategoryCreateView.as_view(),
        name='categories'
    ),
    path(
        'v1/products/',
        ProductCreateView.as_view(),
        name='products'
    ),
    path(
        'v1/payment-methods/',
        PaymentMethodCreateView.as_view(),
        name='payment-methods'
    ),
    path(
        'v1/purchase-orders/',
        PurchaseOrderCreateView.as_view(),
        name='purchase-orders'
    ),
    path(
        'v1/purchase-items/',
        PurchaseItemCreateView.as_view(),
        name='purchase-items'
    ),
]
