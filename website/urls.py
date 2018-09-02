from django.urls import path
from .views import ProductsView

urlpatterns = [
    path('', ProductsView.as_view(), name='index'),
    path('index/', ProductsView.as_view(), name='index'),
    path('products/', ProductsView.as_view()),
]
