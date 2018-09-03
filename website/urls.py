from django.urls import path
from .views import ProductsView, LoginView, LogoutView

app_name = 'website'

urlpatterns = [
    path('', ProductsView.as_view()),
    path('index/', ProductsView.as_view(), name='index'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
]
