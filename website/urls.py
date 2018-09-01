from django.urls import path
from .views import ProductsView

urlpatterns = [
    path('products/', ProductsView.as_view()),
]
