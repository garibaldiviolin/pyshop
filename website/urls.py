from django.urls import path
from .views import ProductsView, LoginView

app_name = 'website'

urlpatterns = [
    path('', ProductsView.as_view()),
    path('index/', ProductsView.as_view(), name='index'),
    path('login/', LoginView.as_view(), name='login'),
]
