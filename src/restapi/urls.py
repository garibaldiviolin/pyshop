from django.urls import path

from .views import CategoryCreateView, ProductCreateView


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
]
