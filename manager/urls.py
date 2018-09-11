from django.urls import path

from .views import IndexView, ProductsManagementView, \
    ProductEditView, ProductDeleteView

app_name = 'manager'

urlpatterns = [
    path('', IndexView.as_view(), name='index'),

    path('products/', ProductsManagementView.as_view(), name='products'),
    path('product-create', ProductEditView.as_view(), name='product-create'),
    path(
        'product-edit/<slug:slug>/', ProductEditView.as_view(),
        name='product-edit'
    ),
    path(
        'product-delete/<slug:slug>/', ProductDeleteView.as_view(),
        name='product-delete'
    ),
]
