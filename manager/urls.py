from django.urls import path

from .views import ProductsManagementView

app_name = 'manager'

urlpatterns = [
    path('products/', ProductsManagementView.as_view(), name='products'),
]
