from django.urls import path

from .views import ProductsView, LoginView, LogoutView, SignUpView, \
    AddToKartView


app_name = 'website'

urlpatterns = [
    path('', ProductsView.as_view()),
    path('index/', ProductsView.as_view(), name='index'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('signup/', SignUpView.as_view(), name='signup'),
    path('add-to-cart/', AddToKartView.as_view(), name='add-to-cart')
]
