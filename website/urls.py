from django.urls import path

from .views import ProductsView, SignInView, SignOutView, SignUpView, \
    AddToCartView, ProductDetailView, ProfileView, PurchaseOrdersView, \
    PurchaseOrderDetailView


app_name = 'website'

urlpatterns = [
    path('', ProductsView.as_view(), name='index'),

    path('signin/', SignInView.as_view(), name='signin'),
    path('signout/', SignOutView.as_view(), name='signout'),
    path('signup/', SignUpView.as_view(), name='signup'),

    path(
        'purchase-orders/', PurchaseOrdersView.as_view(),
        name='purchase-orders'
    ),
    path(
        'purchase-order/<int:id>/', PurchaseOrderDetailView.as_view(),
        name='purchase-order'
    ),
    path('profile/', ProfileView.as_view(), name='profile'),

    path(
        'products/<slug:slug>/', ProductDetailView.as_view(),
        name='product-detail'
    ),
    path('add-to-cart/', AddToCartView.as_view(), name='add-to-cart')
]
