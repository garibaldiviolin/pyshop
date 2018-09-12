from django.urls import path

from .views import IndexView, ProductsManagementView, \
    ProductEditView, ProductDeleteView, CategoriesManagementView, \
    CategoryEditView, CategoryDeleteView

app_name = 'manager'

urlpatterns = [
    path('', IndexView.as_view(), name='index'),

    path('categories/', CategoriesManagementView.as_view(), name='categories'),
    path(
        'category-create', CategoryEditView.as_view(), name='category-create'
    ),
    path(
        'category-edit/<int:id>/', CategoryEditView.as_view(),
        name='category-edit'
    ),
    path(
        'category-delete/<int:pk>/', CategoryDeleteView.as_view(),
        name='category-delete'
    ),

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
