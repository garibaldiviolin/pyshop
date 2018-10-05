from django.urls import path

from .views import (
    CategoryCreateView,
    ProductCreateView,
    PaymentMethodCreateView
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
]
