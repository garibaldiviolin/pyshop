from django.urls import path

from .views import ProductsView, LoginView, LogoutView, SignUpView, \
    AddToKartView, ProductDetailView


app_name = 'website'

urlpatterns = [
    path('', ProductsView.as_view(), name='index'),

    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('signup/', SignUpView.as_view(), name='signup'),

    path(
        'products/<slug:slug>/', ProductDetailView.as_view(),
        name='product-detail'
    ),
    path('add-to-cart/', AddToKartView.as_view(), name='add-to-cart')
]
