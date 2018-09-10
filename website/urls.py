from django.urls import path

from .views import ProductsView, SignInView, SignOutView, SignUpView, \
    AddToCartView, ProductDetailView, ProfileView, UserPurchaseView


app_name = 'website'

urlpatterns = [
    path('', ProductsView.as_view(), name='index'),

    path('signin/', SignInView.as_view(), name='signin'),
    path('signout/', SignOutView.as_view(), name='signout'),
    path('signup/', SignUpView.as_view(), name='signup'),

    path('user-purchases/', UserPurchaseView.as_view(), name='user-purchases'),
    path('profile/', ProfileView.as_view(), name='profile'),

    path(
        'products/<slug:slug>/', ProductDetailView.as_view(),
        name='product-detail'
    ),
    path('add-to-cart/', AddToCartView.as_view(), name='add-to-cart')
]
